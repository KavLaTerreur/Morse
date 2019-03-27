from gpiozero import LED
from a import A
from b import B
from c import C
from d import D
from e import E
from f import F
from g import G
from h import H
from i import I
from j import J
from k import K
from l import L
from m import M
from n import N
from o import O
from p import P
from q import Q
from r import R
from s import S
from t import T
from u import U
from v import V
from w import W
from x import X
from y import Y
from z import Z
from time import sleep

point = 0.2
tiret = point * 3

espaceElement = point
espaceLettre = point * 3
espaceMot = point * 7 - espaceLettre

message = input('Que voulez-vous dire ?')

for x in message:
    if x.upper() == 'A':
        A()
        sleep(espaceLettre)

    elif x.upper() == 'B':
        B()
        sleep(espaceLettre)

    elif x.upper() == 'C':
        C()
        sleep(espaceLettre)

    elif x.upper() == 'D':
        D()
        sleep(espaceLettre)

    elif x.upper() == 'E':
        E()
        sleep(espaceLettre)

    elif x.upper() == 'F':
        F()
        sleep(espaceLettre)

    elif x.upper() == 'G':
        G()
        sleep(espaceLettre)

    elif x.upper() == 'H':
        H()
        sleep(espaceLettre)

    elif x.upper() == 'I':
        I()
        sleep(espaceLettre)

    elif x.upper() == 'J':
        J()
        sleep(espaceLettre)

    elif x.upper() == 'K':
        K()
        sleep(espaceLettre)

    elif x.upper() == 'L':
        L()
        sleep(espaceLettre)

    elif x.upper() == 'M':
        M()
        sleep(espaceLettre)

    elif x.upper() == 'N':
        N()
        sleep(espaceLettre)

    elif x.upper() == 'O':
        O()
        sleep(espaceLettre)

    elif x.upper() == 'P':
        P()
        sleep(espaceLettre)

    elif x.upper() == 'Q':
        Q()
        sleep(espaceLettre)

    elif x.upper() == 'R':
        R()
        sleep(espaceLettre)

    elif x.upper() == 'S':
        S()
        sleep(espaceLettre)

    elif x.upper() == 'T':
        T()
        sleep(espaceLettre)

    elif x.upper() == 'U':
        U()
        sleep(espaceLettre)

    elif x.upper() == 'V':
        V()
        sleep(espaceLettre)

    elif x.upper() == 'W':
        W()
        sleep(espaceLettre)

    elif x.upper() == 'X':
        X()
        sleep(espaceLettre)

    elif x.upper() == 'Y':
        Y()
        sleep(espaceLettre)

    elif x.upper() == 'Z':
        Z()
        sleep(espaceLettre)

    elif x == ' ':
        sleep(espaceMot)

