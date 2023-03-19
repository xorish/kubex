# -*- coding: utf-8 -*-
import time

# Form implementation generated from reading ui file 'consent.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
import sys
path = os.path.dirname(os.path.abspath(sys.argv[0]))
file = open(f"{path}/temp/temp_buff_pvc_edit_cmd", "r")
res=file.read().split("#")
file.close()
pvc=res[1]
password=res[2]
user=res[3]
ip=res[4]

class Ui_MainWindow(object):

    def yesx(self):

        kube_cmd=f'/home/{user}/bin/kubectl apply -f ~/temp_pvc.json'
        ssh_cmd_file=f"sshpass -p {password} scp -o StrictHostKeyChecking=no {path}/temp_pvc.json  {user}@{ip}:~/ "
        ssh_cmd_kube=f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {user}@{ip} '{kube_cmd}' "
        ssh_cmd_rm = f"sshpass -p {password} ssh -o StrictHostKeyChecking=no {user}@{ip} 'rm ~/temp_pvc.json' "
        os.system(ssh_cmd_file)
        os.system(ssh_cmd_kube)
        os.system(ssh_cmd_rm)

        time.sleep(1)
        sys.exit()
    def nox(self):

        sys.exit()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 221)
        MainWindow.setStyleSheet("background-color: rgb(1,1,1);\n"
"color: rgb(198, 70, 0);\n"
"font: 11pt \"Ubuntu\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 120, 471, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yes.sizePolicy().hasHeightForWidth())
        self.yes.setSizePolicy(sizePolicy)
        self.yes.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.yes.setFlat(True)
        self.yes.setObjectName("yes")
        self.horizontalLayout.addWidget(self.yes)
        spacerItem = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.no = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.no.sizePolicy().hasHeightForWidth())
        self.no.setSizePolicy(sizePolicy)
        self.no.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.no.setFlat(True)
        self.no.setObjectName("no")
        self.horizontalLayout.addWidget(self.no)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 19, 621, 71))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setStyleSheet("font: 13pt \"Ubuntu\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.yes.clicked.connect(lambda : self.yesx())
        self.no.clicked.connect(lambda : self.nox())
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"PVC-Update ({pvc})"))
        self.yes.setText(_translate("MainWindow", "Yes"))
        self.no.setText(_translate("MainWindow", "No"))
        self.label.setText(_translate("MainWindow", f"Are you sure to update PVC\n'{pvc}' ?"))
def main():

 app = QtWidgets.QApplication(sys.argv)
 w = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(w)
 w.show()
 sys.exit(app.exec_())
main()