# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.groupBox_4 = QGroupBox(Form)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.input_line = QLineEdit(self.groupBox_4)
        self.input_line.setObjectName(u"input_line")

        self.horizontalLayout_2.addWidget(self.input_line)

        self.input_btn_1 = QPushButton(self.groupBox_4)
        self.input_btn_1.setObjectName(u"input_btn_1")

        self.horizontalLayout_2.addWidget(self.input_btn_1)

        self.input_btn_2 = QPushButton(self.groupBox_4)
        self.input_btn_2.setObjectName(u"input_btn_2")

        self.horizontalLayout_2.addWidget(self.input_btn_2)


        self.verticalLayout_3.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(Form)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.output_line = QLineEdit(self.groupBox_5)
        self.output_line.setObjectName(u"output_line")

        self.horizontalLayout_3.addWidget(self.output_line)

        self.output_btn = QPushButton(self.groupBox_5)
        self.output_btn.setObjectName(u"output_btn")

        self.horizontalLayout_3.addWidget(self.output_btn)


        self.verticalLayout_3.addWidget(self.groupBox_5)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(self.groupBox_2)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.check_1 = QCheckBox(self.groupBox)
        self.check_1.setObjectName(u"check_1")

        self.verticalLayout.addWidget(self.check_1)

        self.check_2 = QCheckBox(self.groupBox)
        self.check_2.setObjectName(u"check_2")

        self.verticalLayout.addWidget(self.check_2)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.start_btn = QPushButton(self.groupBox_3)
        self.start_btn.setObjectName(u"start_btn")

        self.verticalLayout_2.addWidget(self.start_btn)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setOpenExternalLinks(True)

        self.verticalLayout_3.addWidget(self.label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_4.setTitle("")
        self.input_btn_1.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.input_btn_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.groupBox_5.setTitle("")
        self.output_btn.setText(QCoreApplication.translate("Form", u"\u53e6\u5b58\u4e3a", None))
        self.groupBox_2.setTitle("")
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u529f\u80fd\u9009\u62e9", None))
        self.check_1.setText(QCoreApplication.translate("Form", u"\u56fe\u5e8a\u56fe\u7247\u672c\u5730\u5316", None))
        self.check_2.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u4e3amd\u98ce\u683c\u56fe\u7247", None))
        self.groupBox_3.setTitle("")
        self.start_btn.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u8f6c\u5316\uff08\u8bf7\u8010\u5fc3\u7b49\u5f85\uff09", None))
        self.label.setText(QCoreApplication.translate("Form", u"https://github.com/thdlrt/md-pix-tool", None))
    # retranslateUi

