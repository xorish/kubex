# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

path = os.path.dirname(os.path.abspath(sys.argv[0]))

class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1082, 990)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1082, 818))
        MainWindow.setMaximumSize(QtCore.QSize(1082, 990))
        MainWindow.setStyleSheet("background-color: rgb(36, 31, 49);\n"
"background-color: rgb(14, 14, 14);\n"
"color: rgb(198, 70, 0);\n"
"font: 11pt \"Ubuntu\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pod_combo = QtWidgets.QComboBox(self.centralwidget)
        self.pod_combo.setGeometry(QtCore.QRect(50, 420, 381, 41))
        self.pod_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.pod_combo.setEditable(False)
        self.pod_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.pod_combo.setObjectName("pod_combo")
        self.container_combo = QtWidgets.QComboBox(self.centralwidget)
        self.container_combo.setGeometry(QtCore.QRect(40, 620, 471, 41))
        self.container_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.container_combo.setEditable(False)
        self.container_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.container_combo.setObjectName("container_combo")
        self.svc_combo = QtWidgets.QComboBox(self.centralwidget)
        self.svc_combo.setGeometry(QtCore.QRect(570, 790, 471, 41))
        self.svc_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.svc_combo.setEditable(False)
        self.svc_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.svc_combo.setObjectName("svc_combo")
        self.ssh_combo = QtWidgets.QComboBox(self.centralwidget)
        self.ssh_combo.setGeometry(QtCore.QRect(40, 160, 471, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ssh_combo.sizePolicy().hasHeightForWidth())
        self.ssh_combo.setSizePolicy(sizePolicy)
        self.ssh_combo.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.ssh_combo.setEditable(False)
        self.ssh_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.ssh_combo.setObjectName("ssh_combo")
        self.watch_pods = QtWidgets.QPushButton(self.centralwidget)
        self.watch_pods.setGeometry(QtCore.QRect(370, 470, 151, 41))
        self.watch_pods.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.watch_pods.setFlat(True)
        self.watch_pods.setObjectName("watch_pods")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1081, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.settings = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings.sizePolicy().hasHeightForWidth())
        self.settings.setSizePolicy(sizePolicy)
        self.settings.setStyleSheet("background-color: rgb(0,0,0);")
        self.settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("settings-128.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings.setIcon(icon)
        self.settings.setIconSize(QtCore.QSize(40, 40))
        self.settings.setFlat(True)
        self.settings.setObjectName("settings")
        self.horizontalLayout.addWidget(self.settings)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setStyleSheet("font: 24pt \"URW Gothic\";\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.info = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info.sizePolicy().hasHeightForWidth())
        self.info.setSizePolicy(sizePolicy)
        self.info.setStyleSheet("background-color: rgb(0,0,0);")
        self.info.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.info.setIcon(icon1)
        self.info.setIconSize(QtCore.QSize(40, 40))
        self.info.setFlat(True)
        self.info.setObjectName("info")
        self.horizontalLayout.addWidget(self.info)
        spacerItem1 = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(9, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 60, 1081, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.local = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.local.sizePolicy().hasHeightForWidth())
        self.local.setSizePolicy(sizePolicy)
        self.local.setObjectName("local")
        self.horizontalLayout_2.addWidget(self.local)
        self.remote = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.remote.sizePolicy().hasHeightForWidth())
        self.remote.setSizePolicy(sizePolicy)
        self.remote.setObjectName("remote")
        self.horizontalLayout_2.addWidget(self.remote)
        self.svc_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.svc_filter.setGeometry(QtCore.QRect(570, 760, 471, 31))
        self.svc_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.svc_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.svc_filter.setObjectName("svc_filter")
        self.name_space_combo = QtWidgets.QComboBox(self.centralwidget)
        self.name_space_combo.setGeometry(QtCore.QRect(40, 290, 471, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_space_combo.sizePolicy().hasHeightForWidth())
        self.name_space_combo.setSizePolicy(sizePolicy)
        self.name_space_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.name_space_combo.setEditable(False)
        self.name_space_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.name_space_combo.setObjectName("name_space_combo")
        self.namespace_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.namespace_filter.setGeometry(QtCore.QRect(40, 260, 471, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.namespace_filter.sizePolicy().hasHeightForWidth())
        self.namespace_filter.setSizePolicy(sizePolicy)
        self.namespace_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.namespace_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.namespace_filter.setObjectName("namespace_filter")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 281, 17))
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(560, 730, 281, 17))
        self.label_10.setObjectName("label_10")
        self.service_description = QtWidgets.QPushButton(self.centralwidget)
        self.service_description.setGeometry(QtCore.QRect(570, 890, 471, 41))
        self.service_description.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.service_description.setFlat(True)
        self.service_description.setObjectName("service_description")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 350, 281, 17))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(20, 580, 281, 17))
        self.label_12.setObjectName("label_12")
        self.Execute = QtWidgets.QPushButton(self.centralwidget)
        self.Execute.setGeometry(QtCore.QRect(50, 470, 151, 41))
        self.Execute.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.Execute.setFlat(True)
        self.Execute.setObjectName("Execute")
        self.delete_pod = QtWidgets.QPushButton(self.centralwidget)
        self.delete_pod.setGeometry(QtCore.QRect(50, 520, 151, 41))
        self.delete_pod.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.delete_pod.setFlat(True)
        self.delete_pod.setObjectName("delete_pod")
        self.logs = QtWidgets.QPushButton(self.centralwidget)
        self.logs.setGeometry(QtCore.QRect(40, 670, 471, 41))
        self.logs.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.logs.setFlat(True)
        self.logs.setObjectName("logs")
        self.describe_pod = QtWidgets.QPushButton(self.centralwidget)
        self.describe_pod.setGeometry(QtCore.QRect(210, 470, 151, 41))
        self.describe_pod.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.describe_pod.setFlat(True)
        self.describe_pod.setObjectName("describe_pod")
        self.pod_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.pod_filter.setGeometry(QtCore.QRect(50, 390, 381, 31))
        self.pod_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.pod_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.pod_filter.setObjectName("pod_filter")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(10, 940, 1061, 41))
        self.status.setStyleSheet("font: 9pt \"Ubuntu Mono\";\n"
"color: rgb(42, 177, 23);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.status.setText("")
        self.status.setObjectName("status")
        self.node_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.node_filter.setGeometry(QtCore.QRect(570, 160, 381, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_filter.sizePolicy().hasHeightForWidth())
        self.node_filter.setSizePolicy(sizePolicy)
        self.node_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.node_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.node_filter.setObjectName("node_filter")
        self.node_combo = QtWidgets.QComboBox(self.centralwidget)
        self.node_combo.setGeometry(QtCore.QRect(570, 190, 381, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.node_combo.sizePolicy().hasHeightForWidth())
        self.node_combo.setSizePolicy(sizePolicy)
        self.node_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.node_combo.setEditable(False)
        self.node_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.node_combo.setObjectName("node_combo")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 220, 281, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(560, 120, 281, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(560, 360, 281, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setObjectName("label_14")
        self.node_describe = QtWidgets.QPushButton(self.centralwidget)
        self.node_describe.setGeometry(QtCore.QRect(570, 240, 151, 41))
        self.node_describe.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.node_describe.setFlat(True)
        self.node_describe.setObjectName("node_describe")
        self.node_cordon = QtWidgets.QPushButton(self.centralwidget)
        self.node_cordon.setGeometry(QtCore.QRect(730, 240, 151, 41))
        self.node_cordon.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.node_cordon.setFlat(True)
        self.node_cordon.setObjectName("node_cordon")
        self.node_delete = QtWidgets.QPushButton(self.centralwidget)
        self.node_delete.setGeometry(QtCore.QRect(890, 240, 151, 41))
        self.node_delete.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.node_delete.setFlat(True)
        self.node_delete.setObjectName("node_delete")
        self.node_top = QtWidgets.QPushButton(self.centralwidget)
        self.node_top.setGeometry(QtCore.QRect(570, 300, 181, 41))
        self.node_top.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.node_top.setFlat(True)
        self.node_top.setObjectName("node_top")
        self.pvc_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.pvc_filter.setGeometry(QtCore.QRect(570, 390, 381, 31))
        self.pvc_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.pvc_filter.setText("")
        self.pvc_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.pvc_filter.setObjectName("pvc_filter")
        self.pvc_combo = QtWidgets.QComboBox(self.centralwidget)
        self.pvc_combo.setGeometry(QtCore.QRect(570, 420, 381, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pvc_combo.sizePolicy().hasHeightForWidth())
        self.pvc_combo.setSizePolicy(sizePolicy)
        self.pvc_combo.setMaximumSize(QtCore.QSize(16777215, 2000))
        self.pvc_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.pvc_combo.setEditable(False)
        self.pvc_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.pvc_combo.setObjectName("pvc_combo")
        self.port_forward = QtWidgets.QPushButton(self.centralwidget)
        self.port_forward.setGeometry(QtCore.QRect(780, 840, 161, 41))
        self.port_forward.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.port_forward.setFlat(True)
        self.port_forward.setObjectName("port_forward")
        self.svc_port = QtWidgets.QLineEdit(self.centralwidget)
        self.svc_port.setGeometry(QtCore.QRect(570, 840, 201, 41))
        self.svc_port.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(38, 162, 105);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.svc_port.setAlignment(QtCore.Qt.AlignCenter)
        self.svc_port.setPlaceholderText("")
        self.svc_port.setObjectName("svc_port")
        self.top_pod = QtWidgets.QPushButton(self.centralwidget)
        self.top_pod.setGeometry(QtCore.QRect(210, 520, 311, 41))
        self.top_pod.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.top_pod.setFlat(True)
        self.top_pod.setObjectName("top_pod")
        self.deployment_combo = QtWidgets.QComboBox(self.centralwidget)
        self.deployment_combo.setGeometry(QtCore.QRect(40, 790, 471, 41))
        self.deployment_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.deployment_combo.setEditable(False)
        self.deployment_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.deployment_combo.setObjectName("deployment_combo")
        self.deployment_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.deployment_filter.setGeometry(QtCore.QRect(40, 760, 471, 31))
        self.deployment_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.deployment_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.deployment_filter.setObjectName("deployment_filter")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(20, 730, 281, 17))
        self.label_15.setObjectName("label_15")
        self.rollout_restart = QtWidgets.QPushButton(self.centralwidget)
        self.rollout_restart.setGeometry(QtCore.QRect(40, 840, 151, 41))
        self.rollout_restart.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.rollout_restart.setFlat(True)
        self.rollout_restart.setObjectName("rollout_restart")
        self.roll_out_status = QtWidgets.QPushButton(self.centralwidget)
        self.roll_out_status.setGeometry(QtCore.QRect(200, 840, 151, 41))
        self.roll_out_status.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.roll_out_status.setFlat(True)
        self.roll_out_status.setObjectName("roll_out_status")
        self.rollou_undo = QtWidgets.QPushButton(self.centralwidget)
        self.rollou_undo.setGeometry(QtCore.QRect(360, 840, 151, 41))
        self.rollou_undo.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.rollou_undo.setFlat(True)
        self.rollou_undo.setObjectName("rollou_undo")
        self.pv_combo = QtWidgets.QComboBox(self.centralwidget)
        self.pv_combo.setGeometry(QtCore.QRect(570, 590, 471, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pv_combo.sizePolicy().hasHeightForWidth())
        self.pv_combo.setSizePolicy(sizePolicy)
        self.pv_combo.setMaximumSize(QtCore.QSize(16777215, 2000))
        self.pv_combo.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(46, 194, 126);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)")
        self.pv_combo.setEditable(False)
        self.pv_combo.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.pv_combo.setObjectName("pv_combo")
        self.pv_filter = QtWidgets.QLineEdit(self.centralwidget)
        self.pv_filter.setGeometry(QtCore.QRect(570, 560, 471, 31))
        self.pv_filter.setStyleSheet("\n"
"font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(222, 221, 218);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.pv_filter.setAlignment(QtCore.Qt.AlignCenter)
        self.pv_filter.setObjectName("pv_filter")
        self.edit_deployment = QtWidgets.QPushButton(self.centralwidget)
        self.edit_deployment.setGeometry(QtCore.QRect(40, 890, 471, 41))
        self.edit_deployment.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.edit_deployment.setFlat(True)
        self.edit_deployment.setObjectName("edit_deployment")
        self.pvc_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pvc_edit.setGeometry(QtCore.QRect(570, 470, 201, 41))
        self.pvc_edit.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pvc_edit.setFlat(True)
        self.pvc_edit.setObjectName("pvc_edit")
        self.pvc_describe = QtWidgets.QPushButton(self.centralwidget)
        self.pvc_describe.setGeometry(QtCore.QRect(840, 470, 201, 41))
        self.pvc_describe.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pvc_describe.setFlat(True)
        self.pvc_describe.setObjectName("pvc_describe")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(560, 530, 281, 17))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setObjectName("label_16")
        self.pv_describe = QtWidgets.QPushButton(self.centralwidget)
        self.pv_describe.setGeometry(QtCore.QRect(840, 650, 201, 41))
        self.pv_describe.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pv_describe.setFlat(True)
        self.pv_describe.setObjectName("pv_describe")
        self.pv_edit = QtWidgets.QPushButton(self.centralwidget)
        self.pv_edit.setGeometry(QtCore.QRect(570, 650, 201, 41))
        self.pv_edit.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pv_edit.setFlat(True)
        self.pv_edit.setObjectName("pv_edit")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(640, 120, 401, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ready = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ready.sizePolicy().hasHeightForWidth())
        self.ready.setSizePolicy(sizePolicy)
        self.ready.setObjectName("ready")
        self.horizontalLayout_3.addWidget(self.ready)
        self.not_ready = QtWidgets.QRadioButton(self.horizontalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_ready.sizePolicy().hasHeightForWidth())
        self.not_ready.setSizePolicy(sizePolicy)
        self.not_ready.setObjectName("not_ready")
        self.horizontalLayout_3.addWidget(self.not_ready)
        self.node_status_bar = QtWidgets.QLabel(self.centralwidget)
        self.node_status_bar.setGeometry(QtCore.QRect(760, 300, 281, 41))
        self.node_status_bar.setStyleSheet("font: 12pt \"Ubuntu Mono\";\n"
"color: rgb(26, 95, 180);\n"
"background-color: rgb(14, 14, 2);\n"
"selection-background-color: rgb(206, 92, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"border: 1px solid rgb(165, 29, 45)\n"
"")
        self.node_status_bar.setText("")
        self.node_status_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.node_status_bar.setObjectName("node_status_bar")
        self.node_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.node_number.setGeometry(QtCore.QRect(963, 160, 81, 71))
        self.node_number.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.node_number.setDigitCount(4)
        self.node_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.node_number.setObjectName("node_number")
        self.clear_port = QtWidgets.QPushButton(self.centralwidget)
        self.clear_port.setGeometry(QtCore.QRect(950, 840, 91, 41))
        self.clear_port.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.clear_port.setFlat(True)
        self.clear_port.setObjectName("clear_port")
        self.pod_count = QtWidgets.QLCDNumber(self.centralwidget)
        self.pod_count.setGeometry(QtCore.QRect(440, 390, 81, 71))
        self.pod_count.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pod_count.setDigitCount(4)
        self.pod_count.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pod_count.setObjectName("pod_count")
        self.pvc_number = QtWidgets.QLCDNumber(self.centralwidget)
        self.pvc_number.setGeometry(QtCore.QRect(960, 390, 81, 71))
        self.pvc_number.setStyleSheet("border: 1px solid rgb(165, 29, 45)")
        self.pvc_number.setDigitCount(4)
        self.pvc_number.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.pvc_number.setObjectName("pvc_number")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.remote.setChecked(True)
        import main_function
        # import json
        # file = open(f'{path}/temp/ssh.json', 'r')
        # data = json.load(file)
        # file.close()
        # for i in data.keys():
        #     self.ssh_combo.addItem(f"{i} {data[i][0]}")

        self.process_settings = QtCore.QProcess()

        # self.process_ns_svc = QtCore.QProcess()
        # self.process_ns_po = QtCore.QProcess()
        # self.process_po_con = QtCore.QProcess()
        # self.process_node = QtCore.QProcess()
        # self.process_deployment = QtCore.QProcess()
        # self.process_pvc = QtCore.QProcess()
        # main_function.pro_ns_po(self)
        # main_function.pro_ns_svc(self)
        # main_function.pro_po_con(self)
        # main_function.pro_node_list(self)
        # main_function.pro_ns_deployment(self)
        # main_function.pro_ns_pvc_pv(self)
        self.settings.clicked.connect(lambda: main_function.settings(self))

        self.ssh_combo.currentIndexChanged.connect(lambda: main_function.start(self))
        self.name_space_combo.currentIndexChanged.connect(lambda: main_function.service_pod_deployment_pvc(self))
        self.pod_combo.currentIndexChanged.connect(lambda: main_function.container(self))
        self.pvc_combo.currentIndexChanged.connect(lambda : main_function.pv(self))

        self.remote.clicked.connect(lambda: main_function.start(self))
        self.local.clicked.connect(lambda: main_function.start(self))

        self.namespace_filter.textEdited.connect(lambda: main_function.namespace_filter(self))
        self.svc_filter.textEdited.connect(lambda: main_function.svc_filter(self))
        self.pod_filter.textEdited.connect(lambda: main_function.po_filter(self))
        self.node_filter.textEdited.connect(lambda : main_function.node_search_filter(self))
        self.svc_filter.textEdited.connect(lambda : main_function.svc_filter(self))
        self.deployment_filter.textEdited.connect(lambda : main_function.deployment_filetr(self))
        self.pvc_filter.textEdited.connect(lambda : main_function.pvc_filetr(self))
        self.pv_filter.textEdited.connect(lambda : main_function.pv_filetr(self))

        self.watch_pods.clicked.connect(lambda: main_function.watch_po(self))
        self.describe_pod.clicked.connect(lambda: main_function.pod_describe(self))
        self.logs.clicked.connect(lambda: main_function.po_logs(self))
        self.Execute.clicked.connect(lambda: main_function.excute_po_con(self))
        self.top_pod.clicked.connect(lambda: main_function.pod_top(self))
        self.delete_pod.clicked.connect(lambda : main_function.po_delete(self))

        self.ready.clicked.connect(lambda: main_function.node_ready_filter(self))
        self.not_ready.clicked.connect(lambda : main_function.node_not_ready_filter(self))
        self.node_describe.clicked.connect(lambda : main_function.node_describe(self))
        self.node_top.clicked.connect(lambda : main_function.node_top(self))

        self.service_description.clicked.connect(lambda : main_function.svc_describe(self))
        self.port_forward.clicked.connect(lambda : main_function.svc_port_forward(self))
        self.clear_port.clicked.connect(lambda : main_function.clear_port(self))

        self.edit_deployment.clicked.connect(lambda : main_function.deployment_edit(self))
        self.rollout_restart.clicked.connect(lambda : main_function.rollout_restart(self))
        self.roll_out_status.clicked.connect(lambda : main_function.rollout_status(self))
        self.rollou_undo.clicked.connect(lambda : main_function.rollout_undo(self))

        self.pvc_describe.clicked.connect(lambda : main_function.pvc_describe(self))
        self.pvc_edit.clicked.connect(lambda : main_function.pvc_edit(self))

        self.pv_describe.clicked.connect(lambda : main_function.pv_describe(self))
        self.pv_edit.clicked.connect(lambda : main_function.pv_edit(self))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.watch_pods.setText(_translate("MainWindow", "Watch Pods"))
        self.label.setText(_translate("MainWindow", "EAZY KUBE"))
        self.local.setText(_translate("MainWindow", "Local"))
        self.remote.setText(_translate("MainWindow", "Remote"))
        self.svc_filter.setPlaceholderText(_translate("MainWindow", "Search Service"))
        self.namespace_filter.setPlaceholderText(_translate("MainWindow", "Search Namespace"))
        self.label_8.setText(_translate("MainWindow", "Remote Server:"))
        self.label_10.setText(_translate("MainWindow", "Service:"))
        self.service_description.setText(_translate("MainWindow", "Describe"))
        self.label_11.setText(_translate("MainWindow", "Pods:"))
        self.label_12.setText(_translate("MainWindow", "Containers:"))
        self.Execute.setText(_translate("MainWindow", "Excecute"))
        self.delete_pod.setText(_translate("MainWindow", "Delete"))
        self.logs.setText(_translate("MainWindow", "Logs"))
        self.describe_pod.setText(_translate("MainWindow", "Describe"))
        self.pod_filter.setPlaceholderText(_translate("MainWindow", "Search Pod"))
        self.node_filter.setPlaceholderText(_translate("MainWindow", "Search Node"))
        self.label_9.setText(_translate("MainWindow", "Namespace:"))
        self.label_13.setText(_translate("MainWindow", "Nodes:"))
        self.label_14.setText(_translate("MainWindow", "PVC:"))
        self.node_describe.setText(_translate("MainWindow", "Describe"))
        self.node_cordon.setText(_translate("MainWindow", "Cordon"))
        self.node_delete.setText(_translate("MainWindow", "Force Delete"))
        self.node_top.setText(_translate("MainWindow", "Top (Resource Usage)"))
        self.pvc_filter.setPlaceholderText(_translate("MainWindow", "Search PVC"))
        self.port_forward.setText(_translate("MainWindow", "Port-Forward-Local"))
        self.top_pod.setText(_translate("MainWindow", "Top (Resource Usage)"))
        self.deployment_filter.setPlaceholderText(_translate("MainWindow", "Search Deployment"))
        self.label_15.setText(_translate("MainWindow", "Deployment:"))
        self.rollout_restart.setText(_translate("MainWindow", "Rollout Restart"))
        self.roll_out_status.setText(_translate("MainWindow", "Rollout Status"))
        self.rollou_undo.setText(_translate("MainWindow", "Rollout Undo"))
        self.pv_filter.setPlaceholderText(_translate("MainWindow", "Search PV"))
        self.edit_deployment.setText(_translate("MainWindow", "Edit"))
        self.pvc_edit.setText(_translate("MainWindow", "Edit"))
        self.pvc_describe.setText(_translate("MainWindow", "Describe"))
        self.label_16.setText(_translate("MainWindow", "PV:"))
        self.pv_describe.setText(_translate("MainWindow", "Describe"))
        self.pv_edit.setText(_translate("MainWindow", "Edit"))
        self.ready.setText(_translate("MainWindow", "Ready"))
        self.not_ready.setText(_translate("MainWindow", "Not-Ready"))
        self.clear_port.setText(_translate("MainWindow", "Clear Port"))

def appExec():
  import sys
  app = QtWidgets.QApplication(sys.argv)

  app.exec_()
  file = open(f"{path}/temp/flag", 'w')
  file.write('0')
  file.close()

def main():
 import sys
 app = QtWidgets.QApplication(sys.argv)
 w = QtWidgets.QMainWindow()
 ui = Ui_MainWindow()
 ui.setupUi(w)
 w.show()
 sys.exit(appExec())
main()