import os,sys
import time,datetime

from acctrl.access import(
  whitelist_checked
)


from main import app
from config import *


@app.route('/twtter/post',methods=['GET','POST'])
@whitelist_checked( REMOTE_WHITELIST )
def twitter_post():
  return 'twitter post  hogehoge';

