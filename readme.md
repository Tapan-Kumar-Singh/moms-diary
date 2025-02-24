## MOMS DIARY
Mom's Diary is a Python-based web application built with Flask. It helps manage household expenses efficiently with an easy-to-use interface.

##### Feature of Mom's diary
- Designed to track and manage home expenses on a delayed basis.
- Simple and intuitive UI for effortless expense management.

##### Functionlity of Mom's diary:
 ```🚀 Updates coming soon... ```

#### 01. Installation
- Ensure that Python 3 is installed on your device.

##### Steps to install application
###### Clone the Repository 
Run the following command to clone the project from GitHub:

 ```bash 
    git clone https://github.com/Tapan-Kumar-Singh/moms-diary.git
```
- Install the necessery packages from requirements.txt

#### 01. Create database:
```bash
flask db init
```
```bash
flask db migrate -m "Initial migration"
```
```bash
flask db upgrade
```

#### 02. Create a new Admin User Using Flask Shell:

```bash
flask shell
```

```bash
from models import db, User  # Import the database and User model
from werkzeug.security import generate_password_hash  # Import password hashing

# Create a new admin user
admin = User(
    full_name="Admin User",
    user_name="admin",
    password_hash=generate_password_hash("admin123"),  # Hash password
    is_financer=True  # Set as financer if needed
)

# Add to database and commit changes
db.session.add(admin)
db.session.commit()

print("Admin user created successfully!")
```
After running the above commands, you can check if the user was successfully created:
```bash
User.query.all()
```

#### 04. Exit from Flask shell:

```bash
exit()
```
