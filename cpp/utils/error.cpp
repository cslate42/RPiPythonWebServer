#include "error.h"

void myError(const char *msg)
{
    perror(msg);
    exit(EXIT_FAILURE);
}

class HardwareException: public std::exception {
public:
    HardwareException(const char* msg="General Hardware Exception"):
        msg_(msg) {}
    const char* getMsg() { return msg_; }
private:
    const char *msg_;
};
