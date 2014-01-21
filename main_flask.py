""" main.py is the top level script.

Return "Hello World" at the root URL.
"""

import os
import sys
import cgi

# sys.path includes 'server/lib' due to appengine_config.py
from flask import Flask
from flask import request, render_template
app = Flask(__name__.split('.')[0])


@app.route('/')
# @app.route('/<name>')
def hello(name=None):

    def get(self):
        pass

    """ Return hello template at application root URL."""
    return render_template('index.html', name=name)

@app.route('/thanks', methods=['GET', 'POST'])
@app.route('/thanks/<name>', methods=['GET', 'POST'])
def thanks(name=None):
    """Return Thank You page after signup"""
    name = request.get('list')
    return render_template('thanks.html', name=name)
    
    # template = JINJA_ENVIRONMENT.get_template('thanks.html')
    # self.response.write(template.render(template_values))
    # return render_template('thanks.html', name=name)