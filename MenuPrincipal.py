from gpiozero import LED
from time import sleep

point = 0.2
tiret = point * 3

espaceElement = point
espaceLettre = point * 3
espaceMot = point * 7 - espaceLettre

message = input('Que voulez-vous dire ?')

for x in message:
    if x.upper() == 'A':
        exec(open("./a.py".read()))
        sleep(espaceLettre)

    elif x.upper() == 'B':
        import b
        sleep(espaceLettre)

    elif x.upper() == 'C':
        import c
        sleep(espaceLettre)

    elif x.upper() == 'D':
        import d
        sleep(espaceLettre)

    elif x.upper() == 'E':
        import e
        sleep(espaceLettre)

    elif x.upper() == 'F':
        import f
        sleep(espaceLettre)

    elif x.upper() == 'G':
        import g
        sleep(espaceLettre)

    elif x.upper() == 'H':
        import h
        sleep(espaceLettre)

    elif x.upper() == 'I':
        import i
        sleep(espaceLettre)

    elif x.upper() == 'J':
        import j
        sleep(espaceLettre)

    elif x.upper() == 'K':
        import k
        sleep(espaceLettre)

    elif x.upper() == 'L':
        import l
        sleep(espaceLettre)

    elif x.upper() == 'M':
        import m
        sleep(espaceLettre)

    elif x.upper() == 'N':
        import n
        sleep(espaceLettre)

    elif x.upper() == 'O':
        import o
        sleep(espaceLettre)

    elif x.upper() == 'P':
        import p
        sleep(espaceLettre)

    elif x.upper() == 'Q':
        import q
        sleep(espaceLettre)

    elif x.upper() == 'R':
        import r
        sleep(espaceLettre)

    elif x.upper() == 'S':
        import s
        sleep(espaceLettre)

    elif x.upper() == 'T':
        import t
        sleep(espaceLettre)

    elif x.upper() == 'U':
        import u
        sleep(espaceLettre)

    elif x.upper() == 'V':
        import v
        sleep(espaceLettre)

    elif x.upper() == 'W':
        import w
        sleep(espaceLettre)

    elif x.upper() == 'X':
        import x
        sleep(espaceLettre)

    elif x.upper() == 'Y':
        import y
        sleep(espaceLettre)

    elif x.upper() == 'Z':
        import z
        sleep(espaceLettre)

    elif x == ' ':
        sleep(espaceMot)


