from PySide2.QtWidgets import QApplication, QWidget, QGridLayout, QHBoxLayout, QLabel, QTimeEdit, QVBoxLayout, \
    QPushButton
from datetime import date

class TimeClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TimeClockWidget")
        self.buttons_setter = {}
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.modify_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        # Control part
        self.buttons_setter[QPushButton("Début de journée")] = QTimeEdit()
        self.buttons_setter[QPushButton("Début de pause")] = QTimeEdit()
        self.buttons_setter[QPushButton("Fin de pause")] = QTimeEdit()
        self.buttons_setter[QPushButton("Fin de journée")] = QTimeEdit()

    def modify_widgets(self):
        pass

    def create_layouts(self):
        self.main_layout = QVBoxLayout(self)

        # Control part
        self.cp_layout = QGridLayout()

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(QLabel(date.today().strftime("%A %d %B %Y")))
        self.main_layout.addWidget(QLabel(date.today().strftime("Semaine %W de %Y")))

        # Control part
        self.main_layout.addLayout(self.cp_layout)
        index = 0
        for btn, te in self.buttons_setter.items():
            self.cp_layout.addWidget(btn, index, 1, 1, 1)
            self.cp_layout.addWidget(te, index, 2, 1, 1)
            index +=1

    def setup_connections(self):
        for btn, te in self.buttons_setter.items():
            btn.clicked.connect(self.set_hour_by_btn)

    def set_hour_by_btn(self):
        te_current = self.buttons_setter[self.sender()]
        # TODO: Set current time te_current.setTime("")
        print("TODO: Set hour")


if __name__ == '__main__':
    win = QApplication()
    app = TimeClockWidget()
    app.show()
    win.exec_()
