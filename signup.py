# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'noback.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
#from login import login_Ui_login
from project import Ui_project
import sqlite3

class registration_form(object):
    def insertdata(self):
        username= self.lineEdit.text()
            
        password=self.lineEdit_3.text()
        cpassword=self.lineEdit_4.text()
        
        if not username:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Enter username')
            msg.setWindowTitle("Error")
            msg.exec_()

        if not password:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Enter password')
            msg.setWindowTitle("Error")
            msg.exec_()
        if not cpassword:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Confirm password')
            msg.setWindowTitle("Error")
            msg.exec_()
        


        elif password != cpassword:

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Password")
            msg.setInformativeText('Password dont match')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            connection=sqlite3.connect("login_gotcha.db")
            connection.execute("INSERT INTO USERS VALUES(?,?)",(username,password))         
            connection.commit()
            connection.close()
            print("Regsitered successfully")
            msg = QMessageBox()
            #msg.setIcon(QMessageBox.Alert)
            msg.setText("DONE")
            msg.setInformativeText('Successfully Regsitered')
            msg.setWindowTitle("ALERT")
            msg.exec_()

            """self.window=QtWidgets.QMainWindow()
            self.ui =Ui_project()
            self.ui.setupUi(self.window)"""
            #MainWindow.hide()
            #MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 482)
        MainWindow.setStyleSheet("background-color:black")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 19, 581, 441))
        self.frame.setStyleSheet("background-color:#E8B510")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 10, 561, 421))
        self.frame_3.setStyleSheet("background-color:black")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.create_account = QtWidgets.QLabel(self.frame_3)
        self.create_account.setGeometry(QtCore.QRect(140, 20, 301, 61))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.create_account.setFont(font)
        self.create_account.setStyleSheet("background-color:#E8B510;\n"
"padding:3px;\n"
"border-radius:22px;\n"
"color:black;\n"
"font-size:30px;\n"
"font-family:gotham;")
        self.create_account.setAlignment(QtCore.Qt.AlignCenter)
        self.create_account.setWordWrap(False)
        self.create_account.setObjectName("create_account")
        self.signup_username = QtWidgets.QLabel(self.frame_3)
        self.signup_username.setGeometry(QtCore.QRect(110, 170, 121, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signup_username.setFont(font)
        self.signup_username.setStyleSheet("\n"
"background-color:#E8B510;\n"
"text-align:center;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:20px;\n"
"font-family:gotham;")
        self.signup_username.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_username.setWordWrap(False)
        self.signup_username.setObjectName("signup_username")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(250, 180, 211, 21))
        self.lineEdit.setStyleSheet("background-color:white")
        self.lineEdit.setPlaceholderText("")
        self.lineEdit.setObjectName("lineEdit")
        self.signup_pass = QtWidgets.QLabel(self.frame_3)
        self.signup_pass.setGeometry(QtCore.QRect(110, 220, 121, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signup_pass.setFont(font)
        self.signup_pass.setStyleSheet("\n"
"background-color:#E8B510;\n"
"text-align:center;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:20px;\n"
"font-family:gotham;")
        self.signup_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_pass.setWordWrap(False)
        self.signup_pass.setObjectName("signup_pass")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 230, 211, 21))
        self.lineEdit_3.setStyleSheet("background-color:white")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.signup_con_pass = QtWidgets.QLabel(self.frame_3)
        self.signup_con_pass.setGeometry(QtCore.QRect(40, 270, 201, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signup_con_pass.setFont(font)
        self.signup_con_pass.setStyleSheet("\n"
"background-color:#E8B510;\n"
"text-align:center;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:20px;\n"
"font-family:gotham;")
        self.signup_con_pass.setAlignment(QtCore.Qt.AlignCenter)
        self.signup_con_pass.setWordWrap(False)
        self.signup_con_pass.setObjectName("signup_con_pass")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(250, 280, 211, 21))
        self.lineEdit_4.setStyleSheet("background-color:white")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.register_2 = QtWidgets.QPushButton(self.frame_3)
        self.register_2.setGeometry(QtCore.QRect(200, 340, 141, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.register_2.setFont(font)
        self.register_2.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;")
        self.register_2.setObjectName("register_2")
                ###########################
        self.register_2.clicked.connect(self.insertdata)
        #############################
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.create_account.setText(_translate("MainWindow", "Create an Account"))
        self.signup_username.setText(_translate("MainWindow", "Username"))
        self.signup_pass.setText(_translate("MainWindow", "Password"))
        self.signup_con_pass.setText(_translate("MainWindow", "Confirm Password"))
        self.register_2.setText(_translate("MainWindow", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = registration_form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
