from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QMainWindow

import cv2

from src.ui_MainWindow import Ui_Dialog
from src.autostereogram import create_autoStereogram


class Window(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.result = None
        self.current_preview_grascale = False

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.LoadImage.clicked.connect(self.getImage)
        self.SaveImage.clicked.connect(self.getImage)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self)
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.MapPreview.setPixmap(QPixmap(pixmap))

        self.current_preview_grascale = self.checkBox.isChecked()
        self.result = create_autoStereogram(fname[0], self.current_preview_grascale)

        h, w = self.result.shape[:2]
        if self.current_preview_grascale:
            bytesPerLine = w
            qimage = QImage(
                self.result.data, w, h, bytesPerLine, QImage.Format.Format_Grayscale8)
        else:
            bytesPerLine = 3 * w
            qimage = QImage(
                self.result.data, w, h, bytesPerLine, QImage.Format.Format_RGB888)

        self.ResultPreview.setPixmap(QPixmap(qimage))

    def save_result(self):
        fname = QFileDialog.getOpenFileName(self)
        if fname is not None:
            cv2.imwrite(fname, 255 * self.result)
