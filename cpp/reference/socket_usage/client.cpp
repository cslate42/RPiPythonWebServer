#include "socket.h"

#include <cstdlib>

int main(int argc, char const *argv[])
{
    printf("Start of main\n");
    SocketClient s = SocketClient();
    // printf("\nsetup\n");
    // s.setup();
    // printf("BUFFER: %s\n", s.getMsg());

    char c = true;
    while(c)
    {
        char buffer[1024];
        printf("Option 0=exit 1=get 2=send 3=write: ");
        fgets(buffer, 1024, stdin);

        switch( atoi(buffer) )
        {
            case 0:
                c = false;
                break;
            case 1:
                printf("Getting input...\n");
                printf("Msg: %d => %s\n", s.readMsg(), s.getBuffer());
                break;
            case 2:
                printf("Msg to send: ");
                fgets(buffer, 1024, stdin);
                printf("Sending %d\n", s.sendMsg(&buffer[0]));
            case 3:
                printf("Msg to send: ");
                fgets(buffer, 1024, stdin);
                printf("Sending %d\n", s.writeMsg(&buffer[0]));
        }
    }
    s.destroy();
}
