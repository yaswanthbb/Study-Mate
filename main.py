from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QRect,Qt

import csv

class StudyMate(QMainWindow):
    def __init__(self):
        super(StudyMate,self).__init__()
        uic.loadUi("gui.ui",self)
        
        with open('data.csv','r') as file:
            data = csv.DictReader(file)
            
            self.subject_chapters={}    
            
            for row in data:
                subject = row['Subject']
                chapter = row['Chapter']
                if subject in self.subject_chapters:
                    self.subject_chapters[subject].append(chapter)
                else:
                    self.subject_chapters[subject] = [chapter]

        self.show()
if __name__ == '__main__':
    app = QApplication([])
    window = StudyMate()
    app.exec_()
