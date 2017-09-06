"""
Basic controls
"""
import lib.basic_io as basicIO
import my_pi_server

@my_pi_server.sioServer.on('joystick-camera', namespace='/socketio')
def updateCamera(sid, message):
    basicIO.updateCameraPos(message['x'], message['y'])
    return

@my_pi_server.sioServer.on('update-controls', namespace='/socketio')
def updateControls(sid, message):
    """Listen to user keys then update drive based on that"""
    myGlobals.sio.emit('update-controls-results', {'message': message, 'sid': sid}, namespace='/socketio')
    keysPressed = message['keysPressed'] if message['keysPressed'] else {}

    # print("KEYS PRESSED", keysPressed, "PWM PINS", basicIO.pwmPins)
    # ---------------------------------------OH SHIT BUTTON---------------------------------------------------------
    if keysPressed.get('Escape'):
        basicIO.reset()
    # ---------------------------------------CHASSIS CONTROLS--------------------------------------------------------
    if keysPressed.get('ArrowUp') and keysPressed.get('ArrowLeft'):
        chassisForwardLeft()
    elif keysPressed.get('ArrowUp') and keysPressed.get('ArrowRight'):
        chassisForwardRight()
    elif keysPressed.get('ArrowDown') and keysPressed.get('ArrowLeft'):
        chassisBackwardLeft()
    elif keysPressed.get('ArrowDown') and keysPressed.get('ArrowRight'):
        chassisBackwardRight()
    elif (keysPressed.get('ArrowUp') and keysPressed.get('ArrowDown')) \
        or (keysPressed.get('ArrowLeft') and keysPressed.get('ArrowRight')):
        chassisStop()
    elif keysPressed.get('ArrowUp'):
        chassisForward()
    elif keysPressed.get('ArrowRight'):
        chassisRight()
    elif keysPressed.get('ArrowDown'):
        chassisBackward()
    elif keysPressed.get('ArrowLeft'):
        chassisLeft()
    else:
        chassisStop()

    if keysPressed.get('a'):
        basicIO.pwmPinsUpdate(basicIO.PWM_LED, 50, 25)
    elif keysPressed.get('s'):
        basicIO.pwmPinsUpdate(basicIO.PWM_LED, 100, 50)

    # -----------------------------LED TEST----------------------------
    # if( keysPressed.get('a') ):
    #     basicIO.write(3, 1)
    # else:
    #     basicIO.write(3, 0)

    return


def chassisForwardLeft():
    basicIO.write(basicIO.MOTOR_L_B, 0)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 0)

def chassisForwardRight():
    basicIO.write(basicIO.MOTOR_L_B, 1)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 1)

def chassisBackwardLeft():
    basicIO.write(basicIO.MOTOR_L_B, 1)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 1)

def chassisBackwardRight():
    basicIO.write(basicIO.MOTOR_L_B, 1)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 1)

def chassisForward():
    basicIO.write(basicIO.MOTOR_L_B, 0)
    basicIO.write(basicIO.MOTOR_L_F, 1)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 1)

def chassisRight():
    basicIO.write(basicIO.MOTOR_L_B, 0)
    basicIO.write(basicIO.MOTOR_L_F, 1)
    basicIO.write(basicIO.MOTOR_R_B, 1)
    basicIO.write(basicIO.MOTOR_R_F, 0)

def chassisBackward():
    basicIO.write(basicIO.MOTOR_L_B, 1)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 1)
    basicIO.write(basicIO.MOTOR_R_F, 0)

def chassisLeft():
    basicIO.write(basicIO.MOTOR_L_B, 1)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 1)

def chassisStop():
    basicIO.write(basicIO.MOTOR_L_B, 0)
    basicIO.write(basicIO.MOTOR_L_F, 0)
    basicIO.write(basicIO.MOTOR_R_B, 0)
    basicIO.write(basicIO.MOTOR_R_F, 0)


# # @myGlobals.app.route('/controls')
# # def control():
# #     myThreading.prepareThreads()
# #     return render_template('controls.html')
#
# # @sio.on('update-controls', namespace='/socketio')
# # def test_message(sid, message):
# #     global sio
# #     sio.emit('update-controls-results', {'data': message}, room=sid, namespace='/socketio')
# #
# # @sio.on('my broadcast event', namespace='/socketio')
# # def test_broadcast_message(sid, message):
# #     sio.emit('my response', {'data': message['data']}, namespace='/socketio')
