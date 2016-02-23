#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pushbullet.com message service
#  url 
#  method post 
#  post params 
#    subject
#    body

import os,sys,time,datetime
import urllib
import dateutil.parser

from urlparse import urlparse
from google.appengine.api import (
  users, urlfetch, taskqueue
)
from flask import(
 Flask, request, Response, url_for
) 
from flaskext.appengine import(
  AppEngine, login_required
)
from acctrl.access import(
  whitelist_checked
)

from main import app
from config import *


PUSHBULLET_USER_KEY=pushbullet['user']
PUSHBULLET_API_TOKEN=pushbullet['apikey']
PUSHBULLET_API_URL='https://api.pushbullet.com/1/messages.json'


@app.route('/pushbullet/message', methods=['POST'])
@whitelist_checked( REMOTE_WHITELIST )
def pushover_message():

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
  try:
    result = urlfetch.fetch(url=PUSHOVER_API_URL,
      payload=form_data,
      method=urlfetch.POST,
      headers={'Content-Type': 'application/x-www-form-urlencoded'})
  except:
    pd = {
      'subject': form_fields['title'],
      'body': form_fields['message']
    } 
    taskqueue.Task( url=url_for('pushover_retry_message'), params=pd ).add( 'request-retry' )
 
  return 'ok'

@app.route('/pushbullet/retry_message',methods=['GET','POST'])
def pushbullet_retry_message():

  form_fields = {
    "user": PUSHOVER_USER_KEY,
    "token": PUSHOVER_API_TOKEN,
    "device": 'all',
    "title": 'no title',
    "message" : 'no message'
  }

  if request.method == 'POST':
    form_fields['title'] = request.form['subject'].encode('utf-8')
    form_fields['message'] = request.form['body'].encode('utf-8')

  form_data = urllib.urlencode(form_fields)
  try:
    result = urlfetch.fetch(url=PUSHOVER_API_URL,
      payload=form_data,
      method=urlfetch.POST,
      headers={'Content-Type': 'application/x-www-form-urlencoded'})
  except:
    print 'error taskqueue %s ' % form_fields['title']
  
  return 'ok'

@app.route('/pushover/image',methods=['GET'])
def pushbullet_image():
  taskqueue.add( queue_name='request-retry', url='/pushover/test_return', params={'key':'hoge'} )
  return 'ok'


@app.route('/pushover/test_return',methods=['GET','POST'])
def pushbullet_test_return():
  print 'ok'
  #print request.get('key')
  return 'ok'
  
@app.route('/pushover/test',methods=['GET'])
def pushbullet_test():
  taskqueue.add( queue_name='request-retry', url='/pushover/test_return', params={'key':'hoge'} )
  return 'ok'

A
A
A
A
A
A
A
A
A
A
A
A
A

