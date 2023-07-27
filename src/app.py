# import flask
from flask import Flask, request, redirect, url_for, session, make_response, flash, render_template
# from flask_session import Session

# set up flask app
app = Flask(__name__, static_url_path='')


# redirect to our static home page
@app.route('/', methods=['GET'])
def home():
    return redirect('../home.html')


@app.route('/session/spellbook_id', methods=['GET'])
def session_spellbook_id():
    return str(session.get('spellbook_id'))


@app.route('/session/user_id', methods=['GET'])
def session_user_id():
    return str(session.get('user_id'))
