# import our flask app from app.py
from src.app import app

# import our user and reimbursement controllers for our app
from src.controllers import spellbook_controller
from src.controllers import spell_controller

# start our application when main.py is running
if __name__ == '__main__':
    app.secret_key = 'super_secret'
    app.run()
