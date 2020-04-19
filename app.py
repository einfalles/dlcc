"""
Command Center
~~~~~~~~~~~
Setting up everything to run portfolio and other things
~~~~~~~~
author: Duylam Nguyen-Ngo
date of creation: 16.04.2020
"""

from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import requests
import os
from flask_frozen import Freezer
from flask_script import Manager
from flask_assets import Environment, Bundle, ManageAssets
# import utils
template_dir = os.path.abspath('./app/templates')
static_dir = os.path.abspath('./app/static')
app = Flask(__name__, template_folder=template_dir,static_folder=static_dir)
freezer = Freezer(app)
manager = Manager(app)
assets = Environment(app)
manager = Manager(app)


css_files = ['app.fb0c6e1c.css']
css_all = Bundle(*['css/' + file for file in css_files], output='gen/css_all.css')
assets.register("css_all", css_all)

js_files = ['app.06b766ee.js','app.06b766ee.js.map','chunk-vendors.61405a0c.js','chunk-vendors.61405a0c.js.map']
js_all = Bundle(*['js/' + file for file in js_files], filters='rjsmin', output='gen/js_all.js')
assets.register("js_all", js_all)


manager.add_command("assets", ManageAssets(assets))

@app.route('/')
def index():
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return r.text+"do do do doooo dodo"

@app.route('/vue_demo')
def vue_demo():
    return render_template('index.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8000))
    freezer.freeze()
    app.run(host='0.0.0.0',port=port,debug=True)