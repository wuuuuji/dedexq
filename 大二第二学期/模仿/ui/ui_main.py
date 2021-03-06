import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from src.view.table import MyTableView


class ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # 销毁MainWindow
        MainWindow.resize(1025, 772.5)  # 设置窗口大小(x,y)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        # addWidget 控件名，起始行，起始列，占用行，占用列

        # 航班编号
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 1, 1, 1)
        self.flight_no = QtWidgets.QLineEdit(self.centralwidget)
        self.flight_no.setObjectName("flight_no")
        self.gridLayout_3.addWidget(self.flight_no, 1, 2, 1, 1)

        # 航班名称
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 4, 1, 1)
        self.flight_name = QtWidgets.QLineEdit(self.centralwidget)
        self.flight_name.setObjectName("flight_name")
        self.gridLayout_3.addWidget(self.flight_name, 1, 5, 1, 1)

        # 起始地
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 1, 1, 1)
        self.start = QtWidgets.QLineEdit(self.centralwidget)
        self.start.setObjectName("start")
        self.gridLayout_3.addWidget(self.start, 2, 2, 1, 1)

        # 目的地
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 2, 4, 1, 1)
        self.end = QtWidgets.QLineEdit(self.centralwidget)
        self.end.setObjectName("end")
        self.gridLayout_3.addWidget(self.end, 2, 5, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 6, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()  # 水平布局
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)  # 设置左侧、顶部、右侧和底部边距
        self.horizontalLayout.setObjectName("horizontalLayout")

        # 添加航班
        self.add_flight = QtWidgets.QPushButton(self.centralwidget)
        self.add_flight.setObjectName("add_flight")
        self.horizontalLayout.addWidget(self.add_flight)
        # 添加客户
        self.add_client = QtWidgets.QPushButton(self.centralwidget)
        self.add_client.setObjectName("add_client")
        self.horizontalLayout.addWidget(self.add_client)
        # 查询订单
        self.query_record = QtWidgets.QPushButton(self.centralwidget)
        self.query_record.setObjectName("query_record")
        self.horizontalLayout.addWidget(self.query_record)
        # 查询客户
        self.query_client = QtWidgets.QPushButton(self.centralwidget)
        self.query_client.setObjectName("query_client")
        self.horizontalLayout.addWidget(self.query_client)

        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 8)

        # 查询订单
        self.query_flight = QtWidgets.QPushButton(self.centralwidget)
        self.query_flight.setObjectName("query_flight")
        self.gridLayout_3.addWidget(self.query_flight, 3, 0, 1, 8)

        # 最下面的窗口
        self.table = MyTableView(self.centralwidget)
        self.table.setObjectName("table")
        self.gridLayout_3.addWidget(self.table, 4, 0, 1, 8)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "航班熔断的航班管理系统"))
        self.label.setText(_translate("MainWindow", "航班编号"))
        self.label_2.setText(_translate("MainWindow", "航班名称"))
        self.label_4.setText(_translate("MainWindow", "起始地"))
        self.label_5.setText(_translate("MainWindow", "目的地"))
        self.add_flight.setText(_translate("MainWindow", "添加航班"))
        self.add_client.setText(_translate("MainWindow", "添加客户"))
        self.query_record.setText(_translate("MainWindow", "查询订单"))
        self.query_client.setText(_translate("MainWindow", "查询客户"))
        self.query_flight.setText(_translate("MainWindow", "查询航班"))

