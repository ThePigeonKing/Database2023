.PHONY: build clean

all: clean build

clean:
	- rm -f pointer nopointer

build: pointer nopointer

pointer: pointer.c
	gcc pointer.c -o pointer

nopointer: nopointer.c
	gcc nopointer.c -o nopointer

