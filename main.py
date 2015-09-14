import os
import sys
import urllib
import time
import datetime
import dateutil.parser

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


CHATWORK_API_TOKEN = '9faad66c13223a882c6e7f01fe22dace'

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
    "body": "no message body"
  }

  if request.method == 'POST':
    form_fields['body'] = request.form['body'].encode('utf-8')
 
  if request.method == 'GET':
    form_fields['body'] = request.args.get("body").encode('utf-8')

  form_data = urllib.urlencode(form_fields)
  result = urlfetch.fetch(url=Url,
    payload=form_data,
    method=urlfetch.POST,
    headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': CHATWORK_API_TOKEN })

  return 'ok'



@app.route('/task/<int:room_id>', methods=['GET','POST'])
#@login_required
def task(room_id):
  Url="https://api.chatwork.com/v1/rooms/%s/tasks" % room_id
  form_fields = {
   'body': "no task title",
   'to_ids': 1049263 
  }

  if request.method == 'GET':
    form_fields['body'] = request.args.get("body").encode('utf-8')
    dt = datetime.datetime.strptime( request.args.get('expire') )
    form_fields['limit'] = int( time.mktime( dt.timetuple() ) )  
    form_fields['to_ids'] = request.args.get('to_ids').encode('utf-8')

  if request.method == 'POST':
    if request.form.has_key('expire'): 
      dt = dateutil.parser.parse( request.form['expire'] )
      form_fields['limit'] = int( time.mktime( dt.timetuple() ) ) 
    
    form_fields['body'] = request.form['body'].encode('utf-8') if request.form.has_key('body') else null
    form_fields['to_ids'] = request.form['to_ids'] if request.form.has_key('to_ids') else null

  form_data = urllib.urlencode( form_fields )
  urlfetch.fetch(url=Url,
    payload=form_data,
    method=urlfetch.POST,
    headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': CHATWORK_API_TOKEN})

  return 'ok'


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
