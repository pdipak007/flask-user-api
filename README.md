# Flask User API

A simple Flask REST API that returns static user data in JSON format.

---

**How to Run This Project**

**Step 1: Clone the Repository**

**git clone https://github.com/pdipak007/flask-user-api.git**  
**cd flask-user-api**

**Step 2: Create Virtual Environment (Optional but Recommended)**

**python3 -m venv venv**  
**source venv/bin/activate**  (For Linux/Mac)  
**venv\Scripts\activate**     (For Windows)

**Step 3: Install Required Packages**

**pip install -r requirements.txt**

**Step 4: Run the Flask App**

**python app.py**

You will see:

Running on http://127.0.0.1:5000/


Now the API is live locally.

---

**Step 5: Run with Docker**

**docker build -t flask-user-api .**

**docker run -d -p 5000:5000 flask-user-api**

Now the Docker container is running.

Open this in your browser:  
**http://localhost:5000/user**

---

**API Endpoints**

**GET /user**  
Returns a list of 10 sample users in JSON format.

**Sample Response:**

```json
[
  {
    "id": 1,
    "name": "Amit",
    "email": "amit@example.com"
  },
  
]
```
---

**API Output Screenshot:**
 
![API Output](output.png)


---

**Project Structure:**

flask-user-api/  
├── app.py             - Main Flask application  
├── requirements.txt   - Python dependencies  
├── Dockerfile         - Docker configuration  
├── output.png         - Screenshot of API output  
└── README.md          - Documentation

---
