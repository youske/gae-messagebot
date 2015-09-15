import os,sys
import time,datetime

from main import app
from config import *

@app.route('/slack/post',methods=['GET','POST'])
def slack_post():
  return 'slack post  hogehoge';

