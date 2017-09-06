// https://github.com/jeromeetienne/virtualjoystick.js/
function MyJoystick(joystick, updateFrequency) {
    this.containerId = joystick + "-container";
    this.container = document.getElementById(this.containerId);
    this.horizontialOffset = $(this.container).width() / 2;
    this.verticalOffset = 200;
    this.virtualJoystick = new VirtualJoystick({
        container: this.container,
        mouseSupport: true,

        // stationaryBase: true,
        // baseX: this.horizontialOffset,
        // baseY: this.verticalOffset,

        limitStickTravel: true,
        stickRadius: 100
    });
    this.updateFunc = function() {
        // positive = right, negative = left
        var x = this.virtualJoystick.deltaX();
        // positive = down, negative = up
        var y = this.virtualJoystick.deltaY();
        // data to pass on to python server
        var data = {
            'x': x,
            'y': y
        };
        console.log(data, joystick, this.containerId, this.container);
        socket.emit(joystick, data);
    };
    this.updateFunc();
}

$(document).ready(function() {
    // console.log("touchscreen is", VirtualJoystick.touchScreenAvailable() ? "available" : "not available");
    createJoysticks();
});

function createJoysticks() {
    var joysticks = {
        // drive: new MyJoystick("joystick-drive"),
        camera: new MyJoystick("joystick-camera")
    };
    console.log(joysticks);
}

// joystick.addEventListener('touchStart', function(){
//     console.log('down')
// })
// joystick.addEventListener('touchEnd', function(){
//     console.log('up')
// })
//
// setInterval(function(){
//     var outputEl = document.getElementById('result');
//     outputEl.innerHTML	= '<b>Result:</b> '
//         + ' dx:'+joystick.deltaX()
//         + ' dy:'+joystick.deltaY()
//         + (joystick.right()	? ' right'	: '')
//         + (joystick.up()	? ' up'		: '')
//         + (joystick.left()	? ' left'	: '')
//         + (joystick.down()	? ' down' 	: '')
// }, 1/30 * 1000);
