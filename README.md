# Bank System API

## Project Purpose

This project is a simple bank management system designed to demonstrate a RESTful API built with Django and Django REST Framework.  
It allows management of users, user groups, bank accounts, and financial transactions with both API endpoints and user-friendly UI views.  

The main goals are:  
- To provide a secure and organized backend for basic banking operations  
- To demonstrate API development and frontend UI integration  
- To offer a foundation for further banking application development  

---

## API Endpoints

| URL                                  | Description                          |
|------------------------------------|------------------------------------|
| `http://localhost:8000/api/accounts/`      | List and manage bank accounts (JSON) |
| `http://localhost:8000/api/transactions/`  | List and manage transactions (JSON)  |
| `http://localhost:8000/api/users/`          | List users (JSON)                    |
| `http://localhost:8000/api/groups/`         | List groups (JSON)                   |

## UI Endpoints

| URL                                   | Description                                |
|-------------------------------------|--------------------------------------------|
| [http://localhost:8000/api/accounts/ui/](http://localhost:8000/api/accounts/ui/)       | Displays bank accounts as a visual list     |
| [http://localhost:8000/api/transactions/ui/](http://localhost:8000/api/transactions/ui/) | Shows all transactions in a table/card      |
| [http://localhost:8000/api/users/ui/](http://localhost:8000/api/users/ui/)             | Lists users as cards                         |
| [http://localhost:8000/api/groups/ui/](http://localhost:8000/api/groups/ui/)           | Lists groups along with their users         |

---

## Prerequisites

- Python 3.8 or higher  
- PostgreSQL installed and running  
- Virtual environment tool (recommended: `venv` or `virtualenv`)
