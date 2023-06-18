.PHONY: diff build clean

all: clean build

clean:
	- rm -f *.s

build: const.s noconst.s

const.s: const.c
	gcc -S const.c -o const.s

noconst.s: noconst.c
	gcc -S noconst.c -o noconst.s

diff:
	diff --color const.s noconst.s || true
