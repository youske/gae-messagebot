import os,sys
import time,datetime

from main import app
from config import *

@app.route('/t',methods=['GET','POST'])
def std_post():
  return 'general post  hogehoge';

