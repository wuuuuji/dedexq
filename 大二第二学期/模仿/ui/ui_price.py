from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_price(object):
    def setupUi(self, price):
        price.setObjectName("price")
        price.resize(333, 173)
        self.gridLayout_2 = QtWidgets.QGridLayout(price)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # 航班编号
        self.label_4 = QtWidgets.QLabel(price)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 1, 1, 1)
        self.flight_id = QtWidgets.QLabel(price)
        self.flight_id.setText("")
        self.flight_id.setObjectName("flight_id")
        self.gridLayout_2.addWidget(self.flight_id, 0, 2, 1, 1)

        # 航班名称
        self.label_6 = QtWidgets.QLabel(price)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 0, 3, 1, 1)
        self.flight_name = QtWidgets.QLabel(price)
        self.flight_name.setText("")
        self.flight_name.setObjectName("flight_name")
        self.gridLayout_2.addWidget(self.flight_name, 0, 4, 1, 1)

        # 起始地
        self.label_8 = QtWidgets.QLabel(price)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 1, 1, 1, 1)
        self.start = QtWidgets.QLabel(price)
        self.start.setText("")
        self.start.setObjectName("start")
        self.gridLayout_2.addWidget(self.start, 1, 2, 1, 1)

        # 目的地
        self.label_10 = QtWidgets.QLabel(price)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 1, 3, 1, 1)
        self.end = QtWidgets.QLabel(price)
        self.end.setText("")
        self.end.setObjectName("end")
        self.gridLayout_2.addWidget(self.end, 1, 4, 1, 1)

        # 经济舱数量
        self.label = QtWidgets.QLabel(price)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 1, 1, 1)
        self.class1count = QtWidgets.QLabel(price)
        self.class1count.setText("")
        self.class1count.setObjectName("class1count")
        self.gridLayout_2.addWidget(self.class1count, 3, 2, 1, 1)

        # 经济舱价格
        self.label_5 = QtWidgets.QLabel(price)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)
        self.class1price = QtWidgets.QLineEdit(price)
        self.class1price.setObjectName("class1price")
        self.gridLayout_2.addWidget(self.class1price, 3, 4, 1, 1)

        # 商务舱数量
        self.label_2 = QtWidgets.QLabel(price)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)
        self.class2count = QtWidgets.QLabel(price)
        self.class2count.setText("")
        self.class2count.setObjectName("class2count")
        self.gridLayout_2.addWidget(self.class2count, 4, 2, 1, 1)

        # 商务舱价格
        self.label_7 = QtWidgets.QLabel(price)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 4, 3, 1, 1)
        self.class2price = QtWidgets.QLineEdit(price)
        self.class2price.setObjectName("class2price")
        self.gridLayout_2.addWidget(self.class2price, 4, 4, 1, 1)

        # 头等舱数量
        self.label_3 = QtWidgets.QLabel(price)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 1, 1, 1)
        self.class3count = QtWidgets.QLabel(price)
        self.class3count.setText("")
        self.class3count.setObjectName("class3count")
        self.gridLayout_2.addWidget(self.class3count, 5, 2, 1, 1)

        # 头等舱价格
        self.label_9 = QtWidgets.QLabel(price)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 5, 3, 1, 1)
        self.class3price = QtWidgets.QLineEdit(price)
        self.class3price.setObjectName("class3price")
        self.gridLayout_2.addWidget(self.class3price, 5, 4, 1, 1)

        #
        self.modify_price = QtWidgets.QPushButton(price)
        self.modify_price.setObjectName("modify_price")
        self.gridLayout_2.addWidget(self.modify_price, 6, 1, 1, 4)


        self.retranslateUi(price)
        QtCore.QMetaObject.connectSlotsByName(price)

    def retranslateUi(self, price):
        _translate = QtCore.QCoreApplication.translate
        price.setWindowTitle(_translate("price", "Form"))
        self.label_4.setText(_translate("price", "航班编号"))
        self.label_6.setText(_translate("price", "航班名称"))
        self.label_8.setText(_translate("price", "起始地"))
        self.label_10.setText(_translate("price", "目的地"))
        self.label.setText(_translate("price", "经济舱数量"))
        self.label_5.setText(_translate("price", "经济舱价格"))
        self.label_2.setText(_translate("price", "商务舱数量"))
        self.label_7.setText(_translate("price", "商务舱价格"))
        self.label_3.setText(_translate("price", "头等舱数量"))
        self.label_9.setText(_translate("price", "头等舱价格"))
        self.modify_price.setText(_translate("price", "修改航班"))
