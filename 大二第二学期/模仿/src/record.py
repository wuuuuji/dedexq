from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QMessageBox

from ui.ui_record import Ui_record

class RecordWindow(QWidget, Ui_record):
    def __init__(self, parent=None):
        super(RecordWindow, self).__init__()
        self.setupUi(self)
