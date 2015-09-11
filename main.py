import os
import sys
import urllib

from urlparse import urlparse

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import urlfetch

from flask import Flask
from flaskext.appengine import(
  AppEngine, login_required
)
from flask import request
from flask import Response
  
app = Flask(__name__)
app.config['DEBUG'] = True

gae = AppEngine(app)

import jinja2
jn2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)



# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
@login_required
def hello():
    """Return a friendly HTTP greeting."""
    return 'ok'

@app.route('/event')
@login_required
def event():
    return 'event'


@app.route('/message/<int:room_id>', methods=['GET','POST'])
#@login_required
def message(room_id):
  Url="https://api.chatwork.com/v1/rooms/%d/messages" % room_id
  form_fields = {
    "body": "body data not found"
  }

  if request.method == 'POST':
    form_fields['body'] = request.form['body'].encode('utf-8')
 
  if request.method == 'GET':
    form_fields['body'] = request.args.get("body").encode('utf-8')

  form_data = urllib.urlencode(form_fields)
  result = urlfetch.fetch(url=Url,
    payload=form_data,
    method=urlfetch.POST,
    headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': ''})

  return 'ok'


@app.route('/task/<int:room_id>', methods=['GET','POST'])
def task(room_id):
  return 'ok'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
