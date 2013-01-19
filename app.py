#!/usr/bin/python

import os
from flask import Flask, render_template, redirect, url_for
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


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = bool(os.environ.get('DEBUG', True))
    app.run(host='0.0.0.0', port=port, debug=debug)
