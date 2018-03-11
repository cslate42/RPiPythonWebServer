/**
 * general use functions
**/


var NAMESPACE = '/socketio';
var sio = io.connect('http://' + document.domain + ':' + location.port + NAMESPACE);


/**
 * parse url string and return url without path
**/
function genGetHostname(url) {
    var m = url.match(/^http:\/\/[^/]+/);
    return m ? m[0] : null;
}

/**
 *
 */
function addTrailingSlash(url) {
    if (url.substr(-1) !== '/') url += '/';
    return url;
}
