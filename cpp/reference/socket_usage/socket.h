// see https://www.geeksforgeeks.org/socket-programming-cc/

#include <stdio.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>
#include <unistd.h>

#ifndef SOCKET_H_
    #define SOCKET_H_
#include "error.h"
    #define SOCKET_PORT 12345
    #define SOCKET_BUFFER_SIZE 1024

    class Socket
    {
    public:
        char* getBuffer();
        virtual int readMsg();
        char* getMsg();
        virtual int sendMsg(char *msg);
        virtual int writeMsg(char *msg);
        int destroy();
    protected:
        char buffer[SOCKET_BUFFER_SIZE];
        // ???
        struct sockaddr_in servAddr;
        // ???
        int sockFd;
        // ???
        int enable;
        void setup();
    private:
        // Socket() {}; // don't allow instance of object
        void __createSocketFd();
    };

    class SocketServer: public Socket
    {
    public:
        SocketServer();
        int readMsg();
        int sendMsg(char *msg);
        int writeMsg(char *msg);
        int destroy();
    private:
        // socket file descripter referencing sockFd http://man7.org/linux/man-pages/man2/accept.2.html
        int socketFd;
    };

    class SocketClient: public Socket
    {
    public:
        SocketClient();
    };

#endif
