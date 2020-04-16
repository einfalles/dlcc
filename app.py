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

app = Flask(__name__)

@app.route('/')
def index():
	return "hello"