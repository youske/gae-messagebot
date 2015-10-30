# -*- coding: utf-8 -*-

import os,sys
import time,datetime
import urllib

from ipaddr.ipaddr import *

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

@app.route('/iptest')
@login_required
@whitelist_checked( REMOTE_WHITELIST )
def iptest():
  q0 = IPAddress('66.249.84.127')

  for item in REMOTE_WHITELIST:
     if item == 'localhost' :
        continue
     network = IPNetwork(item)
     if q0 in network :
        return 'hit'

  return 'not'


def test_ipaddr():
  network = IPv4Network('192.168.10.0/28')
  for x in xrange(1, 100):
    if IPv4Address('192.168.10.%d'%x) in network :
      print "%d" % x
