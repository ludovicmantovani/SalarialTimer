from PySide2.QtWidgets import QApplication, QWidget


class TimeClockWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TimeClockWidget")


if __name__ == '__main__':
    win = QApplication()
    app = TimeClockWidget()
    app.show()
    win.exec_()
