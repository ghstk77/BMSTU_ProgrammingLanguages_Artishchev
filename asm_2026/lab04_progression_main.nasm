[bits 64]

global main
 
extern printf
extern scanf
 
section .data

scanf_fmt db "%lu%lu%lu", 0
printf_fmt db "%lu ", 0

section .text

main:
; ------------------------------------------------------------------------------
;                      Код получения значений из консоли
;                                  НЕ МЕНЯТЬ!
    push rbp
    mov rbp, rsp

    sub rsp, 0x20

    lea rcx, [rbp - 0x10]
    lea rdx, [rbp - 0x18]
    lea rsi, [rbp - 0x20]
    mov rdi, scanf_fmt
    call scanf

    pop rax
    pop rbx
    pop rcx

    add rsp, 0x8
    call lab_code

    pop rbp

    mov rax, 0

    ret
;
; ------------------------------------------------------------------------------

printer:
    push rbp
    mov rbp, rsp
    push rcx
    push rax
    push rbx
    sub rsp, 0x28
    
    mov rdi, printf_fmt
    mov rsi, rdx
    call printf
    
    add rsp, 0x28
    pop rbx
    pop rax
    pop rcx
    mov rsp, rbp
    pop rbp
    ret
; ------------------------------------------------------------------------------
;                                   ЗАДАНИЕ
;
;    Разработать программу вывода
;    арифметической прогрессии:
;    
;    – В регистре RAX — начальное значение
;    – В регистре RBX — шаг прогрессии
;    – В регистре RCX — количество элементов
;   
;    
;    *Модернизировать программу через
;    использование инструкции loop
;    
;
; ------------------------------------------------------------------------------
        
lab_code:
    push rbp
    mov rbp, rsp

;; Внутри пишем наш код

;;
    pop rbp
    ret








