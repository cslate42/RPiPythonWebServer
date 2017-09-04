from flask import render_template

import myGlobals
import myThreading

@myGlobals.app.route('/')
@myGlobals.app.route('/dashboard')
def index():
    myThreading.prepareThreads()
    return render_template('index.html')
