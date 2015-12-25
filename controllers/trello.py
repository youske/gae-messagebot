import os,sys
import time,datetime

from acctrl.access import(
  whitelist_checked
)

from main import app
from config import *

@app.route('/trello/post',methods=['GET','POST'])
@whitelist_checked( REMOTE_WHITELIST )
def trello_post():
  return 'trello post ';



#https://trello.com/1/members/me/boards?fields=name
