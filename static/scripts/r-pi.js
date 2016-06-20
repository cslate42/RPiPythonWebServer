// https://github.com/jaredwolff/nodejs-websocket-example
var namespace = '/socketio';
var socket = io.connect('http://' + document.domain + ':' + location.port + namespace);

socket.on('update-controls-results', function (data) {
    console.log("update controls results", data);
});

function emitUpdatedControls(keysPressed) {
    console.log("KEYS PRESSED = ", keysPressed);
    socket.emit('update-controls', { keysPressed: keysPressed });
}

function piRun() {

}

function piStop() {

}
