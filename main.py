# -*- coding: utf-8 -*-

import os,sys
import time,datetime
import urllib

try:
  import dateutil.parser
except:
  sys.exit ( 'Error: dateutils module not installed' )

from urlparse import urlparse
from google.appengine.api import users, ndb, urlfetch
from flask import Flask, request, Response

from flaskext.appengine import(
  AppEngine, login_required
)

import jinja2
jn2 = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

gae = AppEngine(app)

from target.general import *
from target.trello import *
from target.slack import *
from target.pushover import *
from target.chatwork import *
from target.twitter import * 
from target.facebook import *

@app.route('/')
@login_required
def hello():
    """Return a friendly HTTP greeting."""
    return 'ok'

@app.route('/stats')
@login_required
def stats():
    return 'ok'

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404
