
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
