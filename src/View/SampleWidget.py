from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSpinBox, QLabel, QPushButton
from PyQt5.QtCore import pyqtSlot


class SampleWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.parent = parent
        self._vbox_layout = QVBoxLayout(self)
        self.add_spinbox()
        self.even_odd_label()
        self.reset_button()

        self.parent.controller.change_amount(47)
        self.parent.model.amount_changed.connect(self.on_amount_changed)
        self.parent.model.even_odd_changed.connect(self.on_even_odd_changed)
        self.parent.model.enable_reset_changed.connect(self.on_enable_reset_changed)

    def add_spinbox(self):
        self._spinbox = QSpinBox()
        self._vbox_layout.addWidget(self._spinbox)
        self._spinbox.valueChanged.connect(self.parent.controller.change_amount)

    @pyqtSlot(int)
    def on_amount_changed(self, value):
        self._spinbox.setValue(value)

    def even_odd_label(self):
        self._even_odd_label = QLabel()
        self._vbox_layout.addWidget(self._even_odd_label)

    @pyqtSlot(str)
    def on_even_odd_changed(self, value):
        self._even_odd_label.setText(value)

    def reset_button(self):
        self._reset_button = QPushButton("Reset")
        self._vbox_layout.addWidget(self._reset_button)
        self._reset_button.clicked.connect(lambda: self.parent.controller.change_amount(0))

    @pyqtSlot(bool)
    def on_enable_reset_changed(self, value):
        self._reset_button.setEnabled(value)
