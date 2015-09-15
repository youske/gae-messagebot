#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pushover.net message service
#  url 
#  method post 
#  post params 
#    subject
#    body

import os,sys
import time,datetime
import urllib
import dateutil.parser

from urlparse import urlparse
from google.appengine.api import users, urlfetch
from flask import Flask,request,Response
 
from flaskext.appengine import(
  AppEngine, login_required
)

from acctrl.access import(
  whitelist_checked
)

from main import app
from config import *

PUSHOVER_USER_KEY=pushover['user']
PUSHOVER_API_TOKEN=pushover['apikey']

@app.route('/pushover/message', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def pushover_message():
  Url="https://api.pushover.net/1/messages.json"
  form_fields = {
    "user": PUSHOVER_USER_KEY,
    "token": PUSHOVER_API_TOKEN,
    "device": 'all',
    "title": "no title",
    "message" : "no message"
  }

  if request.method == 'POST':
    form_fields['title'] = request.form['subject'].encode('utf-8')
    form_fields['message'] = request.form['body'].encode('utf-8')
 
  form_data = urllib.urlencode(form_fields)
  result = urlfetch.fetch(url=Url,
    payload=form_data,
    method=urlfetch.POST,
    headers={'Content-Type': 'application/x-www-form-urlencoded'})

  return 'ok'


