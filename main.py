""" main.py is the top level script.
"""

import os
import sys
import cgi

import urllib

import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import request, render_template
app = Flask(__name__.split('.')[0])

# from jinja2 import Environment, PackageLoader
# env = Environment(loader=PackageLoader('verplichterekentoets', 'templates'))

def email_key(email_name='DEFAULT_NAME'):
    return ndb.Key('EmailDatabase', email_name)

class EmailDatabase(ndb.Model):
    email_address = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)

@app.route('/')
@app.route('/<name>')
def main(name=None):
    return render_template('welcome.html', name=name)

@app.route('/thanks', methods=['POST'])
@app.route('/thanks/<name>', methods=['POST'])
def thanks(name=None, email='unknown'):
    """Return Thank You page after signup"""

    email = EmailDatabase(parent=email_key('EmailDatabase'))
    email.name = request.form['list']
    email.email_address = request.form['email_address']
    print "email: ", email.email_address
    email.put()
    role = name
    return render_template('thanks.html', name=email.name, email=email.email_address)

@app.route('/overons')
@app.route('/overons/<name>')
def about(name=None, email='unknown'):
    return render_template('overons.html')
