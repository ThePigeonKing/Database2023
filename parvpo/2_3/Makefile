.PHONY: build clean

all: clean build

clean:
	- rm -f binary/*

build: pointer nopointer pointer_o3 nopointer_o3

pointer: pointer.c
	gcc pointer.c -o binary/pointer

nopointer: nopointer.c
	gcc nopointer.c -o binary/nopointer

pointer_o3: pointer.c
	gcc pointer.c -O3 -o binary/pointer_o3

nopointer_o3: nopointer.c
	gcc nopointer.c -O3 -o binary/nopointer_o3

