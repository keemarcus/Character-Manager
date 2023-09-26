# import our flask app from app.py
import logging

from src.app import app

# import our user and reimbursement controllers for our app
from src.controllers import spellbook_controller, spell_controller, character_controller

# start our application when main.py is running
if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.secret_key = 'super_secret'
    app.run()

