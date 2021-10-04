from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from ui.ui_client import Ui_client

class ClientWindow(QWidget, Ui_client):
    def __init__(self, parent=None):
        super(ClientWindow, self).__init__()
        self.setupUi(self)