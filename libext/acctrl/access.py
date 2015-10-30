#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    flaskext.appengine
    ------------------

    Adds basic App Engine support for Flask.

    :copyright: (c) 2011 by tnakaura.
    :license: BSD, see LICENSE for more details.
"""
import json
from pprint import pprint
from functools import wraps
from google.appengine.api import users
from werkzeug.exceptions import (
    NotFound, Unauthorized, Forbidden,
)
from flask import (
    request, redirect,
)
from ipaddr.ipaddr import *

def whitelist_checked(lists):
  def wrapper(func):
    @wraps(func)
    def wrapped(*args, **kwargs ):
      tip = IPAddress(request.remote_addr)
      for item in lists :
        network = IPNetwork(item)
        if tip in network :
          return func( *args, **kwargs ) 
    
      raise Forbidden()

    return wrapped
  return wrapper 


