import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from geradormegasena import *


class GeradorMega(QMainWindow, Ui_GeradorMegaSena):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
    
    def engineMegaSena(self):
        from random import randint
from time import sleep
from itertools import count


def gera_sena(lista):
    for i in lista:
        yield i


    n_jogo = int(input('Quantos jogos você quer gerar? '))

    sena = []

    for i in range(n_jogo):
        jogo: list = []
        while len(jogo) != 6:
            ran = randint(1, 60)
            if ran not in jogo:
                jogo.append(ran)
            else:
                continue
        sena.append(jogo)

    s = gera_sena(sena)
    c = count()
    d = count()

    while next(c) < n_jogo:
        print(f'Jogo {next(d) + 1}: {next(s)}')
        sleep(0.5)

if __name__ == '__main__'    :
    qt = QApplication(sys.argv)
    appMain = GeradorMega()
    appMain.show()
    qt.exec_()
