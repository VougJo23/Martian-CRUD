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
git clone https://github.com/VougJo23/Martian-CRUD.git
cd Martian-CRUD
```

### **3️⃣ Run the Application**

▶️ Method 1: Running Locally (Python Environment)
Install Dependencies
```bash
pip install -e .
```
Run the App
```bash
martian-compiler
```
or 
```bash
python -m martian_crud.main
```

▶️ Method 2: Running with Docker
Build Docker Image & Run the App
```bash
docker build -t martian-crud .
docker run -p 5000:5000 martian-crud
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

