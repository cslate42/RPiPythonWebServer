
all:
	touch __tmp.o
	g++ utils/socket.cpp -c -o socket.o
	g++ utils/error.cpp -c -o error.o
	g++ webInterface.cpp -c -o webInterface.o
	g++ main.cpp -c -o main.o
	g++ main.o webInterface.o socket.o error.o -o main.out
	rm *.o
	./main.out

server:
	touch asdf.o
	g++ error.cpp -c -o error.o
	g++ socket.cpp -c -o socket.o
	g++ server.cpp -c -o server.o
	g++ socket.o server.o error.o -o server.out
	rm *.o
	./server.out

client:
	touch asdf.o
	rm *.o
	g++ error.cpp -c -o error.o
	g++ socket.cpp -c -o socket.o
	g++ client.cpp -c -o client.o
	g++ socket.o client.o error.o -o client.out
	rm *.o
	./client.out
