import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from geradormegasena import *
from random import randint
from itertools import count


class GeradorMega(QMainWindow, Ui_GeradorMegaSena):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        super().setupUi(self)
        self.btnGerador.clicked.connect(self.engineMegaSena)
        self.modelo = QStandardItemModel()
        self.resultado.setModel(self.modelo)
        self.qtdJogos.setMaxLength(3)
        self.btnLimpador.clicked.connect(self.limparNumeros)
    
    def limparNumeros(self):
        self.modelo.clear()
        self.btnGerador.setEnabled(True)
        self.qtdJogos.setText('')
    
    def engineMegaSena(self):
        self.btnGerador.setEnabled(False)
        try:
            def gera_sena(lista):
                for i in lista:
                    yield i

            if self.qtdJogos.text() == '':
                qtdJogos = 1
            else:
                qtdJogos = int(self.qtdJogos.text())

            sena: list = []
            for _ in range(qtdJogos):
                jogo: list = []
                while len(jogo) != 6:
                    ran = randint(1, 60)
                    if ran not in jogo:
                        jogo.append(ran)
                    else:
                        continue
                sena.append(jogo)

            sena = gera_sena(sena)
            contador = count()
            nJogo = count()

            while next(contador) < qtdJogos:
                self.modelo.appendRow(QStandardItem(f'Jogo {next(nJogo) + 1}: {next(sena)}\n'))
        except Exception as e:
            self.modelo.appendRow(QStandardItem(f'{e.__class__.__name__}'))


if __name__ == '__main__'    :
    qt = QApplication(sys.argv)
    appMain = GeradorMega()
    appMain.show()
    qt.exec_()
