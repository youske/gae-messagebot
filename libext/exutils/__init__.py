#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

class __LINE__(object):
  def __repr__(self):
    try:
      raise Exception
    except:
      return str(sys.exc_info()[2].tb_frame.f_back.f_lineno)

__line__ = __LINE__()


