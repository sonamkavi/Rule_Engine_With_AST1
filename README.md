# Rule Engine API with AST
This project implements a simple 3-tier rule engine that evaluates user eligibility based on rules. The rules are represented as an Abstract Syntax Tree (AST) and support dynamic creation, combination, and modification. The rule engine is exposed as a RESTful API using Flask.
- Table of Contents
   - Project Overview
   - Features
  -Technologies Used
* Getting Started
     - Prerequisites
     - Installation
     - Running the Application
* API Endpoints
       - Create Rule
       - Combine Rules
       - Evaluate Rule
* Testing
* Project Structure
* Design Choices
* Build and Deployment
* Additional Notes
 
   

# Project Overview
The Rule Engine is designed to evaluate user eligibility based on customizable rules such as age, department, salary, etc. The rules are dynamically represented as an Abstract Syntax Tree (AST). The project includes:
 - A simple UI (to be implemented if needed)
 - A backend rule engine API (Flask-based)
 - Data storage for storing rule logic and metadata (SQLite or any preferred DB)
# Features
  - Create Rules: Convert a rule string into an Abstract Syntax Tree (AST).
  - Combine Rules: Combine multiple rules into one logical structure.
  - Evaluate Rules: Evaluate rules against user-provided data.
  - Dynamic Rule Creation: Create, modify, and combine rules dynamically using AST representation.

 ## Extra Features Implemented

In addition to the basic requirements, the following enhancements were made to the project:

1. **Modifiable Rules**: 
   - Users can modify existing rules dynamically through API endpoints, allowing for more flexible rule management.
2. **User-Defined Functions**:
   - Added the ability to define custom functions within rules for advanced conditions, allowing users to implement complex logic beyond basic comparisons.
3. **Enhanced Error Handling**:
   - Improved error handling and validation to ensure that rules follow the correct syntax and structure before being processed.
4. **Database Integration**:
   - Implemented a simple SQLite database to store created rules and their metadata, providing persistence across sessions.
   - API endpoints for inserting and fetching rules from the database.
5. **Detailed Logging**:
   - Added logging functionality to track requests and rule evaluations for debugging purposes.

# Technologies Used
   - Python 3.7+
   - Flask (Web framework)
   - SQLite (Database for storing rule logic and metadata 
   -  Postman (For API testing)

# Getting Started
 # Prerequisites
- Ensure you have the following installed:

   - Python 3.7
   - Flask
  - SQLite3 
  - Postman (for testing APIs)
 # Installation
1. Clone the Repository:
   ```

   git clone https://github.com/yourusername/rule-engine-api.git cd rule-engine-api


   ```
2. Set Up Virtual Environment:
   ```
  
   python -m venv venv 
  
   ```
   ```
   - source venv/bin/activate  # On Windows use `venv\Scripts\activate`

   ```
3. Install Dependencies:
   ```
   pip install -r requirements.txt

   ```

4. Set Up the Database: If you're using SQLite (you can also set up other databases if needed):
   ```
   sqlite3 rule_engine.db

   ```
# Running the Application
To start the Flask application:
 ```
python api.py
```
The application will run at http://127.0.0.1:5000/ by default.

# API Endpoints
1. Create Rule
  - Endpoint: /create_rule
  - Method: POST
  - Description: Converts a rule string into an Abstract Syntax Tree (AST).
  - Request Body:

    ```
    {
    "rule_string": "age > 30 AND department = 'Sales'"
    }
    ```
  - Response
    ```
     {
    "ast": "AST representation of the rule"
    }
    ```
2. Combine Rules
  - Endpoint: /combine_rules
  - Method: POST
  - Description: Combines multiple rules into one using logical operators.
  - Request Body:
  ```
  {
    "rules": ["age > 30", "salary > 50000"]
  }
  ```
  - Response:
  ```
  {
    "combined_ast": "Combined AST representation"
  }
 ```
3. Evaluate Rule
  - Endpoint: /evaluate_rule
  - Method: POST
  - Description: Evaluates a rule (AST) against user data.
  - Request Body:
    ```
    {
    "ast": {
        "type": "operator",
        "value": "AND",
        "left": {
            "type": "operand",
            "value": ["age", ">", 30]
        },
        "right": {
            "type": "operand",
            "value": ["department", "=", "Sales"]
        }
    },
    "data": {
        "age": 35,
        "department": "Sales"
    }
    }
    ```
   - Response
     ```
     {
      "result": true
      }
     ```
# Testing
  - To run unit tests, execute the following command:
    ```
    python -m unittest tests.py
    ```
# Project Structure
```
 
├── api.py               # Flask API entry point
├── rule_engine.py       # Core rule engine logic
├── database.py          # Database handling (storing and retrieving rules)
├── tests.py             # Unit tests for rule engine
├── requirements.txt     # Python dependencies          
└── README.md            # Project documentation
```




 










