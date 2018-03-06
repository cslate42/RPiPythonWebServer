// Server side C/C++ program to demonstrate Socket programming
#include "socket.h"

void Socket::setup()
{
    __createSocketFd();
    // ???
    this->enable = 1;
    // ???
    bzero((char *) &(this->servAddr), sizeof(this->servAddr));
    this->servAddr.sin_family = AF_INET;
    this->servAddr.sin_addr.s_addr = INADDR_ANY;
    this->servAddr.sin_port = htons( SOCKET_PORT );
}

void Socket::__createSocketFd() {
    // Creating socket file descriptor
    this->sockFd = socket(AF_INET, SOCK_STREAM, 0);
    if ( this->sockFd < 0) { myError("socket() failed"); }
}

char* Socket::getBuffer() {
    return this->buffer;
}

int Socket::destroy() {
    return close(this->sockFd);
}

int Socket::readMsg() {
    return read(this->sockFd, this->buffer, SOCKET_BUFFER_SIZE);
}

int Socket::sendMsg(char *msg) {
    return send(this->sockFd, msg, strlen(msg) , 0);
}

int Socket::writeMsg(char *msg) {
    return write(this->sockFd, msg, strlen(msg));
}


char* Socket::getMsg() {
    readMsg();
    return this->buffer;
}
//==============================================================================
//              Socket Server
//==============================================================================

SocketServer::SocketServer()
{
    setup();
    // option t rebind port if in use
    if ( setsockopt(
            this->sockFd,
            SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
            &this->enable, sizeof(this->enable)
        ) < 0
    ) { myError("setsockopt(SO_REUSEADDR) failed"); }
    // Forcefully attaching socket to the port
    if ( bind(
        this->sockFd,
        (struct sockaddr *) &(this->servAddr),
        sizeof(this->servAddr)
    ) < 0)
    { myError("myError on binding"); }
    // start listening
    if (listen(this->sockFd, 3) < 0) { myError("listen"); }
    // start accepting msgs
    socklen_t addrlen = (socklen_t) sizeof(this->servAddr);
    this->socketFd = accept(
        this->sockFd,
        (struct sockaddr *) &(this->servAddr),
        &addrlen
    );
    if ( this->socketFd < 0 ) { myError("accept"); }
}

int SocketServer::destroy() {
    if ( close(this->socketFd) != 0 ) { myError("SocketServer destory()"); }
    return Socket::destroy();
}

int SocketServer::readMsg() {
    return read(this->socketFd, this->buffer, SOCKET_BUFFER_SIZE);
}

int SocketServer::sendMsg(char *msg) {
    return send(this->socketFd, msg, strlen(msg) , 0);
}

int SocketServer::writeMsg(char *msg) {
    return write(this->socketFd, msg, strlen(msg));
}

//==============================================================================
//              Socket Client
//==============================================================================

SocketClient::SocketClient()
{
    setup();
    // connect to socket
    if ( connect(
        this->sockFd,
        (struct sockaddr *) &this->servAddr,
        sizeof(this->servAddr)
    ) < 0)
    {
        myError("ERROR connecting");
    }
}
