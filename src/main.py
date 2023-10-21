# import our flask app from app.py
import logging

from app import app

# import our user and reimbursement controllers for our app

# start our application when main.py is running
if __name__ == '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    #app.config['SESSION_TYPE'] = 'memcached'
    #app.secret_key = 'super_secret'
    #session['user_id'] = 1
    app.run()

