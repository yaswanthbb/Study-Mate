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
        
        self.progress_bars = {}

        y = 40

        for subject,chapter in self.subject_chapters.items():
            label = QLabel(self.progressFrame)
            label.setGeometry(QRect(10,y,92,23))
            label.setObjectName(f"label_{subject}")
            label.setText(subject)
            progressBar = QProgressBar(self.progressFrame)
            progressBar.setGeometry((QRect(120, y, 118, 23)))
            progressBar.setObjectName(f"progressBar_{subject}")

            y += 40
            self.progress_bars[subject] = progressBar
            
        self.show()


if __name__ == '__main__':
    app = QApplication([])
    window = StudyMate()
    app.exec_()
