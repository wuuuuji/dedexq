from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_record:
    def setupUi(self, record):
        record.setObjectName("record")
        record.resize(711, 535)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(record)  # 垂直布局
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()  # 水平布局
        self.horizontalLayout.setContentsMargins(-1, 8, -1, 8)  # 设置左侧、顶部、右侧和底部边距
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 姓名
        self.label = QtWidgets.QLabel(record)
        self.label.setMinimumSize(QtCore.QSize(112, 12))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name = QtWidgets.QLabel(record)
        self.name.setText("")
        self.name.setObjectName("name")
        self.horizontalLayout.addWidget(self.name)

        # 证件号码
        self.label_2 = QtWidgets.QLabel(record)
        self.label_2.setMinimumSize(QtCore.QSize(112, 0))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.id = QtWidgets.QLabel(record)
        self.id.setText("")
        self.id.setObjectName("id")
        self.horizontalLayout.addWidget(self.id)

        # 电话
        self.label_5 = QtWidgets.QLabel(record)
        self.label_5.setMinimumSize(QtCore.QSize(112, 0))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.phone = QtWidgets.QLabel(record)
        self.phone.setText("")
        self.phone.setObjectName("phone")
        self.horizontalLayout.addWidget(self.phone)

        self.verticalLayout_2.addLayout(self.horizontalLayout)  # 将水平布局加入到垂直布局
        self.table = QtWidgets.QTableView(record)
        self.table.setObjectName("table")
        self.verticalLayout_2.addWidget(self.table)
        self.retranslateUi(record)
        QtCore.QMetaObject.connectSlotsByName(record)

    def retranslateUi(self, record):
        _translate = QtCore.QCoreApplication.translate
        record.setWindowTitle(_translate("record", "查询订单"))
        self.label.setText(_translate("record", "姓名："))
        self.label_2.setText(_translate("record", "证件号码："))
        self.label_5.setText(_translate("record", "电话："))
