"""
Controls page
"""
import my_pi_server

@my_pi_server.app.route('/')
@my_pi_server.app.route('/controls')
def control():
    """All web based controls"""
    return my_pi_server.render('controls.html')

@my_pi_server.app.route('/joystick-example')
def joystickExample():
    """Test if joystick renders correctly"""
    return my_pi_server.render('joystick-example.html')
