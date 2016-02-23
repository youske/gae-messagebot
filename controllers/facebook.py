#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys,time,datetime

from acctrl.access import(
  whitelist_checked
)

from main import app
from config import *

@app.route('/facebook/post',methods=['GET','POST'])
@whitelist_checked( REMOTE_WHITELIST )
def facebook_post():
  return 'facebook post  hogehoge';

