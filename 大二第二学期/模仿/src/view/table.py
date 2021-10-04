from PyQt5.QtWidgets import QTableView

class MyTableView(QTableView):
    def __init__(self, parent=None):
        super(MyTableView, self).__init__(parent)

    def set_price(self, price):
        self.price = price

    def mouseDoubleClickEvent(self, event):  # 双击事件
        QTableView.mouseDoubleClickEvent(self, event)
        pos = event.pos()
        item = self.indexAt(pos)
        if item:
            print("item clicked at ", item.row(), " ", item.column())

        if item.column() == 0 and self.price:
            self.price(item.row())
        elif self.buy:
            self.buy(item.row())