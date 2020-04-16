"""
Command Center
~~~~~~~~~~~
Setting up everything to run portfolio and other things
~~~~~~~~
author: Duylam Nguyen-Ngo
date of creation: 16.04.2020
"""

from flask import Flask, render_template, request, redirect, session, url_for
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return r.text


if __name__ == '__main__':
	port = int(os.environ.get('PORT', 8000))
	app.run(host='0.0.0.0', port=port,debug=True)