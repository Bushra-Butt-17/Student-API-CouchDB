
<img src='https://github.com/user-attachments/assets/76652fd3-996d-4feb-8aa6-1aabe569fe94' width=100%>

https://github.com/user-attachments/assets/34d42e04-7f48-4a92-b46b-74396554ed22


---

# 📚 **Student Management System - Flask with CouchDB**

Welcome to the **Student Management System** built using **Flask** and **CouchDB**! 🚀 This project enables users to **Create**, **Read**, **Update**, and **Delete** student records through a simple web interface, utilizing a **CouchDB** NoSQL database for storing student data.

## 🔗 Demo Link

Check out the live demo of this application:  
[Student Management System Demo](http://your-demo-link.com)

---

## 🚀 **Features**

- **✨ CRUD Operations**: Allows users to **Create**, **Read**, **Update**, and **Delete** student records.
- **📚 Manage Student Data**: Manage student information including **name**, **age**, and **grade**.
- **💻 Web Interface**: A user-friendly interface built using **Flask** and **Bootstrap** for a responsive design.
- **🔒 Flash Messages**: Displays success or error messages based on user actions (e.g., add, update, delete students).
- **📱 Mobile-Friendly**: Fully responsive, making the application accessible on both desktop and mobile devices.

---

## 🛠️ **Technologies Used**

- **Flask**: The Python web framework used for building the backend.
- **CouchDB**: A NoSQL database to store and manage student records in JSON format.
- **Bootstrap**: A front-end framework for responsive and mobile-first web pages.
- **HTML/CSS**: For the structure and styling of the web interface.

---

## 🔧 **Installation & Setup**

### Prerequisites

Before you start, ensure you have the following installed:

- **Python 3.x**
- **CouchDB** (for database storage)
- **Flask** (Python web framework)
- **Bootstrap** (via CDN for front-end)

---

### 1. **Clone the Repository**

```bash
git clone https://github.com/your-username/student-api-couchdb.git
cd student-api-couchdb
```

---

### 2. **Install Dependencies**

Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

Activate the virtual environment:

- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source venv/bin/activate
  ```

Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. **Set Up CouchDB**

Make sure you have **CouchDB** installed and running on your local machine. You can download it from [here](https://couchdb.apache.org/).

#### Create a CouchDB Database:

- Open the CouchDB dashboard by navigating to `http://127.0.0.1:5984/_utils/` in your browser.
- Create a new database named `students`.

Alternatively, you can use the following command to create a database programmatically:

```bash
curl -X PUT http://localhost:5984/students
```

---

### 4. **Configure CouchDB in Flask**

In `app.py`, configure the CouchDB URL for your application:

```python
from couchdb import Server

server = Server('http://localhost:5984/')
db = server['students']  # Use the "students" database
```

---

### 5. **Run the Application**

After setting up CouchDB, start the Flask application:

```bash
python app.py
```

The app should be running on `http://127.0.0.1:5000`. Open this link in your browser to interact with the Student Management System.

---

## 🌟 **How It Works**

This application provides basic **CRUD (Create, Read, Update, Delete)** functionality to manage student records. The steps for each operation are as follows:

### 1. **Create (Add Student)**

- Fill out the **Add Student** form with details like:
  - **Name**
  - **Age**
  - **Grade**
  
- After submission, the student data is stored in the **CouchDB** database.

### 2. **Read (View Students)**

- View all students in a dynamic table.
- Each student entry displays their **Name**, **Age**, and **Grade**.

### 3. **Update (Edit Student)**

- Edit existing student information using an **Edit** button next to each record.
- Modify **Name**, **Age**, or **Grade**, and save the changes to the database.

### 4. **Delete (Remove Student)**

- Delete a student record by clicking the **Delete** button next to their entry.

---

## 🎨 **UI Preview**

### 1. **Home Page**
The homepage displays the list of all students in a table, with options to **Add**, **Edit**, and **Delete** students.
![Main](https://github.com/user-attachments/assets/df7a90ab-e03c-4635-bb8c-0233144f62b2)
![Main1](https://github.com/user-attachments/assets/5d6b34d7-4226-48ce-80dc-df5c697b77a0)
![Main3](https://github.com/user-attachments/assets/1db6a08e-83f1-4a60-9eb6-17129f0634e4)
![Main2](https://github.com/user-attachments/assets/f3e16e50-b90b-4e04-99ce-7796619544e8)

### 2. **Add Student Form**
A simple form where users can add a new student by entering their **Name**, **Age**, and **Grade**.
![Add-Students](https://github.com/user-attachments/assets/30ed59f0-37e2-4188-a277-3e37c869cf37)
![Add-Form](https://github.com/user-attachments/assets/bc85cafa-8e5a-4ced-9e95-79ebc986f309)
![Added-Student](https://github.com/user-attachments/assets/3381723c-f3ba-4a30-980e-b7151d18d139)


### 3. **Update Student Form**
A form to edit an existing student's details.

![Update Student Form](https://github.com/user-attachments/assets/update-student-form-preview.jpg)

---

## ⚙️ **Folder Structure**

Here’s the structure of the project:

```
student-api-couchdb/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
│
├── templates/           # HTML templates (Flask uses Jinja2 templating)
│   ├── index.html        # Home page template
│   ├── add_student.html # Add student form template
│   └── update_student.html  # Update student form template
│
├── assets/              # Folder for static assets
│   ├── images/          # Folder for images          
│
└── README.md            # Project README
```

---

## 📝 **Contributing**

Contributions are welcome! If you find any issues or have ideas for improvements, feel free to open an issue or create a pull request. Here's how you can contribute:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

---

## 🛠️ **License**

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 💬 **Contact**

Feel free to reach out with questions, suggestions, or feedback at [email@example.com](mailto:bsdsf21m020@pucit.edu.pk).

Made with ❤️ by 

---

