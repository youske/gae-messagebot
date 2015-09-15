import os,sys
import time,datetime

from main import app
from config import *

@app.route('/facebook/post',methods=['GET','POST'])
def facebook_post():
  return 'facebook post  hogehoge';

