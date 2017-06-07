#!/usr/bin/python
activate_this = '/var/www/grand-bargain-monitoring/pyenv/bin/activate_this.py'
exec(open(activate_this).read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/grand-bargain-monitoring/")
sys.path.insert(0,"/var/www/grand-bargain-monitoring/src/")

from src.app import app as application
application.secret_key = 'Add your secret key'
