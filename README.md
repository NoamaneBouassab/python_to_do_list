# python_to_do_list
A desktop To-Do List application built with Python to manage daily tasks efficiently.

## Current Features
* Show tasks via Terminal with auto-numbering.
* Add new tasks dynamically.
* Delete tasks with input validation.

## Prerequisites & Technologies
- **Python 3.11**
- **MySQL Database**
- **mysql-connector-python** library

## Database Setup
To run this project locally, you need to import the database structure:
1. Open your MySQL Workbench or terminal.
2. Run the queries inside the `ToDo_DB.sql` file to create the database and the `tasks` table.
3. Update the database configuration (host, user, password) in `To-do-list.py` to match your local setup.
