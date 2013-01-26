#!/usr/bin/python

import os
from flask import Flask, render_template, redirect, url_for, Response
from yaml import load as yamload


app = Flask(__name__)


@app.route('/')
def matthieuhalle():
    # nothing here, go to Margraue
    return redirect(url_for('margraue'))


@app.route('/margraue')
def margraue():
    context = yamload(open('margraue.yaml'))
    return render_template('margraue.html', **context)


@app.route('/margraue/favicon.png')
def icon():
    with open('margraue-icon.png', 'rb') as icon:
        return Response(icon.read(), mimetype='image/png')

@app.route('/humans.txt')
def humans():
    with open('humans.txt') as humanstxt:
        return Response(humanstxt.read(), mimetype='text/plain')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', True))
    app.run(host='0.0.0.0', port=port, debug=debug)
