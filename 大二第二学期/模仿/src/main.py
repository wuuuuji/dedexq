import cgitb
import sys

from PyQt5 import QtSql, QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from src import create, FlightWindow, ClientWindow, RecordWindow, AllClientWindow, \
    PriceWindow, query_flight

'''
create是在database.py中的
'''
from ui.ui_main import ui_MainWindow


class MainWindow(QMainWindow, ui_MainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.setupUi(self)  # 设置主窗口
        self.open()
        self.flight_window = FlightWindow()  # 添加航班
        self.client_window = ClientWindow()  # 添加客户
        self.record_window = RecordWindow()  # 查询订单
        self.all_client_window = AllClientWindow()  # 查询客户
        self.price_window = PriceWindow()

        self.table.set_price(self.price)

        self.on_query_flight_clicked()

    def open(self):  # 添加一个sqlite数据库连接并打开
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        #  QSQLITE是SQLite对应的驱动名
        db.setDatabaseName('flight.db')
        # 创建数据库，名字为flight.db
        if not db.open():
            QMessageBox.critical(self, "数据库错误", "无法打开sqlite数据库", QMessageBox.Ok, QMessageBox.Ok)
            quit(1)
        create()

    def price(self, row):
        flight_id = self.table.model().index(row, 0).data()
        flight_name = self.table.model().index(row, 1).data()
        start = self.table.model().index(row, 2).data()
        end = self.table.model().index(row, 3).data()

        self.price_window.show_info(flight_id, flight_name, start, end)
        self.price_window.show()

    @pyqtSlot()
    # 查询航班按钮
    def on_query_flight_clicked(self):

        flight_id = self.flight_no.text()
        flight_name = self.flight_name.text()
        start = self.start.text()
        end = self.end.text()
        # 下面是显示表
        model = query_flight(flight_id, flight_name, start, end)
        self.table.setModel(model)

    @pyqtSlot()
    # 添加航班按钮的反应
    def on_add_flight_clicked(self):
        # 显示窗口
        self.flight_window.show()

    @pyqtSlot()
    # 添加客户按钮的反应
    def on_add_client_clicked(self):
        # 显示窗口
        self.client_window.show()

    @pyqtSlot()
    # 查询订单按钮的反应
    def on_query_record_clicked(self):
        # 显示窗口
        self.record_window.show()

    @pyqtSlot()
    # 查询所有顾客
    def on_query_client_clicked(self):
        # 显示窗口
        self.all_client_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # ↑每一pyqt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    welcome = MainWindow(app)
    welcome.show()
    app.exec_()
    sys.exit(app.exec_())
