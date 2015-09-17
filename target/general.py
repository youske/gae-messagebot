# -*- coding: utf-8 -*-

import os,sys
import time,datetime
import urllib

try:
  import dateutil.parser
except:
  sys.exit ( 'Error: dateutils module not installed' )

from urlparse import urlparse
from google.appengine.api import users, urlfetch
from google.appengine.ext import ndb
from flask import Flask, request, Response

from flaskext.appengine import(
  AppEngine, login_required
)

from acctrl.access import(
  whitelist_checked  
)

from main import app

from config import *
CHATWORK_API_TOKEN = chatwork['apikey']


@app.route('/')
@login_required
@whitelist_checked( REMOTE_WHITELIST )
def hello():
    """Return a friendly HTTP greeting."""
    return 'ok'

@app.route('/view_remote_addr')
def view_remote_addr():
    return request.remote_addr

@app.route('/q')
@whitelist_checked( REMOTE_WHITELIST )
def query():
    #hosts = whitelist.query_host('xx')
    #for hs in hosts : 
    #  return 'ok'
    return request.remote_addr 

@app.route('/t',methods=['GET','POST'])
def std_post():
  return 'general post  hogehoge';


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404


