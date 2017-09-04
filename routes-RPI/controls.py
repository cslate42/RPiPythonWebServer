from flask import render_template

import myGlobals
import myThreading

@myGlobals.app.route('/controls')
def control():
    myThreading.prepareThreads()
    return render_template('controls.html')
