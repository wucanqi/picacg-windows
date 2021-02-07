# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'user.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_User(object):
    def setupUi(self, User):
        User.setObjectName("User")
        User.resize(801, 488)
        User.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout_2 = QtWidgets.QGridLayout(User)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(User)
        self.stackedWidget.setObjectName("stackedWidget")
        self.gridLayout_2.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon = QtWidgets.QLabel(User)
        self.icon.setEnabled(True)
        self.icon.setMinimumSize(QtCore.QSize(200, 200))
        self.icon.setMaximumSize(QtCore.QSize(200, 200))
        self.icon.setStyleSheet("background: transparent;")
        self.icon.setText("")
        self.icon.setScaledContents(True)
        self.icon.setObjectName("icon")
        self.verticalLayout.addWidget(self.icon)
        self.exp = QtWidgets.QLabel(User)
        self.exp.setMaximumSize(QtCore.QSize(200, 16777215))
        self.exp.setObjectName("exp")
        self.verticalLayout.addWidget(self.exp)
        self.level = QtWidgets.QLabel(User)
        self.level.setMaximumSize(QtCore.QSize(200, 16777215))
        self.level.setObjectName("level")
        self.verticalLayout.addWidget(self.level)
        self.name = QtWidgets.QLabel(User)
        self.name.setMaximumSize(QtCore.QSize(200, 16777215))
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sign = QtWidgets.QLabel(User)
        self.sign.setMinimumSize(QtCore.QSize(0, 0))
        self.sign.setMaximumSize(QtCore.QSize(100, 16777215))
        self.sign.setObjectName("sign")
        self.horizontalLayout.addWidget(self.sign)
        self.signButton = QtWidgets.QPushButton(User)
        self.signButton.setEnabled(False)
        self.signButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.signButton.setObjectName("signButton")
        self.horizontalLayout.addWidget(self.signButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(User)
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(User)
        self.signButton.clicked.connect(User.Sign)
        QtCore.QMetaObject.connectSlotsByName(User)

    def retranslateUi(self, User):
        _translate = QtCore.QCoreApplication.translate
        User.setWindowTitle(_translate("User", "Form"))
        self.exp.setText(_translate("User", "exp"))
        self.level.setText(_translate("User", "level:"))
        self.name.setText(_translate("User", "name"))
        self.sign.setText(_translate("User", "sign:"))
        self.signButton.setText(_translate("User", "已签到"))