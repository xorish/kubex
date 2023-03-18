# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'watch_disp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

path = os.path.dirname(os.path.abspath(sys.argv[0]))

file = open(f"{path}/temp/temp_buff_port_forward", "r")
cmd=file.read().split("#")
file.close()
print(cmd)
svc=cmd[1]
cmd=cmd[0]
class Ui_MainWindow(object):
    def dataReady(self):
        cursor = self.disp.textCursor()
        cursor.movePosition(cursor.End)

        cursor.insertText(
            str(self.process.readAll().data().decode()))


    def callProgram(self):

        self.process.start("/bin/bash", ["-c",f"{cmd}"])
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(496,207)
        MainWindow.setStyleSheet("background-color: rgb(1,1,1);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.disp = QtWidgets.QTextBrowser(self.centralwidget)
        self.disp.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(38, 162, 105);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 2px solid rgb(198, 70, 0)\n"
"")
        self.disp.setFrameShape(QtWidgets.QFrame.Box)
        self.disp.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.disp.setReadOnly(False)
        self.disp.setObjectName("disp")
        self.verticalLayout.addWidget(self.disp)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.process=QtCore.QProcess()
        self.process.readyRead.connect(self.dataReady)
        self.callProgram()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        title="Description"+" "+f"({svc})"
        MainWindow.setWindowTitle(_translate("MainWindow", title))
def main():
 import sys
 app = QtWidgets.QApplication(sys.argv)
 w = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(w)
 w.show()
 sys.exit(app.exec_())
main()