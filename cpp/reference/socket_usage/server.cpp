#include "socket.h"


#include <cstdlib>

int main(int argc, char const *argv[])
{
    printf("Start of main\n");
    SocketServer s = SocketServer();
    // printf("\nsetup\n");
    // s.setup();
    while(1)
    {
        char buffer[1024];
        printf("Option 1=get 2=send: ");
        fgets(buffer, 1024, stdin);

        switch( atoi(buffer) )
        {
            case 1:
                printf("Getting input...\n");
                printf("Msg: %d => %s\n", s.readMsg(), s.getBuffer());
                break;
            case 2:
                printf("Msg to send: ");
                fgets(buffer, 1024, stdin);
                printf("Sending %d\n", s.sendMsg(&buffer[0]));
        }
    }
    s.destroy();
}
