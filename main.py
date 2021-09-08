import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QSizePolicy
from PyQt5.QtWidgets import QWidget, QGridLayout

class Caculadora(QMainWindow):
    def __init__(self, parent = None):
       super().__init__(parent=parent)
       self.setWindowTitle('caculadora do matheus')
       self.setFixedSize(400, 400)
       self.cw = QWidget()
       self.grid = QGridLayout(self.cw)

       self.display = QLineEdit()
       self.grid.addWidget(self.display, 0, 0, 1, 5)
       self.display.setDisabled(True)
       self.display.setStyleSheet(
           '* {background: #FFF; color #000; font-size: 30px}'
       )
       self.display.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)

       #linha do 7, 8, 9
       self.addBTN(QPushButton('7'), 1, 0, 1, 1)
       self.addBTN(QPushButton('8'), 1, 1, 1, 1)
       self.addBTN(QPushButton('9'), 1, 2, 1, 1)
       self.addBTN(QPushButton('+'), 1, 3, 1, 1)
       self.addBTN(
           QPushButton('C'), 1, 4, 1, 1, 
           lambda: self.display.setText(''),
           'background: #0095ff; color: #fff; font-weight: 700'
           )

       # linha do 4, 5, 6
       self.addBTN(QPushButton('4'), 2, 0, 1, 1)
       self.addBTN(QPushButton('5'), 2, 1, 1, 1)
       self.addBTN(QPushButton('6'), 2, 2, 1, 1)
       self.addBTN(QPushButton('-'), 2, 3, 1, 1)
       self.addBTN(
           QPushButton('<-'), 2, 4, 1, 1,
           lambda: self.display.setText(
               self.display.text()[:-1],
           ),
            'background: #0095ff; color: #fff; font-weight: 700'
        )

       # linha do 1, 2, 3
       self.addBTN(QPushButton('1'), 3, 0, 1, 1)
       self.addBTN(QPushButton('2'), 3, 1, 1, 1)
       self.addBTN(QPushButton('3'), 3, 2, 1, 1)
       self.addBTN(QPushButton('/'), 3, 3, 1, 1)

       # linha do ., 0, =
       self.addBTN(QPushButton('.'), 4, 0, 1, 1)
       self.addBTN(QPushButton('0'), 4, 1, 1, 1)
       self.addBTN(
            QPushButton('='), 4, 2, 1, 1,
            self.igual,
            'background: #0095ff; color: #fff; font-weight: 700'

           )
       self.addBTN(QPushButton('x'), 4, 3, 1, 1)

       self.setCentralWidget(self.cw)

    def igual(self):
        try:
            self.display.setText(
                str(eval(self.display.text()))
            )
        except Exception as e:
            self.display.setText('conta invàlida')

    def addBTN(self, btn, row, col, rowspan, colspan, funcao=None, style=None):

        self.grid.addWidget(btn, row, col, rowspan, colspan)

        if not funcao:
            btn.clicked.connect(
                lambda: self.display.setText(
                    self.display.text() + btn.text()
                )   
            )
        else:
            btn.clicked.connect(funcao)

        if style:
            btn.setStyleSheet(style)
        btn.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = Caculadora()
    app.show()
    qt.exec_()
