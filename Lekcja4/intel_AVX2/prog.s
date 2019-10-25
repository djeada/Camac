	.file	"avx2_example.c"
	.text
	.globl	randomize
	.type	randomize, @function
randomize:
.LFB3695:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$40, %rsp
	.cfi_offset 3, -24
	movq	%rdi, -40(%rbp)
	movq	%rsi, -48(%rbp)
	movq	$0, -24(%rbp)
	jmp	.L2
.L3:
	movq	-24(%rbp), %rax
	leaq	0(,%rax,4), %rdx
	movq	-40(%rbp), %rax
	leaq	(%rdx,%rax), %rbx
	call	rand
	movl	%eax, %ecx
	movl	$274877907, %edx
	movl	%ecx, %eax
	imull	%edx
	sarl	$6, %edx
	movl	%ecx, %eax
	sarl	$31, %eax
	subl	%eax, %edx
	movl	%edx, %eax
	imull	$1000, %eax, %eax
	subl	%eax, %ecx
	movl	%ecx, %eax
	movl	%eax, (%rbx)
	addq	$1, -24(%rbp)
.L2:
	movq	-24(%rbp), %rax
	cmpq	-48(%rbp), %rax
	jb	.L3
	nop
	addq	$40, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3695:
	.size	randomize, .-randomize
	.globl	add_normal
	.type	add_normal, @function
add_normal:
.LFB3696:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	movq	%rdx, -40(%rbp)
	movq	$0, -8(%rbp)
	jmp	.L5
.L6:
	movq	-8(%rbp), %rax
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movq	-8(%rbp), %rdx
	leaq	0(,%rdx,4), %rcx
	movq	-24(%rbp), %rdx
	addq	%rcx, %rdx
	movl	(%rdx), %ecx
	movq	-8(%rbp), %rdx
	leaq	0(,%rdx,4), %rsi
	movq	-32(%rbp), %rdx
	addq	%rsi, %rdx
	movl	(%rdx), %edx
	addl	%ecx, %edx
	movl	%edx, (%rax)
	addq	$1, -8(%rbp)
.L5:
	movq	-8(%rbp), %rax
	cmpq	-40(%rbp), %rax
	jb	.L6
	nop
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3696:
	.size	add_normal, .-add_normal
	.globl	add_powerfull
	.type	add_powerfull, @function
add_powerfull:
.LFB3697:
	.cfi_startproc
	leaq	8(%rsp), %r10
	.cfi_def_cfa 10, 0
	andq	$-32, %rsp
	pushq	-8(%r10)
	pushq	%rbp
	.cfi_escape 0x10,0x6,0x2,0x76,0
	movq	%rsp, %rbp
	pushq	%r10
	.cfi_escape 0xf,0x3,0x76,0x78,0x6
	subq	$392, %rsp
	movq	%rdi, -360(%rbp)
	movq	%rsi, -368(%rbp)
	movq	%rdx, -376(%rbp)
	movq	%fs:40, %rax
	movq	%rax, -24(%rbp)
	xorl	%eax, %eax
	movq	$0, -280(%rbp)
	jmp	.L8
.L12:
	movq	-280(%rbp), %rax
	addq	$7, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %eax
	movq	-280(%rbp), %rdx
	addq	$6, %rdx
	leaq	0(,%rdx,4), %rcx
	movq	-360(%rbp), %rdx
	addq	%rcx, %rdx
	movl	(%rdx), %edx
	movq	-280(%rbp), %rcx
	addq	$5, %rcx
	leaq	0(,%rcx,4), %rsi
	movq	-360(%rbp), %rcx
	addq	%rsi, %rcx
	movl	(%rcx), %ecx
	movq	-280(%rbp), %rsi
	addq	$4, %rsi
	leaq	0(,%rsi,4), %rdi
	movq	-360(%rbp), %rsi
	addq	%rdi, %rsi
	movl	(%rsi), %esi
	movq	-280(%rbp), %rdi
	addq	$3, %rdi
	leaq	0(,%rdi,4), %r8
	movq	-360(%rbp), %rdi
	addq	%r8, %rdi
	movl	(%rdi), %edi
	movq	-280(%rbp), %r8
	addq	$2, %r8
	leaq	0(,%r8,4), %r9
	movq	-360(%rbp), %r8
	addq	%r9, %r8
	movl	(%r8), %r8d
	movq	-280(%rbp), %r9
	addq	$1, %r9
	leaq	0(,%r9,4), %r10
	movq	-360(%rbp), %r9
	addq	%r10, %r9
	movl	(%r9), %r9d
	movq	-280(%rbp), %r10
	leaq	0(,%r10,4), %r11
	movq	-360(%rbp), %r10
	addq	%r11, %r10
	movl	(%r10), %r10d
	movl	%r10d, -344(%rbp)
	movl	%r9d, -308(%rbp)
	movl	%r8d, -304(%rbp)
	movl	%edi, -300(%rbp)
	movl	%esi, -296(%rbp)
	movl	%ecx, -292(%rbp)
	movl	%edx, -288(%rbp)
	movl	%eax, -284(%rbp)
	movl	-344(%rbp), %eax
	movl	-308(%rbp), %edx
	vmovd	%edx, %xmm4
	vpinsrd	$1, %eax, %xmm4, %xmm2
	movl	-304(%rbp), %eax
	movl	-300(%rbp), %edx
	vmovd	%edx, %xmm5
	vpinsrd	$1, %eax, %xmm5, %xmm1
	movl	-296(%rbp), %eax
	movl	-292(%rbp), %edx
	vmovd	%edx, %xmm6
	vpinsrd	$1, %eax, %xmm6, %xmm3
	movl	-288(%rbp), %eax
	movl	-284(%rbp), %edx
	vmovd	%edx, %xmm7
	vpinsrd	$1, %eax, %xmm7, %xmm0
	vpunpcklqdq	%xmm3, %xmm0, %xmm0
	vpunpcklqdq	%xmm2, %xmm1, %xmm1
	vinserti128	$0x1, %xmm1, %ymm0, %ymm0
	vmovdqa	%ymm0, -80(%rbp)
	vmovdqa	-80(%rbp), %ymm0
	vmovdqa	%ymm0, -240(%rbp)
	movq	-280(%rbp), %rax
	addq	$7, %rax
	leaq	0(,%rax,4), %rdx
	movq	-368(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %eax
	movq	-280(%rbp), %rdx
	addq	$6, %rdx
	leaq	0(,%rdx,4), %rcx
	movq	-368(%rbp), %rdx
	addq	%rcx, %rdx
	movl	(%rdx), %edx
	movq	-280(%rbp), %rcx
	addq	$5, %rcx
	leaq	0(,%rcx,4), %rsi
	movq	-368(%rbp), %rcx
	addq	%rsi, %rcx
	movl	(%rcx), %ecx
	movq	-280(%rbp), %rsi
	addq	$4, %rsi
	leaq	0(,%rsi,4), %rdi
	movq	-368(%rbp), %rsi
	addq	%rdi, %rsi
	movl	(%rsi), %esi
	movq	-280(%rbp), %rdi
	addq	$3, %rdi
	leaq	0(,%rdi,4), %r8
	movq	-368(%rbp), %rdi
	addq	%r8, %rdi
	movl	(%rdi), %edi
	movq	-280(%rbp), %r8
	addq	$2, %r8
	leaq	0(,%r8,4), %r9
	movq	-368(%rbp), %r8
	addq	%r9, %r8
	movl	(%r8), %r8d
	movq	-280(%rbp), %r9
	addq	$1, %r9
	leaq	0(,%r9,4), %r10
	movq	-368(%rbp), %r9
	addq	%r10, %r9
	movl	(%r9), %r9d
	movq	-280(%rbp), %r10
	leaq	0(,%r10,4), %r11
	movq	-368(%rbp), %r10
	addq	%r11, %r10
	movl	(%r10), %r10d
	movl	%r10d, -340(%rbp)
	movl	%r9d, -336(%rbp)
	movl	%r8d, -332(%rbp)
	movl	%edi, -328(%rbp)
	movl	%esi, -324(%rbp)
	movl	%ecx, -320(%rbp)
	movl	%edx, -316(%rbp)
	movl	%eax, -312(%rbp)
	movl	-340(%rbp), %eax
	movl	-336(%rbp), %edx
	vmovd	%edx, %xmm4
	vpinsrd	$1, %eax, %xmm4, %xmm2
	movl	-332(%rbp), %eax
	movl	-328(%rbp), %edx
	vmovd	%edx, %xmm5
	vpinsrd	$1, %eax, %xmm5, %xmm1
	movl	-324(%rbp), %eax
	movl	-320(%rbp), %edx
	vmovd	%edx, %xmm6
	vpinsrd	$1, %eax, %xmm6, %xmm3
	movl	-316(%rbp), %eax
	movl	-312(%rbp), %edx
	vmovd	%edx, %xmm7
	vpinsrd	$1, %eax, %xmm7, %xmm0
	vpunpcklqdq	%xmm3, %xmm0, %xmm0
	vpunpcklqdq	%xmm2, %xmm1, %xmm1
	vinserti128	$0x1, %xmm1, %ymm0, %ymm0
	vmovdqa	%ymm0, -112(%rbp)
	vmovdqa	-112(%rbp), %ymm0
	vmovdqa	%ymm0, -208(%rbp)
	vmovdqa	-240(%rbp), %ymm0
	vmovdqa	%ymm0, -176(%rbp)
	vmovdqa	-208(%rbp), %ymm0
	vmovdqa	%ymm0, -144(%rbp)
	vmovdqa	-176(%rbp), %ymm1
	vmovdqa	-144(%rbp), %ymm0
	vpaddd	%ymm0, %ymm1, %ymm0
	vmovdqa	%ymm0, -272(%rbp)
	movq	-280(%rbp), %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	leaq	-272(%rbp), %rax
	movl	(%rax), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$1, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-268(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$2, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-264(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$3, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-260(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$4, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-256(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$5, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-252(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$6, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-248(%rbp), %eax
	movl	%eax, (%rdx)
	movq	-280(%rbp), %rax
	addq	$7, %rax
	leaq	0(,%rax,4), %rdx
	movq	-360(%rbp), %rax
	addq	%rax, %rdx
	movl	-244(%rbp), %eax
	movl	%eax, (%rdx)
	addq	$8, -280(%rbp)
.L8:
	movq	-280(%rbp), %rax
	cmpq	-376(%rbp), %rax
	jb	.L12
	nop
	movq	-24(%rbp), %rax
	xorq	%fs:40, %rax
	je	.L13
	call	__stack_chk_fail
.L13:
	addq	$392, %rsp
	popq	%r10
	.cfi_def_cfa 10, 0
	popq	%rbp
	leaq	-8(%r10), %rsp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3697:
	.size	add_powerfull, .-add_powerfull
	.section	.rodata
.LC0:
	.string	"%d "
	.text
	.globl	print_data
	.type	print_data, @function
print_data:
.LFB3698:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$32, %rsp
	movq	%rdi, -24(%rbp)
	movq	%rsi, -32(%rbp)
	movq	$0, -8(%rbp)
	jmp	.L15
.L16:
	movq	-8(%rbp), %rax
	leaq	0(,%rax,4), %rdx
	movq	-24(%rbp), %rax
	addq	%rdx, %rax
	movl	(%rax), %eax
	movl	%eax, %esi
	movl	$.LC0, %edi
	movl	$0, %eax
	call	printf
	addq	$1, -8(%rbp)
.L15:
	movq	-8(%rbp), %rax
	cmpq	-32(%rbp), %rax
	jb	.L16
	movl	$10, %edi
	call	putchar
	nop
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3698:
	.size	print_data, .-print_data
	.globl	main
	.type	main, @function
main:
.LFB3699:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$8416, %rsp
	movq	%fs:40, %rax
	movq	%rax, -8(%rbp)
	xorl	%eax, %eax
	movl	$0, %edi
	call	time
	movl	%eax, %edi
	call	srand
	leaq	-8400(%rbp), %rax
	movl	$4192, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	memset
	leaq	-4208(%rbp), %rax
	movl	$4192, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	memset
	leaq	-8400(%rbp), %rax
	movl	$1048, %esi
	movq	%rax, %rdi
	call	randomize
	leaq	-4208(%rbp), %rax
	movl	$1048, %esi
	movq	%rax, %rdi
	call	randomize
	leaq	-4208(%rbp), %rcx
	leaq	-8400(%rbp), %rax
	movl	$1048, %edx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	call	add_normal
	leaq	-8400(%rbp), %rax
	movl	$1048, %esi
	movq	%rax, %rdi
	call	randomize
	leaq	-4208(%rbp), %rax
	movl	$1048, %esi
	movq	%rax, %rdi
	call	randomize
	leaq	-4208(%rbp), %rcx
	leaq	-8400(%rbp), %rax
	movl	$1048, %edx
	movq	%rcx, %rsi
	movq	%rax, %rdi
	call	add_powerfull
	movl	$0, %eax
	movq	-8(%rbp), %rcx
	xorq	%fs:40, %rcx
	je	.L19
	call	__stack_chk_fail
.L19:
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3699:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 5.4.0-6ubuntu1~16.04.11) 5.4.0 20160609"
	.section	.note.GNU-stack,"",@progbits
