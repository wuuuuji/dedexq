from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_all_client(object):
    def setupUi(self, all_client):
        all_client.setObjectName("all_client")
        all_client.resize(340, 321)
        self.verticalLayout = QtWidgets.QVBoxLayout(all_client)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QTableView(all_client)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)

        self.retranslateUi(all_client)
        QtCore.QMetaObject.connectSlotsByName(all_client)


    def retranslateUi(self, all_client):
        _translate = QtCore.QCoreApplication.translate
        all_client.setWindowTitle(_translate("all_client", "查询客户"))