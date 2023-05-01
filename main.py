from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QFont

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
        
        with open('exam_dates.csv','r') as file:
             exam_data = csv.DictReader(file)
             self.exam_names = {}
             for row in exam_data:
                 date = row['Exam Date']
                 subject = row['Subject']
                 if subject in self.exam_names:
                     self.exam_names[subject].append(date)
                 else:
                     self.exam_names[subject] = [date]


        self.progress_bars = {}

        y = 40

        for subject,chapters in self.subject_chapters.items():
            label = QLabel(self.progressFrame)
            label.setFont(QFont("Arial", 10))
            label.setMinimumWidth(200)
            label.setGeometry(QRect(10,y,200,23))
            label.setObjectName(f"label_{subject}")
            label.setText(subject)
            progressBar = QProgressBar(self.progressFrame)
            progressBar.setGeometry((QRect(180, y, 118, 23)))
            progressBar.setObjectName(f"progressBar_{subject}")
            progressBar.setMinimum(0)
            progressBar.setMaximum(len(chapters))
            y += 40
            self.progress_bars[subject] = progressBar

        x = 30
        y = 100
        for subject, chapters in self.subject_chapters.items():
            label = QLabel(self.centralWidget)
            label.setMinimumWidth(200)
            label.setGeometry(QRect(x, y, 200, 17))
            label.setText(subject)
            frame = QFrame(self.centralWidget)
            frame.setGeometry(QRect(x, y+30, 151, 221))
            frame.setFrameShape(QFrame.StyledPanel)
            frame.setFrameShadow(QFrame.Raised)
            x += 230
            for i, chapter in enumerate(chapters):
                checkBox = QCheckBox(frame)
                checkBox.setGeometry(QRect(10, 40 + i*30 , 95, 23))
                checkBox.setText(chapter)
                checkBox.stateChanged.connect(lambda state, subject=subject, frame=frame: self.update_progress(subject, frame))
        x = 250
        y = 40
        for subject, exam_dates in self.exam_names.items():
            label = QLabel(self.examFrame)
            label.setFont(QFont("Arial", 10))
            label.setMinimumWidth(200)
            label.setGeometry(QRect(10,y,200,23))
            label.setText(subject)
            for exam_date in exam_dates:
                label = QLabel(self.examFrame)
                label.setGeometry(QRect(x, y, 200, 23))
                label.setText(exam_date)
                checkBox = QCheckBox(self.examFrame)
                checkBox.setGeometry((QRect(x + 180, y, 118, 23)))
                y += 40
        x += 400
        y = 40


        self.show()

    def update_progress(self, subject, frame):
        checked_chapters = [checkBox.text() for checkBox in frame.findChildren(QCheckBox) if checkBox.isChecked()]
        progressBar = self.progress_bars[subject]
        progressBar.setValue(len(checked_chapters))


if __name__ == '__main__':
    app = QApplication([])
    window = StudyMate()
    app.exec_()
