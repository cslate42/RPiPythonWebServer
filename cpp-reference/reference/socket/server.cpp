// Server side C/C++ program to demonstrate Socket programming
#include "server.h"

// #ifdef __cplusplus
// extern "C" {
// #endif

class SocketServer {
public:
    SocketServer();
    int readMsg();
    char* getMsg();
    int sendMsg(char *msg);
private:
    char buffer[SOCKET_BUFFER_SIZE];
    // ???
    struct sockaddr_in servAddr;
    // ???
    int sockFd;
    // socket file descripter referencing sockFd http://man7.org/linux/man-pages/man2/accept.2.html
    int socketFd;
    // ???
    int enable;
    void __createSocket();
    void __bindSocketToPort();
};

SocketServer::SocketServer():
    enable(1)
{
    __createSocket();
    __bindSocketToPort();
    // start accepting msgs
    socklen_t addrlen = (socklen_t) sizeof(this->servAddr);
    this->socketFd = accept(
        this->sockFd,
        (struct sockaddr *) &(this->servAddr),
        &addrlen
    );
    if ( this->socketFd < 0 ) { error("accept"); }
}

void SocketServer::__createSocket() {
    // Creating socket file descriptor
    this->sockFd = socket(AF_INET, SOCK_STREAM, 0);
    if ( this->sockFd == 0) { error("socket() failed"); }
}

void SocketServer::__bindSocketToPort() {
    // Forcefully attaching socket to the port 8080
    if ( setsockopt(
            this->sockFd,
            SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT,
            &this->enable, sizeof(this->enable)
        ) < 0
    ) { error("setsockopt(SO_REUSEADDR) failed"); }

    bzero((char *) &(this->servAddr), sizeof(this->servAddr));
    this->servAddr.sin_family = AF_INET;
    this->servAddr.sin_addr.s_addr = INADDR_ANY;
    this->servAddr.sin_port = htons( SOCKET_PORT );

    printf("Before BIND\n");
    if ( bind(
        this->sockFd,
        (struct sockaddr *) &(this->servAddr),
        sizeof(this->servAddr)
    ) < 0)
    { error("ERROR on binding"); }

    printf("BEFORE LISTEN\n");
    if (listen(this->sockFd, 3) < 0) { error("listen"); }
}

///
/// SocketServer::read()
///
/// returns -1 on failure and bytes read on success
///

int SocketServer::readMsg() {
    return read(this->socketFd, this->buffer, SOCKET_BUFFER_SIZE);
}

char* SocketServer::getMsg() {
    readMsg();
    return this->buffer;
}

///
/// SocketServer::send
///
/// char *msg the msg buffer
/// returns -1 on failure or number of bytes sent
/// TODO ??? add for loop if msg > buffer size??
///
int SocketServer::sendMsg(char *msg) {
    return send(this->socketFd, msg, strlen(msg) , 0);
}

// #ifdef __cplusplus
// }
// #endif

int main(int argc, char const *argv[])
{
    SocketServer s = SocketServer();
    printf("BUFFER: %s\n", s.getMsg());
    char msg[] = "server send";
    printf("SENDING: %d\n", s.sendMsg(&msg[0]));
    printf("FINAL:%s\n", s.getMsg());
    printf("DONE WITH main\n");
}
