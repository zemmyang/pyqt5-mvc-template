from PyQt5.QtWidgets import QMainWindow

from .SampleWidget import SampleWidget


class MainView(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()

        self.model = model
        self.controller = controller

        self._main_widget = SampleWidget(self)
        self.setCentralWidget(self._main_widget)
