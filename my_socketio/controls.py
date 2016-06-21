from flask import render_template

import myGlobals
import myThreading

import lib.myGpio as myGpio

@myGlobals.sio.on('update-controls', namespace='/socketio')
def updateControls(sid, message):
    myGlobals.sio.emit('update-controls-results', {'message': message, 'sid': sid}, namespace='/socketio')
    keysPressed = message['keysPressed'] if message['keysPressed'] else {}

    print(keysPressed)
    # ---------------------------------------CHASSIS CONTROLS--------------------------------------------------------
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
        myGpio.pwmPinsUpdate(myGpio.MOTOR_L_F, 100, 25)
    elif( keysPressed.get('s') ):
        myGpio.pwmPinsUpdate(myGpio.MOTOR_L_F, 100, 50)
    elif( keysPressed.get('d') ):
        myGpio.pwmPinsUpdate(myGpio.MOTOR_L_F, 100, 75)
    elif( keysPressed.get('f') ):
        myGpio.pwmPinsUpdate(myGpio.MOTOR_L_F, 100, 100)
    elif( keysPressed.get('j') ):
        myGpio.pwmStop(myGpio.MOTOR_L_F)
    # if( keysPressed.get('a') ):
    #     myGpio.write(3, 1)
    # else:
    #     myGpio.write(3, 0)

    return


def chassisForwardLeft():
    # TODO pwm
    myGpio.write(myGpio.MOTOR_L_B, 0)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 0)

def chassisForwardRight():
    # TODO pwm
    myGpio.write(myGpio.MOTOR_L_B, 1)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 1)

def chassisBackwardLeft():
    #TODO pwm
    myGpio.write(myGpio.MOTOR_L_B, 1)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 1)

def chassisBackwardRight():
    #TODO pwm
    myGpio.write(myGpio.MOTOR_L_B, 1)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 1)

def chassisForward():
    myGpio.write(myGpio.MOTOR_L_B, 0)
    myGpio.write(myGpio.MOTOR_L_F, 1)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 1)

def chassisRight():
    myGpio.write(myGpio.MOTOR_L_B, 0)
    myGpio.write(myGpio.MOTOR_L_F, 1)
    myGpio.write(myGpio.MOTOR_R_B, 1)
    myGpio.write(myGpio.MOTOR_R_F, 0)

def chassisBackward():
    myGpio.write(myGpio.MOTOR_L_B, 1)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 1)
    myGpio.write(myGpio.MOTOR_R_F, 0)

def chassisLeft():
    myGpio.write(myGpio.MOTOR_L_B, 1)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 1)

def chassisStop():
    myGpio.write(myGpio.MOTOR_L_B, 0)
    myGpio.write(myGpio.MOTOR_L_F, 0)
    myGpio.write(myGpio.MOTOR_R_B, 0)
    myGpio.write(myGpio.MOTOR_R_F, 0)

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
