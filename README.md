# python_to_do_list
A desktop To-Do List application built with Python (Tkinter GUI) and MySQL to manage daily tasks efficiently.

## Current Features
* A desktop GUI built with Python's Tkinter.
* Display, add, and delete tasks seamlessly through the interface.
* pop-up notifications (Success & Warning messages) for input validation.

## Prerequisites & Technologies
- **Python 3.11**
- **MySQL Database**
- **mysql-connector-python** library
- **Tkinter** (Built-in Python GUI library)

## Database Setup
To run this project locally, you need to import the database structure:
1. Open your MySQL Workbench or terminal.
2. Run the queries inside the `ToDo_DB.sql` file to create the database and the `tasks` table.
3. Update the database configuration (host, user, password) in `To-do-list.py` to match your local setup.
