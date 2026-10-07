#!/bin/sh
set -eu
nasm -f elf64 main.nasm -o main.o
gcc -static main.o -o a.out
