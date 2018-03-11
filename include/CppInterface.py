import socket


class CppInterface:
    # @see https://pymotw.com/2/socket/tcp.html
    HOST = 'localhost'
    PORT = 12345
    sock = None

    def initialize(cls):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # addr = socket.getaddrinfo(cls.HOST, cls.PORT)
        # print(addr)
        addr = (cls.HOST, cls.PORT)
        cls.sock.connect(addr)

    def destroy(cls):
        cls.sock.close()

    def send(cls, msg):
        try:
            cls.sock.sendall(msg)
            # TODO look for response and validate msg recieved correctly
            # # Look for the response
            # amount_received = 0
            # amount_expected = len(message)
            # while amount_received < amount_expected:
            #     data = sock.recv(16)
            #     amount_received += len(data)
            #     print >>sys.stderr, 'received "%s"' % data
        except Exception as e:
            print(e)
            raise IOError("Unable to send to socket")

    def read(cls, length=512):
        """
        :param int bytes to read
        """
        data = ''
        try:
            # while True:
            data = cls.sock.recv(length)
        except Exception as e:
            print(e)
            raise IOError("Unable to read socket")
        return data

    def readAll(cls):
        BUFF_SIZE = 4096  # 4 KiB
        data = ''
        while True:
            part = cls.sock.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                # either 0 or end of data
                break
        return data


if __name__ == '__main__':
    cpp = CppInterface()
    cpp.initialize()
    # cpp.send('py')
    for i in range(0, 3):
        print("FORE " + str(i))
        print(cpp.readAll())
