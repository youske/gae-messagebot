#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os,sys
import time,datetime
import urllib
import dateutil.parser

from urlparse import urlparse
from google.appengine.api import (
  users, urlfetch, taskqueue
)
from flask import (
  Flask,request,Response,url_for
) 
from flaskext.appengine import(
  AppEngine, login_required
)
from acctrl.access import(
  whitelist_checked
)

from main import app
 
from config import *

CHATWORK_API_TOKEN = chatwork['apikey']
CHATWORK_API_MESSAGE = 'https://api.chatwork.com/v1/rooms/%s/messages'
CHATWORK_API_TASK = 'https://api.chatwork.com/v1/rooms/%s/tasks'


@app.route('/chatwork/message/<string:room_id>', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def chatwork_message(room_id):
  opt = { 'room_id':room_id, 'retry': False } 
  return str( __fetch_chatwork_message( opt ) )


@app.route('/chatwork/retry_message/<string:room_id>', methods=['POST'])
def chatwork_retry_message(room_id):
  opt = { 'room_id':room_id, 'retry': False } 
  return str( __fetch_chatwork_message( opt ) )


def __fetch_chatwork_message( options ):
  ret = False
  room_id = options['room_id']

  form_fields = {
    "body": "no body"
  }

  if request.method == 'POST':
    form_fields['body'] = request.form['body'].encode('utf-8')
 
  form_data = urllib.urlencode(form_fields)
  try:
    fetchUrl = CHATWORK_API_MESSAGE % room_id 
    result = urlfetch.fetch( url=fetchUrl,
      payload=form_data,
      method=urlfetch.POST,
      headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': CHATWORK_API_TOKEN })
    ret = True
 
  except:
    print 'error : room_id=%s' % room_id
    if options['retry'] == True:
      pd = { 'body': form_fields['body'] }
      retryUrl = "/chatwork/retry_message/%s" % room_id
      taskqueue.Task( url=retryUrl, params=pd ).add( 'request-retry' )

  return ret





@app.route('/chatwork/task/<string:room_id>', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def chatwork_task(room_id):
  opt = { 'room_id': room_id, 'retry': True }
  return str( __fetch_chatwork_task( opt ) )

@app.route('/chatwork/retry_task/<string:room_id>', methods=['POST'])
def chatwork_retry_task(room_id):
  opt = { 'room_id': room_id, 'retry': False }
  return str( __fetch_chatwork_task( opt ) )


def __fetch_chatwork_task( options ):
  ret = False
  room_id = options['room_id']

  form_fields = {
   'body': "no task title",
   'to_ids': 1049263 
  }

  if request.method == 'POST':
    if request.form.has_key('expire'): 
      dt = dateutil.parser.parse( request.form['expire'] )
      form_fields['limit'] = int( time.mktime( dt.timetuple() ) ) 
    
    if request.form.has_key('body'):
      form_fields['body'] = request.form['body'].encode('utf-8') 
    
    if request.form.has_key('to_ids'):
      form_fields['to_ids'] = request.form['to_ids'] 

  form_data = urllib.urlencode( form_fields )
  try:
    urlfetch.fetch(url=CHATWORK_API_TASK % room_id,
      payload=form_data,
      method=urlfetch.POST,
      headers={'Content-Type': 'application/x-www-form-urlencoded', 'X-ChatWorkToken': CHATWORK_API_TOKEN})
    ret = True

  except:
    print 'error : room_id=%s' % room_id
    if options['retry'] == True :
      retryUrl = "/chatwork/retry_message/%s" % room_id
      pd = { 'body': form_fields['body'], 'to_ids': form_fields['to_ids'], 'limit': form_fields['limit'] }
      taskqueue.Task( url=retryUrl, params=pd ).add( 'request-retry' )
 
  return ret

