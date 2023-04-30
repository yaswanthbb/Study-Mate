from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QRect,Qt

import csv

class StudyMate(QMainWindow):
    def __init__(self):
        super(StudyMate,self).__init__()
        uic.loadUi("Study-Mate/gui.ui",self)
        
        self.show()
if __name__ == '__main__':
    app = QApplication([])
    window = StudyMate()
    app.exec_()
