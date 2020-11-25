CC=gcc
CFLAGS=-I.

plaync: plaync.o
	$(CC) -o plaync plaync.o -lncurses 
