from flask import render_template

import myGlobals
import myThreading


class myDemo(object):

    def streamCamera(self):
        return None

    def streamGyroPyGame(self):
        return None

    def dashboard(self):
        """
            Navigation
                Dashboard
                UI
                Schematic
                ???
            Description
        """
        myThreading.prepareThreads()
        return render_template('index.html')

    def ui(self):
        """
            Get basic html controls
                motor movements
                state of photoeye
            Logic is done in socketio
            logs + streams
                stream camera - live feed
                    audio option?
                sonar shit - overlay on camera feed
                gyroscope display angles upon each access + stream pygame
                log i2c inputs - 10 lines of history
        """
        return None

@myGlobals.app.route('/demo')
def asdf():
    d = myDemo()
    return d.dashboard()


@myGlobals.app.route('/')
@myGlobals.app.route('/dashboard')
def index():
    myThreading.prepareThreads()
    return render_template('index.html')
