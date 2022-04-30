from PyQt5.QtWidgets import QApplication,QWidget, QVBoxLayout, QPushButton, QFileDialog , QLabel, QTextEdit, QSizePolicy, QHBoxLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QRect, Qt, QCoreApplication, QMetaObject

from src.autostereogram import create_autoStereogram


class UI_MainWindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(600, 420)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 9, 581, 401))
        self.MainBox = QVBoxLayout(self.verticalLayoutWidget)
        self.MainBox.setObjectName(u"MainBox")
        self.MainBox.setContentsMargins(0, 0, 0, 0)
        self.Title = QLabel(self.verticalLayoutWidget)
        self.Title.setObjectName(u"Title")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(30)
        sizePolicy.setHeightForWidth(self.Title.sizePolicy().hasHeightForWidth())
        self.Title.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setTextFormat(Qt.RichText)
        self.Title.setAlignment(Qt.AlignCenter)

        self.MainBox.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayoutOriginal = QVBoxLayout()
        self.verticalLayoutOriginal.setObjectName(u"verticalLayoutOriginal")
        self.ImagePreviewLabel = QLabel(self.verticalLayoutWidget)
        self.ImagePreviewLabel.setObjectName(u"ImagePreviewLabel")
        font1 = QFont()
        font1.setPointSize(14)
        self.ImagePreviewLabel.setFont(font1)
        self.ImagePreviewLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayoutOriginal.addWidget(self.ImagePreviewLabel)

        self.LoadImage = QPushButton(self.verticalLayoutWidget)
        self.LoadImage.setObjectName(u"LoadImage")

        self.verticalLayoutOriginal.addWidget(self.LoadImage)

        self.horizontalLayout.addLayout(self.verticalLayoutOriginal)

        self.verticalLayoutResult = QVBoxLayout()
        self.verticalLayoutResult.setObjectName(u"verticalLayoutResult")
        self.ImageResultLabel = QLabel(self.verticalLayoutWidget)
        self.ImageResultLabel.setObjectName(u"ImageResultLabel")
        self.ImageResultLabel.setFont(font1)
        self.ImageResultLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayoutResult.addWidget(self.ImageResultLabel)

        self.SaveImage = QPushButton(self.verticalLayoutWidget)
        self.SaveImage.setObjectName(u"SaveImage")

        self.verticalLayoutResult.addWidget(self.SaveImage)

        self.horizontalLayout.addLayout(self.verticalLayoutResult)

        self.MainBox.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Title.setText(QCoreApplication.translate("Dialog", u"Autostereogram Generator", None))
        self.ImagePreviewLabel.setText(QCoreApplication.translate("Dialog", u"Map Preview", None))
        self.LoadImage.setText(QCoreApplication.translate("Dialog", u"Select an image", None))
        self.ImageResultLabel.setText(QCoreApplication.translate("Dialog", u"Result", None))
        self.SaveImage.setText(QCoreApplication.translate("Dialog", u"Save Image", None))
