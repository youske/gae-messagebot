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

def whitelist_checked(lists):
  def wrapper(func):
    @wraps(func)
    def wrapped(*args, **kwargs ):
      #if remote_addr is None and has_request_context():
      #  remote_addr = request.remote_addr
      # pprint(vars(request))
      if not request.remote_addr in lists :
        raise Forbidden()
      return func( *args, **kwargs ) 
    return wrapped
  return wrapper 


