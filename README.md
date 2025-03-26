# Martian-CRUD
CI/CD pipeline for automating the build, test, and deployment of Mission Control CRUD

# 🚦 Phase 1: Mission Repository Initialization

## 📌 Features
- **Create** resources
- **Retrieve** all resources
- **Retrieve** a single resource
- **Update** a resource 
- **Delete** all resources 
- **Delete** a resource 

## 🛠 Setup & Installation

### **1️⃣ Prerequisites**
Ensure you have **Python 3.10+** installed.

### **2️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### **3️⃣ Install Dependencies**
```bash
pip install flask flask_sqlalchemy
```

### **4️⃣ Run the Application**
```bash
python app.py
```
You should see:
```
* Running on http://127.0.0.1:5000/
```

---

## 🌍 API Endpoints

### **🔹 Create a Resource**
- **Method:** `POST`
- **Endpoint:** `/resources`
- **Request Example:**
  ```bash
  curl -X POST http://127.0.0.1:5000/resources \
       -H "Content-Type: application/json" \
       -d "{\"name\": \"Oxygen Tanks\", \"quantity\": 50}"
  ```

### **🔹 Get All Resources**
- **Method:** `GET`
- **Endpoint:** `/resources`
- **Request Example:**
  ```bash
  curl -X GET http://127.0.0.1:5000/resources
  ```

### **🔹 Get a Single Resource**
- **Method:** `GET`
- **Endpoint:** `/resources/<id>`
- **Request Example:**
  ```bash
  curl -X GET http://127.0.0.1:5000/resources/1
  ```

### **🔹 Update a Resource**
- **Method:** `PUT`
- **Endpoint:** `/resources/<id>`
- **Request Example:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/resources/1 \
       -H "Content-Type: application/json" \
       -d "{\"quantity\": 75}"
  ```

### **🔹 Delete all Resources**
- **Method:** `DELETE`
- **Endpoint:** `/resources`
- **Request Example:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/resources
  ```

### **🔹 Delete a Single Resource**
- **Method:** `DELETE`
- **Endpoint:** `/resources/<id>`
- **Request Example:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/resources/1
  ```


---

## 📝 Notes
- The application uses **SQLite in-memory storage**, meaning data is lost when the app restarts.
- Modify `app.py` if you need persistent storage.

