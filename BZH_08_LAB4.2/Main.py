#!/usr/bin/env python3
# coding=utf-8

import re
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('Работа со строками в Python')
        

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)


    def is_palindrome(text):
        letter = ''.join(filter(str.isalpha, text))
        return letter == letter[::-1]

    def solve(self):
        self.textEdit_words.clear()
        text = self.textEdit_text.toPlainText()  # получаем наш текст
        txt = text.split()
        self.textEdit_words.insertPlainText("Самое длинное слово: " + max(txt, key=len)+ "\n")
        self.textEdit_words.insertPlainText("Самое короткое слово: " + min(txt, key=len)+ "\n")

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()

def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
