import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.window import UI_MainWindow


class Window(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
