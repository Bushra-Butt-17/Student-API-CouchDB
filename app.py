from flask import Flask, render_template, request, redirect, url_for
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, render_template, request, redirect, url_for, flash
import requests
from requests.auth import HTTPBasicAuth
import os
app = Flask(__name__)
# Set a secret key for session management
app.secret_key = os.urandom(24)  # Generates a random secret key, for security

# CouchDB configuration
COUCHDB_URL = "http://localhost:5984"
DB_NAME = "students"
USERNAME = "<>"  # Replace with your CouchDB username
PASSWORD = "<>"  # Replace with your CouchDB password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        # Get the data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        grade = request.form.get('grade')

        student_data = {
            "name": name,
            "age": age,
            "grade": grade
        }

        # Send the data to CouchDB with authentication
        response = requests.post(
            f"{COUCHDB_URL}/{DB_NAME}",
            json=student_data,
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )

        if response.status_code == 201:
            return redirect(url_for('index'))  # Redirect to the index page after success
        else:
            return f"Error: {response.text}"

    return render_template('add_student.html')  # Render the form when the page is accessed via GET


@app.route('/view_students')
def view_students():
    # Fetch the list of students from CouchDB
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/_all_docs?include_docs=true",
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        students = [doc['doc'] for doc in response.json()['rows']]  # Extract the student documents
        return render_template('view_students.html', students=students)
    else:
        return f"Error: {response.text}"



@app.route('/update_student/<doc_id>', methods=['GET', 'POST'])
def update_student(doc_id):
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        grade = request.form.get('grade')

        # Fetch the current document revision (_rev)
        response = requests.get(
            f"{COUCHDB_URL}/{DB_NAME}/{doc_id}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )

        if response.status_code == 200:
            doc = response.json()
            rev = doc['_rev']  # Get the document revision (_rev)

            # Prepare the updated student data along with the revision
            student_data = {
                "_id": doc_id,
                "_rev": rev,  # Include the current revision
                "name": name,
                "age": age,
                "grade": grade
            }

            # Send the updated data to CouchDB
            update_response = requests.put(
                f"{COUCHDB_URL}/{DB_NAME}/{doc_id}",
                json=student_data,
                auth=HTTPBasicAuth(USERNAME, PASSWORD)
            )

            if update_response.status_code == 201:
                flash('Student updated successfully!', 'success')
                return redirect(url_for('view_students'))  # Redirect after success
            else:
                flash(f"Error: {update_response.text}", 'danger')
                return redirect(url_for('view_students'))

        else:
            flash(f"Error: {response.text}", 'danger')
            return redirect(url_for('view_students'))

    # Fetch the current student's data to prefill the form
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/{doc_id}",
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        student = response.json()
        return render_template('update_student.html', student=student)
    else:
        flash(f"Error: {response.text}", 'danger')
        return redirect(url_for('view_students'))

@app.route('/delete_student/<doc_id>', methods=['POST'])
def delete_student(doc_id):
    # First, retrieve the document revision to delete the student
    response = requests.get(
        f"{COUCHDB_URL}/{DB_NAME}/{doc_id}",
        auth=HTTPBasicAuth(USERNAME, PASSWORD)
    )

    if response.status_code == 200:
        doc = response.json()
        rev = doc['_rev']  # Get the document revision

        # Delete the student document from CouchDB
        delete_response = requests.delete(
            f"{COUCHDB_URL}/{DB_NAME}/{doc_id}?rev={rev}",
            auth=HTTPBasicAuth(USERNAME, PASSWORD)
        )

        if delete_response.status_code == 200:
            flash('Student deleted successfully!', 'success')
            return redirect(url_for('view_students'))  # Redirect after success
        else:
            flash(f"Error: {delete_response.text}", 'danger')
            return redirect(url_for('view_students'))
    else:
        flash(f"Error: {response.text}", 'danger')
        return redirect(url_for('view_students'))

if __name__ == '__main__':
    app.run(debug=True)

