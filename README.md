# Task Description:
Create a simple listing for the employee's attendance system. 

Use Django Web Framework for the project. 

Create the project in a virtual environment. Make requirements.txt file with all libraries used for the project. Use Postgresql as a database.

Employee Model (name, email, mobile, department(Development/Testing/HR)) with validated forms(All fields are mandatory to fill) Add / Edit / Update / Delete the employee details 

Employee attendance Model (employee_id, date, is_present) 

Two buttons for attendance table view 
(1. View Today's attendance 2. All attendance) 

if click the first button then view today's attendance if already filled 

if not then open the edit form to fill each employee's attendance on a single page then click the save button to update attendance and redirect to today's attendance table


# A few Steps for run the project:
- clone repo from given GitHub url
- create virtual environment and activate it
- install dependencies from "requirements.txt" using pip install - r requirements.txt command
- run command ````python manage.py migrate```
- run command "python manage.py createsuperuser"
- then run "python manage.py runserver"


# Technologies used:
- Frontend (Bootstrap - 5.3)
- Backend (Django web framework - 5.0)
- Database (sqlite3 or Postgres SQL database)

# Note: 
- Internet is required for run the project because of I used bootstrap CDN
