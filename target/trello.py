import os,sys
import time,datetime

from main import app
from config import *

@app.route('/trello/post',methods=['GET','POST'])
def trello_post():
  return 'trello post ';



#https://trello.com/1/members/me/boards?fields=name
