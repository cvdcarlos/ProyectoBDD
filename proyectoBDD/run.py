#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,os

reload(sys)  
sys.setdefaultencoding('utf8')

from app import app
app.secret_key = os.urandom(12)
app.run(debug=True)
