# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autostereogram_generatorpgSbja.ui'
##
## Created by: Qt User Interface Compiler version 5.15.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Ui_Dialog(object):
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
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
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
        self.Title.setTextFormat(Qt.TextFormat.RichText)
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.MainBox.addWidget(self.Title)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayoutOriginal = QVBoxLayout()
        self.verticalLayoutOriginal.setObjectName(u"verticalLayoutOriginal")
        self.ImagePreviewLabel = QLabel(self.verticalLayoutWidget)
        self.ImagePreviewLabel.setObjectName(u"ImagePreviewLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ImagePreviewLabel.sizePolicy().hasHeightForWidth())
        self.ImagePreviewLabel.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(14)
        self.ImagePreviewLabel.setFont(font1)
        self.ImagePreviewLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayoutOriginal.addWidget(self.ImagePreviewLabel)

        self.MapPreview = QLabel(self.verticalLayoutWidget)
        self.MapPreview.setObjectName(u"MapPreview")

        self.verticalLayoutOriginal.addWidget(self.MapPreview)

        self.LoadImage = QPushButton(self.verticalLayoutWidget)
        self.LoadImage.setObjectName(u"LoadImage")

        self.verticalLayoutOriginal.addWidget(self.LoadImage)


        self.horizontalLayout.addLayout(self.verticalLayoutOriginal)

        self.verticalLayoutResult = QVBoxLayout()
        self.verticalLayoutResult.setObjectName(u"verticalLayoutResult")
        self.ImageResultLabel = QLabel(self.verticalLayoutWidget)
        self.ImageResultLabel.setObjectName(u"ImageResultLabel")
        sizePolicy1.setHeightForWidth(self.ImageResultLabel.sizePolicy().hasHeightForWidth())
        self.ImageResultLabel.setSizePolicy(sizePolicy1)
        self.ImageResultLabel.setFont(font1)
        self.ImageResultLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayoutResult.addWidget(self.ImageResultLabel)

        self.ResultPreview = QLabel(self.verticalLayoutWidget)
        self.ResultPreview.setObjectName(u"ResultPreview")

        self.verticalLayoutResult.addWidget(self.ResultPreview)

        self.SaveImage = QPushButton(self.verticalLayoutWidget)
        self.SaveImage.setObjectName(u"SaveImage")

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"IsGrayscale")
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"Use grayscale", None))
        self.checkBox.setGeometry(10, 350, 100, 15)

        self.verticalLayoutResult.addWidget(self.SaveImage)


        self.horizontalLayout.addLayout(self.verticalLayoutResult)


        self.MainBox.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.Title.setText(QCoreApplication.translate("Dialog", u"Autostereogram Generator", None))
        self.ImagePreviewLabel.setText(QCoreApplication.translate("Dialog", u"Map Preview", None))
        self.MapPreview.setText("")
        self.LoadImage.setText(QCoreApplication.translate("Dialog", u"Select an image", None))
        self.ImageResultLabel.setText(QCoreApplication.translate("Dialog", u"Result", None))
        self.ResultPreview.setText("")
        self.SaveImage.setText(QCoreApplication.translate("Dialog", u"Save Image", None))
    # retranslateUi

