from flask import render_template

import myGlobals
import myThreading

import lib.myGpio as myGpio

@myGlobals.sio.on('update-controls', namespace='/socketio')
def updateControls(sid, message):
    myGlobals.sio.emit('update-controls-results', {'message': message, 'sid': sid}, namespace='/socketio')

    keysPressed = message['keysPressed'] if message['keysPressed'] else {}
    print(keysPressed, message, message['keysPressed'], message.get('keysPressed'))
    # ------------------CHASSIS CONTROLS---------------------------------
    if( keysPressed.get('ArrowUp') and keysPressed.get('ArrowLeft') ):
        chassisForwardLeft()
    elif( keysPressed.get('ArrowUp') and keysPressed.get('ArrowRight') ):
        chassisForwardRight()
    elif( keysPressed.get('ArrowDown') and keysPressed.get('ArrowLeft') ):
        chassisBackwardLeft()
    elif( keysPressed.get('ArrowDown') and keysPressed.get('ArrowRight') ):
        chassisBackwardRight()
    elif ( (keysPressed.get('ArrowUp') and keysPressed.get('ArrowDown'))
            or (keysPressed.get('ArrowLeft') and keysPressed.get('ArrowRight')) ):
        chassisStop()
    elif ( keysPressed.get('ArrowUp') ):
        chassisForward()
    elif ( keysPressed.get('ArrowRight') ):
        chassisRight()
    elif ( keysPressed.get('ArrowDown') ):
        chassisBackward()
    elif ( keysPressed.get('ArrowLeft') ):
        chassisLeft()
    else:
        chassisStop()

    # -----------------------------LED TEST----------------------------
    if( keysPressed.get('a') ):
        myGPIO.write(3, 1)
    else:
        myGPIO.write(3, 0)

    return


def chassisForwardLeft():
    # TODO pwm
    myGPIO.write(myGPIO.MOTOR_L_B, 0)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 0)

def chassisForwardRight():
    # TODO pwm
    myGPIO.write(myGPIO.MOTOR_L_B, 1)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 1)

def chassisBackwardLeft():
    #TODO pwm
    myGPIO.write(myGPIO.MOTOR_L_B, 1)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 1)

def chassisBackwardRight():
    #TODO pwm
    myGPIO.write(myGPIO.MOTOR_L_B, 1)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 1)

def chassisForward():
    myGPIO.write(myGPIO.MOTOR_L_B, 0)
    myGPIO.write(myGPIO.MOTOR_L_F, 1)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 1)

def chassisRight():
    myGPIO.write(myGPIO.MOTOR_L_B, 0)
    myGPIO.write(myGPIO.MOTOR_L_F, 1)
    myGPIO.write(myGPIO.MOTOR_R_B, 1)
    myGPIO.write(myGPIO.MOTOR_R_F, 0)

def chassisBackward():
    myGPIO.write(myGPIO.MOTOR_L_B, 1)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 1)
    myGPIO.write(myGPIO.MOTOR_R_F, 0)

def chassisLeft():
    myGPIO.write(myGPIO.MOTOR_L_B, 1)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 1)

def chassisStop():
    myGPIO.write(myGPIO.MOTOR_L_B, 0)
    myGPIO.write(myGPIO.MOTOR_L_F, 0)
    myGPIO.write(myGPIO.MOTOR_R_B, 0)
    myGPIO.write(myGPIO.MOTOR_R_F, 0)

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
