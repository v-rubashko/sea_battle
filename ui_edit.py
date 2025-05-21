# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog_edit(object):
    def setupUi(self, Dialog_edit):
        if not Dialog_edit.objectName():
            Dialog_edit.setObjectName(u"Dialog_edit")
        Dialog_edit.resize(500, 350)
        Dialog_edit.setStyleSheet(u"border-image: url(:/backgrond/game_images/background_4.jpg);\n"
"\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog_edit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_edit = QFrame(Dialog_edit)
        self.frame_edit.setObjectName(u"frame_edit")
        self.frame_edit.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-image: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px")
        self.frame_edit.setFrameShape(QFrame.StyledPanel)
        self.frame_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_enter = QLabel(self.frame_edit)
        self.label_enter.setObjectName(u"label_enter")
        self.label_enter.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_enter, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_icon_name = QLabel(self.frame_edit)
        self.label_icon_name.setObjectName(u"label_icon_name")
        self.label_icon_name.setMaximumSize(QSize(24, 16777215))
        self.label_icon_name.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_name.setPixmap(QPixmap(u":/icons/icons/flag_w.svg"))

        self.horizontalLayout_6.addWidget(self.label_icon_name)

        self.label_name = QLabel(self.frame_edit)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_6.addWidget(self.label_name)

        self.lineEdit_name = QLineEdit(self.frame_edit)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setMaximumSize(QSize(130, 25))
        self.lineEdit_name.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"")
        self.lineEdit_name.setMaxLength(10)

        self.horizontalLayout_6.addWidget(self.lineEdit_name)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_icon_shipType = QLabel(self.frame_edit)
        self.label_icon_shipType.setObjectName(u"label_icon_shipType")
        self.label_icon_shipType.setMaximumSize(QSize(24, 16777215))
        self.label_icon_shipType.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_shipType.setPixmap(QPixmap(u":/icons/icons/sailing_w.svg"))

        self.horizontalLayout_5.addWidget(self.label_icon_shipType)

        self.label_shipType = QLabel(self.frame_edit)
        self.label_shipType.setObjectName(u"label_shipType")
        self.label_shipType.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_5.addWidget(self.label_shipType)

        self.comboBox_shipType = QComboBox(self.frame_edit)
        self.comboBox_shipType.addItem("")
        self.comboBox_shipType.addItem("")
        self.comboBox_shipType.addItem("")
        self.comboBox_shipType.setObjectName(u"comboBox_shipType")
        self.comboBox_shipType.setMaximumSize(QSize(130, 16777215))
        self.comboBox_shipType.setStyleSheet(u"QComboBox {\n"
"font-size: 15pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.horizontalLayout_5.addWidget(self.comboBox_shipType)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_icon_hp = QLabel(self.frame_edit)
        self.label_icon_hp.setObjectName(u"label_icon_hp")
        self.label_icon_hp.setMaximumSize(QSize(24, 16777215))
        self.label_icon_hp.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_hp.setPixmap(QPixmap(u":/icons/icons/favorite_w.svg"))

        self.horizontalLayout_4.addWidget(self.label_icon_hp)

        self.label_hp = QLabel(self.frame_edit)
        self.label_hp.setObjectName(u"label_hp")
        self.label_hp.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_4.addWidget(self.label_hp)

        self.lineEdit_hp = QLineEdit(self.frame_edit)
        self.lineEdit_hp.setObjectName(u"lineEdit_hp")
        self.lineEdit_hp.setMaximumSize(QSize(130, 25))
        self.lineEdit_hp.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;")
        self.lineEdit_hp.setMaxLength(1)

        self.horizontalLayout_4.addWidget(self.lineEdit_hp)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_icon__damage = QLabel(self.frame_edit)
        self.label_icon__damage.setObjectName(u"label_icon__damage")
        self.label_icon__damage.setMaximumSize(QSize(24, 16777215))
        self.label_icon__damage.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon__damage.setPixmap(QPixmap(u":/icons/icons/local_police_w.svg"))

        self.horizontalLayout_3.addWidget(self.label_icon__damage)

        self.label_damage = QLabel(self.frame_edit)
        self.label_damage.setObjectName(u"label_damage")
        self.label_damage.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_3.addWidget(self.label_damage)

        self.lineEdit_damage = QLineEdit(self.frame_edit)
        self.lineEdit_damage.setObjectName(u"lineEdit_damage")
        self.lineEdit_damage.setMaximumSize(QSize(130, 25))
        self.lineEdit_damage.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;")
        self.lineEdit_damage.setMaxLength(1)

        self.horizontalLayout_3.addWidget(self.lineEdit_damage)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_icon_speed = QLabel(self.frame_edit)
        self.label_icon_speed.setObjectName(u"label_icon_speed")
        self.label_icon_speed.setMaximumSize(QSize(24, 16777215))
        self.label_icon_speed.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_speed.setPixmap(QPixmap(u":/icons/icons/keyboard_double_arrow_right_w.svg"))

        self.horizontalLayout_2.addWidget(self.label_icon_speed)

        self.label_speed = QLabel(self.frame_edit)
        self.label_speed.setObjectName(u"label_speed")
        self.label_speed.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_speed)

        self.lineEdit_speed = QLineEdit(self.frame_edit)
        self.lineEdit_speed.setObjectName(u"lineEdit_speed")
        self.lineEdit_speed.setMaximumSize(QSize(130, 25))
        self.lineEdit_speed.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;")
        self.lineEdit_speed.setMaxLength(1)

        self.horizontalLayout_2.addWidget(self.lineEdit_speed)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_warning = QLabel(self.frame_edit)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;")

        self.verticalLayout.addWidget(self.label_warning, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame = QFrame(self.frame_edit)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_save = QPushButton(self.frame)
        self.pushButton_save.setObjectName(u"pushButton_save")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(10)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(158, 131, 87, 100);\n"
"border: 1px solid rgba(158, 131, 87, 200);\n"
"border-radius: 7px;\n"
"width: 150px;\n"
"height: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(158, 131, 87, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(158, 131, 87, 200);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/save_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_save.setIcon(icon)
        self.pushButton_save.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_close = QPushButton(self.frame)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setFont(font)
        self.pushButton_close.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(158, 131, 87, 100);\n"
"border: 1px solid rgba(158, 131, 87, 200);\n"
"border-radius: 7px;\n"
"width: 150px;\n"
"height: 25px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(158, 131, 87, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(158, 131, 87, 200);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/close_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_close.setIcon(icon1)
        self.pushButton_close.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.pushButton_close)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.frame_edit, 0, Qt.AlignHCenter)


        self.retranslateUi(Dialog_edit)

        self.comboBox_shipType.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_edit)
    # setupUi

    def retranslateUi(self, Dialog_edit):
        Dialog_edit.setWindowTitle(QCoreApplication.translate("Dialog_edit", u"Ship info", None))
        self.label_enter.setText(QCoreApplication.translate("Dialog_edit", u"\u0412\u0432\u043e\u0434 \u0434\u0430\u043d\u043d\u044b\u0445 \u043a\u043e\u0440\u0430\u0431\u043b\u044f", None))
        self.label_icon_name.setText("")
        self.label_name.setText(QCoreApplication.translate("Dialog_edit", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.lineEdit_name.setPlaceholderText("")
        self.label_icon_shipType.setText("")
        self.label_shipType.setText(QCoreApplication.translate("Dialog_edit", u"\u0422\u0438\u043f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.comboBox_shipType.setItemText(0, QCoreApplication.translate("Dialog_edit", u"\u0411\u0440\u043e\u043d\u0435\u043d\u043e\u0441\u0435\u0446", None))
        self.comboBox_shipType.setItemText(1, QCoreApplication.translate("Dialog_edit", u"\u0422\u043e\u0440\u043f. \u043a\u0430\u0442\u0435\u0440", None))
        self.comboBox_shipType.setItemText(2, QCoreApplication.translate("Dialog_edit", u"\u041f\u041a \u043b\u043e\u0434\u043a\u0430", None))

        self.label_icon_hp.setText("")
        self.label_hp.setText(QCoreApplication.translate("Dialog_edit", u"\u041e\u0447\u043a\u0438 \u0425\u041f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_icon__damage.setText("")
        self.label_damage.setText(QCoreApplication.translate("Dialog_edit", u"\u041e\u0447\u043a\u0438 \u0443\u0440\u043e\u043d\u0430 \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_icon_speed.setText("")
        self.label_speed.setText(QCoreApplication.translate("Dialog_edit", u"\u041e\u0447\u043a\u0438 \u0441\u043a\u043e\u0440\u043e\u0441\u0442\u0438 \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_warning.setText("")
        self.pushButton_save.setText(QCoreApplication.translate("Dialog_edit", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_close.setText(QCoreApplication.translate("Dialog_edit", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

