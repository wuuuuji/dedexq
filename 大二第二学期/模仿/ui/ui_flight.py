from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_flight(object):
    def setupUI(self, flight):
        flight.setObjectName("flight")
        flight.resize(391, 283)
        self.gridLayout_2 = QtWidgets.QGridLayout(flight)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # 航班编号
        self.label = QtWidgets.QLabel(flight)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.id = QtWidgets.QLineEdit(flight)
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 0, 1, 1, 1)

        # 航班名称
        self.label_2 = QtWidgets.QLabel(flight)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 2, 1, 1)
        self.name = QtWidgets.QLineEdit(flight)
        self.name.setObjectName("name")
        self.gridLayout_2.addWidget(self.name, 0, 3, 1, 1)

        # 起始地
        self.label_3 = QtWidgets.QLabel(flight)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)
        self.start = QtWidgets.QLineEdit(flight)
        self.start.setObjectName("start")
        self.gridLayout_2.addWidget(self.start, 1, 1, 1, 1)

        # 目的地
        self.label_4 = QtWidgets.QLabel(flight)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 2, 1, 1)
        self.end = QtWidgets.QLineEdit(flight)
        self.end.setObjectName("end")
        self.gridLayout_2.addWidget(self.end, 1, 3, 1, 1)

        # 经济舱数量
        self.label_5 = QtWidgets.QLabel(flight)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.class1count = QtWidgets.QLineEdit(flight)
        self.class1count.setObjectName("class1count")
        self.gridLayout_2.addWidget(self.class1count, 2, 1, 1, 1)

        # 经济舱价格
        self.label_6 = QtWidgets.QLabel(flight)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.class1price = QtWidgets.QLineEdit(flight)
        self.class1price.setObjectName("class1price")
        self.gridLayout_2.addWidget(self.class1price, 2, 3, 1, 1)

        # 商务舱数量
        self.label_7 = QtWidgets.QLabel(flight)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)
        self.class2count = QtWidgets.QLineEdit(flight)
        self.class2count.setObjectName("class2count")
        self.gridLayout_2.addWidget(self.class2count, 3, 1, 1, 1)

        # 商务舱价格
        self.label_8 = QtWidgets.QLabel(flight)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 2, 1, 1)
        self.class2price = QtWidgets.QLineEdit(flight)
        self.class2price.setObjectName("class2price")
        self.gridLayout_2.addWidget(self.class2price, 3, 3, 1, 1)

        # 头等舱数量
        self.label_9 = QtWidgets.QLabel(flight)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 4, 0, 1, 1)
        self.class3count = QtWidgets.QLineEdit(flight)
        self.class3count.setObjectName("class3count")
        self.gridLayout_2.addWidget(self.class3count, 4, 1, 1, 1)

        # 头等舱价格
        self.label_10 = QtWidgets.QLabel(flight)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 4, 2, 1, 1)
        self.class3price = QtWidgets.QLineEdit(flight)
        self.class3price.setObjectName("class3price")
        self.gridLayout_2.addWidget(self.class3price, 4, 3, 1, 1)

        # 航班时间
        self.label_11 = QtWidgets.QLabel(flight)
        self.label_11.setObjectName("label_11")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.gridLayout_2.addWidget(self.label_11, 5, 0, 1, 2)
        self.firmtime = QtWidgets.QDateTimeEdit(flight)
        self.firmtime.setObjectName("firmtime")
        self.gridLayout_2.addWidget(self.firmtime, 5, 2, 1, 4)


        # 添加航班相信的大按钮
        self.add_flight = QtWidgets.QPushButton(flight)
        self.add_flight.setObjectName("add_flight")
        self.gridLayout_2.addWidget(self.add_flight, 6, 0, 1, 4)

        self.retranslateUi(flight)
        QtCore.QMetaObject.connectSlotsByName(flight)

    def retranslateUi(self, flight):
        _translate = QtCore.QCoreApplication.translate
        flight.setWindowTitle(_translate("flight", "添加航班"))
        self.label.setText(_translate("flight", "航班编号"))
        self.label_2.setText(_translate("flight", "航班名称"))
        self.label_3.setText(_translate("flight", "起始地"))
        self.label_4.setText(_translate("flight", "目的地"))
        self.label_5.setText(_translate("flight", "经济舱数量"))
        self.label_6.setText(_translate("flight", "经济舱价格"))
        self.label_7.setText(_translate("flight", "商务舱数量"))
        self.label_8.setText(_translate("flight", "商务舱价格"))
        self.label_9.setText(_translate("flight", "头等舱数量"))
        self.label_10.setText(_translate("flight", "头等舱价格"))
        self.label_11.setText(_translate("flight", "   航班时间"))
        self.add_flight.setText(_translate("flight", "添加航班信息"))
