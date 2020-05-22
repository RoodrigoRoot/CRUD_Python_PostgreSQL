# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

import utils
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 289)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 301, 211))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 67, 17))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.leUser = QtWidgets.QLineEdit(self.groupBox)
        self.leUser.setGeometry(QtCore.QRect(100, 40, 161, 31))
        self.leUser.setObjectName("leUser")
        self.lePasswd = QtWidgets.QLineEdit(self.groupBox)
        self.lePasswd.setGeometry(QtCore.QRect(100, 110, 161, 31))
        self.lePasswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lePasswd.setObjectName("lePasswd")
        self.pbEnter = QtWidgets.QPushButton(Dialog)
        self.pbEnter.setGeometry(QtCore.QRect(100, 230, 101, 41))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Downloads/ui.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pbEnter.setIcon(icon)
        self.pbEnter.setAutoDefault(False)
        self.pbEnter.setObjectName("pbEnter")
        self.pbEnter.clicked.connect(self.get_user_pass)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("AgroTech", "AgroTech"))
        self.groupBox.setTitle(_translate("Dialog", "Inicio de Sesión"))
        self.label.setText(_translate("Dialog", "Usuario: "))
        self.label_2.setText(_translate("Dialog", "Clave: "))
        self.pbEnter.setText(_translate("Dialog", "Entrar"))

    def get_user_pass(self):
        if utils.file_exists(utils.globlas.INIT_FILE):
            data = utils.get_data_json(utils.globlas.INIT_FILE)
            con = utils.get_connection_db(data)
            passwd =self.lePasswd.text()
            user = self.leUser.text()
            if utils.db.login(con, user, passwd):
                self.leUser.setText("")
                self.lePasswd.setText("")
                #new_user = utils.UserMethods.create_user()
                #utils.UserMethods.insert_user(con, new_user)
                utils.db.close_db(con)
            else:
                print("Problemas en conexión")




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
