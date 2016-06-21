from flask import render_template

import myGlobals
import myThreading

import lib.myGpio as myGpio

@myGlobals.sio.on('update-controls', namespace='/socketio')
def updateControls(sid, message):
    myGlobals.sio.emit('update-controls-results', {'message': message, 'sid': sid}, namespace='/socketio')

    keysPressed = message['keysPressed'] if message['keysPressed'] else []
    print(keysPressed, message)
    # ------------------CHASSIS CONTROLS---------------------------------
    if( keysPressed['ArrowUp'] and keysPressed['ArrowLeft'] ):
        chassisForwardLeft()
    elif( keysPressed['ArrowUp'] and keysPressed['ArrowRight'] ):
        chassisForwardRight()
    elif( keysPressed['ArrowDown'] and keysPressed['ArrowLeft'] ):
        chassisBackwardLeft()
    elif( keysPressed['ArrowDown'] and keysPressed['ArrowRight'] ):
        chassisBackwardRight()
    elif ( (keysPressed['ArrowUp'] and keysPressed['ArrowDown']) or (keysPressed['ArrowLeft'] and keysPressed['ArrowRight']) ):
        chassisStop()
    elif ( keysPressed['ArrowUp'] ):
        chassisForward()
    elif ( keysPressed['ArrowRight'] ):
        chassisRight()
    elif ( keysPressed['ArrowDown'] ):
        chassisBackward()
    elif ( keysPressed['ArrowLeft'] ):
        chassisLeft()
    else:
        chassisStop()

    # -----------------------------LED TEST----------------------------
    if( keysPressed['a'] ):
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
