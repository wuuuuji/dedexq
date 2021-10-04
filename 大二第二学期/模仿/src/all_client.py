from PyQt5.QtWidgets import QWidget


from ui.ui_all_client import Ui_all_client


class AllClientWindow(QWidget, Ui_all_client):
    def __init__(self, parent=None):
        super(AllClientWindow, self).__init__()
        self.setupUi(self)