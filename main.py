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

        y = 40 
        for subject,chapters in self.subject_chapters.items():
            label = QLabel(self.centralWidget)
            label.setGeometry(QRect(30, y, 67, 17))
            label.setText(subject)
            frame = QFrame(self.centralWidget)
            frame.setGeometry(QRect(30, y+30, 151, 221))
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)
            y += 260
            for i, chapter in enumerate(chapters):
                checkBox = QCheckBox(frame)
                checkBox.setGeometry(QRect(10, 40 + i*30 , 95, 23))
                checkBox.setText(chapter)
                checkBox.stateChanged.connect(lambda state, subject=subject, frame=frame: self.update_progress(subject, frame))
        self.show()

    def update_progress(self, subject, frame):
        checked_chapters = [checkBox.text() for checkBox in frame.findChildren(QCheckBox) if checkBox.isChecked()]
        progressBar = self.progress_bars[subject]
        progressBar.setValue(len(checked_chapters))


if __name__ == '__main__':
    app = QApplication([])
    window = StudyMate()
    app.exec_()
