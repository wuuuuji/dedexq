from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QMessageBox

from src import *
from ui.ui_flight import Ui_flight

class FlightWindow(QWidget,Ui_flight):
    def __init__(self, parent=None):
        super(FlightWindow, self).__init__()
        self.setupUI(self)