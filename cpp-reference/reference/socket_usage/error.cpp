#include "error.h"

void myError(const char *msg)
{
    perror(msg);
    exit(EXIT_FAILURE);
}
