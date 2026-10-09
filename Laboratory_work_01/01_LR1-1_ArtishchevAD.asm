global main
 
extern printf
extern scanf
 
section .data

scanf_fmt db "%ld%ld", 0

fmt_add db "%ld + %ld = %ld", 0x0a, "%ld - %ld = %ld", 0x0a, \
           "%ld * %ld = %ld", 0x0a,"%ld / %ld = %ld", 0x0a, 0x0

section .text

main:
; ------------------------------------------------------------------------------
;                      Код получения значений из консоли
;                                  НЕ МЕНЯТЬ!
    push rbp
    mov rbp, rsp

    sub rsp, 0x10

    lea rsi, [rbp - 0x10]
    lea rdx, [rbp - 0x8]
    mov rdi, scanf_fmt
    call scanf

    pop rax
    pop rbx
;
; ------------------------------------------------------------------------------


; ------------------------------------------------------------------------------
;                                   ЗАДАНИЕ
;
; В регистрах RAX и RBX находятся значения, которые необходимо сложить,
; вычесть, умножить и разделить. 
;
; Записать код, который вычисляет:
; rcx = rax + rbx
; rdx = rax - rbx
; rsi = rax * rbx
; rdi = rax / rbx

    mov r8, rax

    mov rcx, rax
    add rcx, rbx

    mov rsi, rax
    imul rsi, rbx

    cqo
    idiv rbx
    mov rdi, rax

    mov rax, r8
    mov rdx, rax
    sub rdx, rbx

;
; ------------------------------------------------------------------------------


; ------------------------------------------------------------------------------
;                                  Код вывода
;                                  НЕ МЕНЯТЬ!
    sub rsp, 0x8

    mov r10, rcx
    mov r11, rdx
    mov r12, rsi
    mov r13, rdi

    push r13
    push rbx
    push rax

    push r12
    push rbx
    push rax

    push r11
    mov r9, rbx
    mov r8, rax

    mov rcx, r10
    mov rdx, rbx
    mov rsi, rax

    mov rdi, fmt_add

    call printf

    add rsp, 0x40
    pop rbp

    mov rax, 0

    ret
; ------------------------------------------------------------------------------
