# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'rules_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Dialog_rules(object):
    def setupUi(self, Dialog_rules):
        if not Dialog_rules.objectName():
            Dialog_rules.setObjectName(u"Dialog_rules")
        Dialog_rules.resize(670, 520)
        Dialog_rules.setMinimumSize(QSize(670, 0))
        Dialog_rules.setStyleSheet(u"border-image: url(:/backgrond/game_images/background_4.jpg);\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog_rules)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_rules = QFrame(Dialog_rules)
        self.frame_rules.setObjectName(u"frame_rules")
        self.frame_rules.setMinimumSize(QSize(640, 0))
        self.frame_rules.setMaximumSize(QSize(640, 16777215))
        self.frame_rules.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-image: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px")
        self.frame_rules.setFrameShape(QFrame.StyledPanel)
        self.frame_rules.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_rules)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_rules = QLabel(self.frame_rules)
        self.label_rules.setObjectName(u"label_rules")
        self.label_rules.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_rules.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_rules)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_rules_text = QLabel(self.frame_rules)
        self.label_rules_text.setObjectName(u"label_rules_text")
        self.label_rules_text.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 12pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.verticalLayout.addWidget(self.label_rules_text)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton_close = QPushButton(self.frame_rules)
        self.pushButton_close.setObjectName(u"pushButton_close")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(10)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(158, 131, 87, 100);\n"
"border: 1px solid rgba(158, 131, 87, 200);\n"
"border-radius: 7px;\n"
"width: 360px;\n"
"height: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(158, 131, 87, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(158, 131, 87, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/close_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_close.setIcon(icon)
        self.pushButton_close.setIconSize(QSize(16, 16))

        self.verticalLayout.addWidget(self.pushButton_close, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_rules, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog_rules)

        QMetaObject.connectSlotsByName(Dialog_rules)
    # setupUi

    def retranslateUi(self, Dialog_rules):
        Dialog_rules.setWindowTitle(QCoreApplication.translate("Dialog_rules", u"Rules", None))
        self.label_rules.setText(QCoreApplication.translate("Dialog_rules", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b:", None))
        self.label_rules_text.setText(QCoreApplication.translate("Dialog_rules", u"TextLabel", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog_rules", u"\u0417\u0430\u043a\u0440\u044b\u0442\u044c", None))
    # retranslateUi

