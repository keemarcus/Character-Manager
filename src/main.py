# import our flask app from app.py
import logging

from src.app import app, session, redirect

# import our service level logic for reimbursements
import src.service.spellbook_service as service

# import our user and reimbursement controllers for our app
from controllers import spellbook_controller, spell_controller, character_controller

# redirect to our static home page
@app.route('/spellbook/<int:spellbook_id>', methods=['GET'])
def spellbook(spellbook_id):
    session['spellbook_id'] = spellbook_id
    session['user_id'] = service.get_user_id(spellbook_id)
    return redirect('../spellbook.html')

# start our application when main.py is running
if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    #app.config['SESSION_TYPE'] = 'memcached'
    #app.secret_key = 'super_secret'
    #session['user_id'] = 1
    app.run()

