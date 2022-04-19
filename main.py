#For the GUI
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit
from PyQt5.QtGui import QPixmap

#To Perform the Stereogram functions
import numpy as np
import math
import cv2
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.title = "AutoStereogram Generator"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300

        self.InitWindow()
 
    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
 
        vbox = QVBoxLayout()
 
        self.btn1 = QPushButton("Browse Image")
        self.btn1.clicked.connect(self.getImage)
 
        vbox.addWidget(self.btn1)
 
        self.label = QLabel("Select an Image")
        vbox.addWidget(self.label)
 
        self.setLayout(vbox)
 
        self.show()
 
    def getImage(self):
        fname = QFileDialog.getOpenFileName(self)
        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        self.label.setPixmap(QPixmap(pixmap))
        self.resize(10, 10)

        create_autoStereogram(fname[0])


def create_autoStereogram(fileName):

    print("File Name", fileName)

    depth_map = cv2.imread(fileName)
    depth_map = cv2.cvtColor(depth_map, cv2.COLOR_BGR2GRAY)

    size_x, size_y = depth_map.shape
    pattern = np.random.uniform(0, 1, (size_y, 64, 1))

    cv2.imshow("pattern", pattern)

    def autostereogram(depth_map, pattern):
        E = 0.1
        b = 1.0  # Distance between the near and far plane
        a = 2  # Distance between the autostereogram plane and the near plane
        autostereogram = np.zeros_like(depth_map, dtype=pattern.dtype)

        for row in range(depth_map.shape[0]):
            for column in range(depth_map.shape[1]):
                if column < pattern.shape[1]:  # If the current column is smaller than the amount of columns in the pattern
                    # Copy in the current row/col the pattern
                    autostereogram[row, column] = pattern[row % pattern.shape[0], column]
                else:
                    grey_value = depth_map[row, column]
                    s_on_two = math.floor((((a - (b * grey_value / 255)) * E) / 2 * (1 + a - (b * grey_value))) + 0.5)
                    autostereogram[row, column] = autostereogram[row, column - pattern.shape[1] + s_on_two]
                    if column - pattern.shape[1] - s_on_two > 0:
                        autostereogram[row, column] = autostereogram[row, column - pattern.shape[1] - s_on_two]
        return autostereogram

    final_image = autostereogram(depth_map, pattern)
    cv2.imshow("final", final_image)

    cv2.imwrite("result.jpg", 255 * final_image)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())




