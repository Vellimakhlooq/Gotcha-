# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
#from signup import  Signup_MainWindow
from PyQt5.QtWidgets import QMessageBox
from project import Ui_project
import sqlite3
from signup import registration_form
class login_Ui_login(object):
     def insertData(self):
            username= self.lineEdit.text()
            
            password=self.lineEdit_3.text()
            cpassword=self.lineEdit_4.text()
            if not username:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Wrong username or password')
                msg.setWindowTitle("Error")
                msg.exec_()
            elif password != cpassword:

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Wrong username or password')
                msg.setWindowTitle("Error")
                msg.exec_()
            

            connection=sqlite3.connect("login_gotcha.db")
            connection.execute("INSERT INTO USERS VALUES(?,?)",(username,password))
            connection.commit()
            connection.close()
            print("Regsitered successfully")
     def nextWindow(self):
        print("login clicked")
        self.window=QtWidgets.QMainWindow()
        self.ui =Ui_project()
        self.ui.setupUi(self.window)
        login.hide()
        self.window.show()
     def error(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('Wrong username or password')
        msg.setWindowTitle("Error")
        msg.exec_()
     def loginCheck(self):
        username =self.lineEdit.text()
        password =self.lineEdit_2.text()
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
        else:
            connection=sqlite3.connect("login_gotcha.db")
            result = connection.execute("SELECT * FROM USERS WHERE USERNAME = ? AND PASSWORD =?",(username,password))
            if(len(result.fetchall()) > 0):
                print("user found")
                self.nextWindow()

            else:
                
                print("user not found")
                self.error()

     def signupCheck(self):
        print("signup button clicked")
        self.window=QtWidgets.QMainWindow()
        self.ui =registration_form()
        self.ui.setupUi(self.window)
        #login.hide()
        self.window.show()
     def setupUi(self, login):
        login.setObjectName("login")
        login.resize(552, 475)
        login.setStyleSheet("background-color:black;")
        self.centralwidget = QtWidgets.QWidget(login)
        self.centralwidget.setObjectName("centralwidget")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(70, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.username.setFont(font)
        self.username.setStyleSheet("\n"
"background-color:#E8B510;\n"
"text-align:center;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:20px;\n"
"font-family:gotham;")
        self.username.setAlignment(QtCore.Qt.AlignCenter)
        self.username.setWordWrap(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(70, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setStyleSheet("\n"
"background-color:#E8B510;\n"
"text-align:center;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:20px;\n"
"font-family:gotham;")
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(230, 189, 211, 21))
        self.lineEdit.setStyleSheet("background-color:white")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(230, 270, 211, 20))
        self.lineEdit_2.setStyleSheet("background-color:white")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.username_2 = QtWidgets.QLabel(self.centralwidget)
        self.username_2.setGeometry(QtCore.QRect(150, 50, 251, 71))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.username_2.setFont(font)
        self.username_2.setStyleSheet("background-color:#E8B510;\n"
"padding:10px;\n"
"border-radius:28px;\n"
"color:black;\n"
"font-size:50px;\n"
"font-family:gotham;")
        self.username_2.setAlignment(QtCore.Qt.AlignCenter)
        self.username_2.setWordWrap(False)
        self.username_2.setObjectName("username_2")
        self.login_2 = QtWidgets.QPushButton(self.centralwidget)
        self.login_2.setGeometry(QtCore.QRect(210, 330, 101, 41))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.login_2.setFont(font)
        self.login_2.setStyleSheet("background-color:#E8B510;\n"
"padding:1px;\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:25px;\n"
"font-family:gotham;")
        self.login_2.setObjectName("login_2")
        #############################
        self.login_2.clicked.connect(self.loginCheck)
        ##########################
        self.signup = QtWidgets.QPushButton(self.centralwidget)
        self.signup.setGeometry(QtCore.QRect(220, 380, 81, 31))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.signup.setFont(font)
        self.signup.setStyleSheet("background-color:#E8B510;\n"
"\n"
"border-radius:10px;\n"
"color:black;\n"
"font-size:18px;\n"
"font-family:gotham;")
        self.signup.setObjectName("signup")
        ############
        self.signup.clicked.connect(self.signupCheck)
        ##############
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 9, 531, 431))
        self.frame.setStyleSheet("background-color:#E8B510;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 9, 511, 411))
        self.frame_2.setStyleSheet("background-color:black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(200, 110, 121, 20))
        font = QtGui.QFont()
        font.setFamily("gotham")
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color:black;\n"
"color:#E8B510;\n"
"font-family:gotham;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.frame.raise_()
        self.username.raise_()
        self.password.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.username_2.raise_()
        self.login_2.raise_()
        self.signup.raise_()
        login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(login)
        self.statusbar.setObjectName("statusbar")
        login.setStatusBar(self.statusbar)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

     def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Gotcha!"))
        self.username.setText(_translate("login", "Username"))
        self.password.setText(_translate("login", "Password"))
        self.username_2.setText(_translate("login", "Gotcha!"))
        self.login_2.setText(_translate("login", "Login"))
        self.signup.setText(_translate("login", "Signup"))
        self.label.setText(_translate("login", "Login Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = QtWidgets.QMainWindow()
    ui = login_Ui_login()
    ui.setupUi(login)
    login.show()
    sys.exit(app.exec_())
