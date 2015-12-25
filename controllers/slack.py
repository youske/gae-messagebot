import os,sys
import time,datetime

from acctrl.access import(
  whitelist_checked
)

from main import app
from config import *

@app.route('/slack/post',methods=['GET','POST'])
@whitelist_checked( REMOTE_WHITELIST )
def slack_post():
  return 'slack post  hogehoge';

