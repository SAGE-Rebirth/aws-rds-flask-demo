
# AWS RDS Flask Demo

This project demonstrates how to integrate a Flask web application with an AWS RDS MySQL database. It covers the steps required to set up a virtual environment, configure the database, and run the Flask server. This example is designed to help developers understand the fundamentals of using cloud-hosted databases with Flask applications.

---

## Steps to Configure and Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/SAGE-Rebirth/aws-rds-flask-demo.git
```

### 2. Navigate to the Project Directory
```bash
cd aws-rds-flask-demo
```

### 3. Prerequisites
- Ensure Python 3.x is installed on your system.
- Install the `virtualenv` Python package if not already installed:
  ```bash
  pip install virtualenv
  ```

### 4. Set Up the Virtual Environment
1. Create a new virtual environment:
   ```bash
   py -m venv new-env
   ```
   > Replace `new-env` with your preferred name.

2. Activate the virtual environment:
   - On Windows:
     ```bash
     new-env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source new-env/bin/activate
     ```

### 5. Install Dependencies
Install all required Python packages:
```bash
pip install -r requirements.txt
```

### 6. Verify Package Installation
Check that all necessary packages are installed:
```bash
pip list
```

### 7. Configure the Project
- Edit the `config.py` file to update the **RDS endpoint**. Use the following format:
  ```
  mysql+pymysql://<username>:<password>@<rds-database-endpoint>/<database-name>
  ```
  - Replace `<username>`, `<password>`, `<rds-database-endpoint>`, and `<database-name>` with your database credentials.
  - **Note:** Do not include angle brackets (`<>`) when entering the values.

- Execute the SQL queries in `table-query.txt` to set up the required database tables. Modify the queries if necessary, but ensure corresponding changes are reflected in the code.

### 8. Start the Flask Server
Run the following command to start the server:
```bash
py run.py
```

---

## Notes
- **Environment Activation**: Ensure the virtual environment is activated before executing any Python commands or installing packages.
- **Database Configuration**: Double-check the credentials and endpoint to avoid connection issues.
- **SQL Queries**: Execute the provided queries carefully to avoid schema mismatches with the application code.

---

Happy Coding! 🎉
