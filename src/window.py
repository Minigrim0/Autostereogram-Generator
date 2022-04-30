from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMainWindow

import cv2

from src.ui_MainWindow import UI_MainWindow
from src.autostereogram import create_autoStereogram


class Window(QMainWindow, UI_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.result = None

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.LoadImage.clicked.connect(self.getImage)
        self.SaveImage.clicked.connect(self.getImage)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self)
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.ImagePreviewLabel.setPixmap(QPixmap(pixmap))
        self.resize(10, 10)

        self.result = create_autoStereogram(fname[0])

        if len(self.result.shape) < 3:
            frame = cv2.cvtColor(self.result, cv2.COLOR_GRAY2RGB)
        else:
            frame = cv2.cvtColor(self.result, cv2.COLOR_BGR2RGB)

        h, w = self.result.shape[:2]
        bytesPerLine = 3 * w
        qimage = QImage(
            frame.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

        self.ImageResultLabel.setPixmap(QPixmap(qimage))

    def save_result(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname is not None:
            cv2.imwrite(fname, 255 * self.result)
