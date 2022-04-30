import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from src.window import Window


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
