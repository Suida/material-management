# -*- coding: utf-8 -*-
from . import app
from flask import redirect, render_template, request, g
from flask_bootstrap import Bootstrap


bootstrap = Bootstrap(app)


@app.route('/')
@app.route('/index')
def index(name=None):
    return 'hello'
