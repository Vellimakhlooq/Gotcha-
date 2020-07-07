# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import cv2
from darkflow.net.build import TFNet
import numpy as np
import time
import os
from PyQt5 import QtCore, QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QPushButton, QInputDialog, QLineEdit
from PyQt5.uic import loadUi
import sys
#from PIL import Image
import tkinter as tk
from tkinter import filedialog
from PyQt5 import QtCore, QtGui, QtWidgets
from obj import Ui_object
option= {
    'model':'cfg/yolo.cfg',
    'load':'bin/yolov2.weights',
    'threshold': 0.3,
    }


class Ui_project(object):

    def CameraTest(self):
        cap = cv2.VideoCapture(0)
        cap.set(3,640) # set Width
        cap.set(4,480) # set Height
        while(True):
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            cv2.imshow('CamTest', frame)
    
            k = cv2.waitKey(30) & 0xff
            if k == 27: # press 'ESC' to quit
                break
        cap.release()
        cv2.destroyAllWindows()
    def camera_live(self):

        tfnet = TFNet(option)
        colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]

        cap= cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)


        while True:
            stime = time.time()
            ret, frame = cap.read()
            if (ret==True):
                
                results = tfnet.return_predict(frame)
                for color, result in zip(colors, results):
                    tl = (result['topleft']['x'], result['topleft']['y'])
                    br = (result['bottomright']['x'], result['bottomright']['y'])
                    label = result['label']
                    confidence = result['confidence']
                    text = '{}: {:.0f}%'.format(label, confidence * 100)
                    frame = cv2.rectangle(frame, tl, br, color, 5)
                    frame = cv2.putText(
                        frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                cv2.imshow('frame', frame)
                print('FPS {:.1f}'.format(1 / (time.time() - stime)))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        cv2.destroyAllWindows()
    def upload_video(self):

        tfnet = TFNet(option)
        colors = [tuple(255 * np.random.rand(3)) for _ in range(10)]
        root = tk.Tk()
        root.withdraw()

        file_path = filedialog.askopenfilename()
        cap= cv2.VideoCapture(file_path)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 512)
        

        while True:
            stime = time.time()
            ret, frame = cap.read()

            if (ret==True):
                
                results = tfnet.return_predict(frame)
                for color, result in zip(colors, results):
                    tl = (result['topleft']['x'], result['topleft']['y'])
                    br = (result['bottomright']['x'], result['bottomright']['y'])
                    label = result['label']
                    confidence = result['confidence']
                    text = '{}: {:.0f}%'.format(label, confidence * 100)
                    frame = cv2.rectangle(frame, tl, br, color, 5)
                    frame = cv2.putText(
                        frame, text, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
                cv2.imshow('frame', frame)

                print('FPS {:.1f}'.format(1 / (time.time() - stime)))
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()

        cv2.destroyAllWindows()
    def obj(self):
        self.window=QtWidgets.QMainWindow()
        self.ui =Ui_object()
        self.ui.setupUi(self.window)
        #login.hide()
        self.window.show()

    def setupUi(self, project):
        project.setObjectName("project")
        project.resize(430, 561)
        project.setStyleSheet("*{background-color:black}")
        self.centralwidget = QtWidgets.QWidget(project)
        self.centralwidget.setObjectName("centralwidget")
        self.gotcha = QtWidgets.QLabel(self.centralwidget)
        self.gotcha.setGeometry(QtCore.QRect(80, 80, 251, 71))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.gotcha.setFont(font)
        self.gotcha.setStyleSheet("background-color:#E8B510;\n"
"padding:10px;\n"
"border-radius:28px;\n"
"color:black;\n"
"font-size:50px;\n"
"font-family:gotham;")
        self.gotcha.setAlignment(QtCore.Qt.AlignCenter)
        self.gotcha.setWordWrap(False)
        self.gotcha.setObjectName("gotcha")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 29, 391, 501))
        self.frame.setStyleSheet("background-color:#E8B510;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 39, 371, 481))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.camera_test = QtWidgets.QPushButton(self.frame_2)
        self.camera_test.setGeometry(QtCore.QRect(100, 130, 161, 61))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.camera_test.setFont(font)
        self.camera_test.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;\n"
"")
        self.camera_test.setObjectName("camera_test")
        ##############
        self.camera_test.clicked.connect(self.CameraTest)
        #################
        self.stream = QtWidgets.QPushButton(self.frame_2)
        self.stream.setGeometry(QtCore.QRect(100, 210, 161, 61))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.stream.setFont(font)
        self.stream.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;\n"
"")
        self.stream.setObjectName("stream")
        ###############
        self.stream.clicked.connect(self.camera_live)
        ###############
        self.upload = QtWidgets.QPushButton(self.frame_2)
        self.upload.setGeometry(QtCore.QRect(100, 290, 171, 61))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.upload.setFont(font)
        self.upload.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;\n"
"")
        self.upload.setObjectName("upload")
        ##################
        self.upload.clicked.connect(self.upload_video)
        ##################
        self.camera_test_2 = QtWidgets.QPushButton(self.frame_2)
        self.camera_test_2.setGeometry(QtCore.QRect(110, 380, 151, 31))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.camera_test_2.setFont(font)
        self.camera_test_2.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;\n"
"")
        self.camera_test_2.setObjectName("camera_test_2")
        ###############
        self.camera_test_2.clicked.connect(self.obj)
        ###########
        self.frame.raise_()
        self.frame_2.raise_()
        self.gotcha.raise_()
        project.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(project)
        self.statusbar.setObjectName("statusbar")
        project.setStatusBar(self.statusbar)

        self.retranslateUi(project)
        QtCore.QMetaObject.connectSlotsByName(project)

    def retranslateUi(self, project):
        _translate = QtCore.QCoreApplication.translate
        project.setWindowTitle(_translate("project", "Gotcha!"))
        self.gotcha.setText(_translate("project", "Gotcha!"))
        self.camera_test.setText(_translate("project", "Camera"))
        self.stream.setText(_translate("project", "Live Stream"))
        self.upload.setText(_translate("project", "Upload Video"))
        self.camera_test_2.setText(_translate("project", "Objects"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    project = QtWidgets.QMainWindow()
    ui = Ui_project()
    ui.setupUi(project)
    project.show()
    sys.exit(app.exec_())
