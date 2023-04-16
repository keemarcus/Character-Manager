# import flask
from flask import Flask, request, redirect, url_for, session, make_response, flash, render_template
# from flask_session import Session

# set up flask app
app = Flask(__name__, static_url_path='')