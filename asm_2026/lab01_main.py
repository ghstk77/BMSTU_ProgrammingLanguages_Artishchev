from subprocess import CalledProcessError, run
from random import randint
from difflib import ndiff
import sys

try:
    print("Compiling sources...")

    run(["nasm", "-f", "elf64", "main.nasm"], check=True, capture_output=True)
    run(["gcc", "-static", "main.o"], check=True, capture_output=True)

except CalledProcessError as e:
    stderr = e.stderr.decode().strip()
    stdout = e.stdout.decode().strip()
    print(f"Compiling error ({e.cmd})")
    if stderr:
        print(stderr)
    if stdout:
        print(stdout)

try:
    print("Checking...")

    a = randint(1_000, 1_000_000)
    b = randint(1, 1000)

    p = run(["./a.out"], input=f"{a} {b}".encode(), check=True, capture_output=True)

    stdout = p.stdout.decode()

    print("Application output:")
    print(stdout)

    etalon = f"{a} + {b} = {a + b}\n{a} - {b} = {a - b}\n{a} * {b} = {a * b}\n{a} / {b} = {a // b}\n"

    if stdout != etalon:
        print("Output not matched:")

        result = ndiff(
            stdout.splitlines(keepends=True), etalon.splitlines(keepends=True)
        )

        print("".join(result))

        exit(1)
    else:
        print("Output matched!")


except CalledProcessError as e:
    stderr = e.stderr.decode().strip()
    stdout = e.stdout.decode().strip()
    print(f"Checking error ({e.cmd})")
    if stderr:
        print(stderr)
    if stdout:
        print(stdout)
