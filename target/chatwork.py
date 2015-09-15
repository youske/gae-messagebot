#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import urllib
import time,datetime
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
CHATWORK_API_TOKEN = chatwork['apikey']

@app.route('/chatwork/message/<int:room_id>', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def message(room_id):
  Url="https://api.chatwork.com/v1/rooms/%d/messages" % room_id
  form_fields = {
    "body": "no message body"
  }

  if request.method == 'POST':
    form_fields['body'] = request.form['body'].encode('utf-8')
 
  form_data = urllib.urlencode(form_fields)
  result = urlfetch.fetch(url=Url,
    payload=form_data,
    method=urlfetch.POST,
    headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': CHATWORK_API_TOKEN })

  return 'ok'

@app.route('/chatwork/task/<int:room_id>', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def task(room_id):
  Url="https://api.chatwork.com/v1/rooms/%s/tasks" % room_id
  form_fields = {
   'body': "no task title",
   'to_ids': 1049263 
  }

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

