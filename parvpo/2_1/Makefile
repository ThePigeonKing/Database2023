.PHONY:	all	clean	build_binary	build_asm diff_base diff_optimize

all:	clean	build_binary	build_asm

clean:
	- rm	-f	cdecl	cdecl_o3	fastcall	fastcall_o3	stdcall	stdcall_o3
	- rm	asm/*

build_binary:	cdecl	cdecl_o3	fastcall	fastcall_o3	stdcall	stdcall_o3

build_asm:	cdecl_asm	cdecl_o3_asm	fastcall_asm	fastcall_o3_asm	stdcall_asm	stdcall_o3_asm

#	binary
cdecl:	cdecl.c
		gcc	-m32	-g	-o	binary/cdecl	cdecl.c

cdecl_o3:	cdecl.c
		gcc	-m32	-g	-O3	-o	binary/cdecl_o3	cdecl.c

fastcall:	fastcall.c
		gcc	-m32	-g	-o	binary/fastcall	fastcall.c

fastcall_o3:	fastcall.c
		gcc	-m32	-g	-O3	-o	binary/fastcall_o3	fastcall.c

stdcall:	stdcall.c
		gcc	-m32	-g	-o	binary/stdcall	stdcall.c

stdcall_o3:	stdcall.c
		gcc	-m32	-g	-O3	-o	binary/stdcall_o3	stdcall.c

#	asm
cdecl_asm:	cdecl.c
		gcc	-m32 -S -o asm/cdecl.s	cdecl.c

cdecl_o3_asm:	cdecl.c
		gcc	-m32 -S -O3	-o	asm/cdecl_o3.s	cdecl.c

fastcall_asm:	fastcall.c
		gcc	-m32 -S -o	asm/fastcall.s	fastcall.c

fastcall_o3_asm:	fastcall.c
		gcc	-m32 -S -O3	-o	asm/fastcall_o3.s	fastcall.c

stdcall_asm:	stdcall.c
		gcc	-m32 -S	-o	asm/stdcall.s	stdcall.c

stdcall_o3_asm:	stdcall.c
		gcc	-m32 -S -O3	-o	asm/stdcall_o3.s	stdcall.c

# diff
diff_base:
	@printf "<--- CDECL vs FASTCALL --->\n"
	@diff --color asm/cdecl.s asm/fastcall.s || true
	@printf "\n\n <--- CDECL vs STDCALL --->\n"
	@diff --color asm/cdecl.s asm/stdcall.s || true
	@printf "\n\n <--- FASTCALL vs STDCALL --->\n"
	@diff --color asm/fastcall.s asm/stdcall.s || true

diff_optimize:
	@printf "<--- CDECL_O3 vs FASTCALL_O3 --->\n"
	@diff --color asm/cdecl_o3.s asm/fastcall_o3.s || true
	@printf "\n\n <--- CDECL_O3 vs STDCALL_O3 --->\n"
	@diff --color asm/cdecl_o3.s asm/stdcall_o3.s || true
	@printf "\n\n <--- FASTCALL_O3 vs STDCALL_O3 --->\n"
	@diff --color asm/fastcall_o3.s asm/stdcall_o3.s || true