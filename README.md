# Flask User API

A simple Flask REST API that **uses a SQLite database**, returns real user data in JSON format, and is ready for Docker Compose with multi-service support.

---

**How to Run This Project**

---

**Option A: Run Locally**

**Step 1: Clone the Repository**

```bash
git clone https://github.com/pdipak007/flask-user-api.git
cd flask-user-api
```

**Step 2: Create Virtual Environment (Optional but Recommended)**
```python
python3 -m venv venv
source venv/bin/activate    # For Linux/Mac
venv\Scripts\activate       # For Windows
```

**Step 3: Install Required Packages**
```
pip install -r requirements.txt
```

**Step 4: Initialize the Database**
```python
python init_db.py
```

This will create users.db inside the db/ folder and insert 10 dummy users.

**Step 5: Run the Flask App**
```python
python app.py
```

You will see:
```
Running on http://127.0.0.1:5000/
Now the API is live locally.
```

---

**Option B: Run with Docker (Single Container)**

**Step 1: Build the Docker Image**
```
docker build -t flask-user-api
```

**Step 2: Run the Container**
```
docker run -d -p 5000:5000 flask-user-api
```

Open in browser:
```
http://localhost:5000/user
```

---

**Option C: Run with Docker Compose (Recommended with DB Setup)**

This option automatically sets up:

A volume-mounted SQLite database (db/users.db)

Table creation via init_db.py

Dummy data insertion

Flask app running inside Docker container

**Step 1: Make sure Docker Compose is installed**
```
docker-compose --version
```

If not installed:
```
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.7/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose
```

**Step 2: Run Everything**
```
docker-compose up --build
```

Then open:
```
http://localhost:5000/user
```

---

**API Endpoints**

**GET /user**

Returns a list of users from the SQLite database.

Sample Response:
```
[
  {
    "id": 1,
    "name": "Amit",
    "email": "amit@example.com"
  },
  {
    "id": 2,
    "name": "Sita",
    "email": "sita@example.com"
  },
 
]
```


---

**API Output Screenshot**

![API Output](output.png)

---

**Project Structure:**
```
flask-user-api/
├── app.py             - Main Flask application
├── init_db.py         - Creates table and inserts dummy users
├── requirements.txt   - Python dependencies
├── Dockerfile         - Docker configuration
├── docker-compose.yml - Multi-service setup
├── db/                - Folder to store SQLite DB file
│   └── users.db       - Created automatically
├── output.png         - Screenshot of API output
└── README.md          - Documentation
```

---
