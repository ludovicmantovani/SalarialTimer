from PySide2.QtWidgets import QApplication, QWidget


class TimeClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TimeClockWidget")
        self.setup_ui()

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        pass

    def create_layouts(self):
        pass

    def modify_widgets(self):
        pass

    def add_widgets_to_layouts(self):
        pass

    def setup_connections(self):
        pass


if __name__ == '__main__':
    win = QApplication()
    app = TimeClockWidget()
    app.show()
    win.exec_()
