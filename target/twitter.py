import os,sys
import time,datetime

from main import app
from config import *


@app.route('/twtter/post',methods=['GET','POST'])
def twitter_post():
  return 'twitter post  hogehoge';

