from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QMainWindow

import os
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
        self.SaveImage.clicked.connect(self.save_result)

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, filter="Image Files (*.png *.jpg *.bmp)")

        # Ensure a file as been chosen
        if fname[0] == '':
            return

        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.MapPreview.setPixmap(QPixmap(pixmap))

        self.current_preview_grascale = self.checkBox.isChecked()
        self.result = create_autoStereogram(fname[0], self.current_preview_grascale)
        cv2.imwrite(".result.jpg", 255 * self.result)

        qimage = QImage(".result.jpg")
        self.ResultPreview.setPixmap(QPixmap(qimage))

    def save_result(self):
        if self.result is not None:
            fname, _ = QFileDialog.getSaveFileName(self, "./results/", filter="Image Files (*.jpg)")
            if fname != "":
                _, filename = os.path.split(fname)
                if os.path.splitext(filename)[1] == "":
                    fname += ".jpg"

                cv2.imwrite(fname, 255 * self.result)
