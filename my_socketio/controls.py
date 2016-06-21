from flask import render_template

import myGlobals
import myThreading

import lib.myGpio as myGpio

@myGlobals.sio.on('update-controls', namespace='/socketio')
def updateControls(sid, message):
    myGlobals.sio.emit('update-controls-results', {'message': message, 'sid': sid}, namespace='/socketio')
    myGpio.write(myGpio.MOTOR_L_F, True)

# @myGlobals.app.route('/controls')
# def control():
#     myThreading.prepareThreads()
#     return render_template('controls.html')

# @sio.on('update-controls', namespace='/socketio')
# def test_message(sid, message):
#     global sio
#     sio.emit('update-controls-results', {'data': message}, room=sid, namespace='/socketio')
#
# @sio.on('my broadcast event', namespace='/socketio')
# def test_broadcast_message(sid, message):
#     sio.emit('my response', {'data': message['data']}, namespace='/socketio')
