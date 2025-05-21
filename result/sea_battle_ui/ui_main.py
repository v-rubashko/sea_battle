# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1399, 600)
        MainWindow.setStyleSheet(u"border-image: url(:/backgrond/game_images/background_4.jpg);\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_16 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ship_1_info_frame = QFrame(self.centralwidget)
        self.ship_1_info_frame.setObjectName(u"ship_1_info_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ship_1_info_frame.sizePolicy().hasHeightForWidth())
        self.ship_1_info_frame.setSizePolicy(sizePolicy)
        self.ship_1_info_frame.setMinimumSize(QSize(380, 0))
        self.ship_1_info_frame.setMaximumSize(QSize(370, 16777215))
        self.ship_1_info_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-image: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px")
        self.verticalLayout = QVBoxLayout(self.ship_1_info_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.label_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_ship_1.setObjectName(u"label_ship_1")
        self.label_ship_1.setStyleSheet(u"color: rgb(0, 170, 0);\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_ship_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_ship_1)

        self.progressBar_ship_1 = QProgressBar(self.ship_1_info_frame)
        self.progressBar_ship_1.setObjectName(u"progressBar_ship_1")
        self.progressBar_ship_1.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"font-size: 15pt;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 170, 0, 200);\n"
"border-radius: 7px;\n"
"border-style: outset;\n"
"width: 360px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"background-color: rgb(0, 170, 0);\n"
"border-radius: 7px;\n"
"border-style: outset;\n"
"border: 1px solid rgba(0, 170, 0, 200);\n"
"}\n"
"")
        self.progressBar_ship_1.setValue(100)
        self.progressBar_ship_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.progressBar_ship_1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon_name_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_icon_name_ship_1.setObjectName(u"label_icon_name_ship_1")
        self.label_icon_name_ship_1.setMaximumSize(QSize(24, 16777215))
        self.label_icon_name_ship_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_name_ship_1.setPixmap(QPixmap(u":/icons/icons/flag_w.svg"))

        self.horizontalLayout.addWidget(self.label_icon_name_ship_1)

        self.label_name_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_name_ship_1.setObjectName(u"label_name_ship_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_name_ship_1.sizePolicy().hasHeightForWidth())
        self.label_name_ship_1.setSizePolicy(sizePolicy1)
        self.label_name_ship_1.setMinimumSize(QSize(210, 0))
        self.label_name_ship_1.setMaximumSize(QSize(210, 16777215))
        self.label_name_ship_1.setStyleSheet(u"color: white;\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_name_ship_1)

        self.label_value_name_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_value_name_ship_1.setObjectName(u"label_value_name_ship_1")
        self.label_value_name_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_value_name_ship_1)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_icon_shipType_1 = QLabel(self.ship_1_info_frame)
        self.label_icon_shipType_1.setObjectName(u"label_icon_shipType_1")
        self.label_icon_shipType_1.setMaximumSize(QSize(24, 16777215))
        self.label_icon_shipType_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_shipType_1.setPixmap(QPixmap(u":/icons/icons/sailing_w.svg"))

        self.horizontalLayout_2.addWidget(self.label_icon_shipType_1)

        self.label_shipType_1 = QLabel(self.ship_1_info_frame)
        self.label_shipType_1.setObjectName(u"label_shipType_1")
        sizePolicy1.setHeightForWidth(self.label_shipType_1.sizePolicy().hasHeightForWidth())
        self.label_shipType_1.setSizePolicy(sizePolicy1)
        self.label_shipType_1.setMinimumSize(QSize(210, 0))
        self.label_shipType_1.setMaximumSize(QSize(210, 16777215))
        self.label_shipType_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_shipType_1)

        self.label_value_shipType_1 = QLabel(self.ship_1_info_frame)
        self.label_value_shipType_1.setObjectName(u"label_value_shipType_1")
        self.label_value_shipType_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_value_shipType_1)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_icon_hp_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_icon_hp_ship_1.setObjectName(u"label_icon_hp_ship_1")
        self.label_icon_hp_ship_1.setMaximumSize(QSize(24, 16777215))
        self.label_icon_hp_ship_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_hp_ship_1.setPixmap(QPixmap(u":/icons/icons/favorite_w.svg"))

        self.horizontalLayout_3.addWidget(self.label_icon_hp_ship_1)

        self.label_hp_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_hp_ship_1.setObjectName(u"label_hp_ship_1")
        sizePolicy1.setHeightForWidth(self.label_hp_ship_1.sizePolicy().hasHeightForWidth())
        self.label_hp_ship_1.setSizePolicy(sizePolicy1)
        self.label_hp_ship_1.setMinimumSize(QSize(210, 0))
        self.label_hp_ship_1.setMaximumSize(QSize(210, 16777215))
        self.label_hp_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_3.addWidget(self.label_hp_ship_1)

        self.label_value_hp_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_value_hp_ship_1.setObjectName(u"label_value_hp_ship_1")
        self.label_value_hp_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_3.addWidget(self.label_value_hp_ship_1)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_icon_damage_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_icon_damage_ship_1.setObjectName(u"label_icon_damage_ship_1")
        self.label_icon_damage_ship_1.setMaximumSize(QSize(24, 16777215))
        self.label_icon_damage_ship_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_damage_ship_1.setPixmap(QPixmap(u":/icons/icons/local_police_w.svg"))

        self.horizontalLayout_4.addWidget(self.label_icon_damage_ship_1)

        self.label_damage_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_damage_ship_1.setObjectName(u"label_damage_ship_1")
        sizePolicy1.setHeightForWidth(self.label_damage_ship_1.sizePolicy().hasHeightForWidth())
        self.label_damage_ship_1.setSizePolicy(sizePolicy1)
        self.label_damage_ship_1.setMinimumSize(QSize(210, 0))
        self.label_damage_ship_1.setMaximumSize(QSize(210, 16777215))
        self.label_damage_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_4.addWidget(self.label_damage_ship_1)

        self.label_value_damage_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_value_damage_ship_1.setObjectName(u"label_value_damage_ship_1")
        self.label_value_damage_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_4.addWidget(self.label_value_damage_ship_1)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_icon_speed_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_icon_speed_ship_1.setObjectName(u"label_icon_speed_ship_1")
        self.label_icon_speed_ship_1.setMaximumSize(QSize(24, 16777215))
        self.label_icon_speed_ship_1.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_speed_ship_1.setPixmap(QPixmap(u":/icons/icons/keyboard_double_arrow_right_w.svg"))

        self.horizontalLayout_5.addWidget(self.label_icon_speed_ship_1)

        self.label_speed_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_speed_ship_1.setObjectName(u"label_speed_ship_1")
        sizePolicy1.setHeightForWidth(self.label_speed_ship_1.sizePolicy().hasHeightForWidth())
        self.label_speed_ship_1.setSizePolicy(sizePolicy1)
        self.label_speed_ship_1.setMinimumSize(QSize(210, 0))
        self.label_speed_ship_1.setMaximumSize(QSize(210, 16777215))
        self.label_speed_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_5.addWidget(self.label_speed_ship_1)

        self.label_value_speed_ship_1 = QLabel(self.ship_1_info_frame)
        self.label_value_speed_ship_1.setObjectName(u"label_value_speed_ship_1")
        self.label_value_speed_ship_1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_5.addWidget(self.label_value_speed_ship_1)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.pushButton_enter_ship_1 = QPushButton(self.ship_1_info_frame)
        self.pushButton_enter_ship_1.setObjectName(u"pushButton_enter_ship_1")
        font = QFont()
        font.setFamilies([u"Noto Sans SC"])
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        self.pushButton_enter_ship_1.setFont(font)
        self.pushButton_enter_ship_1.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 170, 0, 100);\n"
"border: 1px solid rgba(0, 170, 0, 200);\n"
"border-radius: 7px;\n"
"width: 360px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 170, 0, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 170, 0, 200);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border: rgba(200, 200, 200, 200)\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/edit_note_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_enter_ship_1.setIcon(icon)
        self.pushButton_enter_ship_1.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pushButton_enter_ship_1, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout_16.addWidget(self.ship_1_info_frame)

        self.midle_frame = QFrame(self.centralwidget)
        self.midle_frame.setObjectName(u"midle_frame")
        self.midle_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-image: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px")
        self.verticalLayout_6 = QVBoxLayout(self.midle_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_start_battle = QPushButton(self.midle_frame)
        self.pushButton_start_battle.setObjectName(u"pushButton_start_battle")
        self.pushButton_start_battle.setEnabled(False)
        font1 = QFont()
        font1.setFamilies([u"Noto Sans SC"])
        font1.setPointSize(15)
        font1.setBold(True)
        self.pushButton_start_battle.setFont(font1)
        self.pushButton_start_battle.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(226, 118, 10, 100);\n"
"border: 1px solid rgba(226, 118, 10, 200);\n"
"border-radius: 7px;\n"
"width: 360px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(226, 118, 10, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(226, 118, 10, 200);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border: rgba(200, 200, 200, 200)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/swords_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_start_battle.setIcon(icon1)
        self.pushButton_start_battle.setIconSize(QSize(24, 24))

        self.verticalLayout_6.addWidget(self.pushButton_start_battle, 0, Qt.AlignHCenter)

        self.env_frame = QFrame(self.midle_frame)
        self.env_frame.setObjectName(u"env_frame")
        sizePolicy1.setHeightForWidth(self.env_frame.sizePolicy().hasHeightForWidth())
        self.env_frame.setSizePolicy(sizePolicy1)
        self.env_frame.setMinimumSize(QSize(360, 0))
        self.env_frame.setMaximumSize(QSize(360, 16777215))
        self.env_frame.setStyleSheet(u"")
        self.horizontalLayout_14 = QHBoxLayout(self.env_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_icon_location = QLabel(self.env_frame)
        self.label_icon_location.setObjectName(u"label_icon_location")
        self.label_icon_location.setMaximumSize(QSize(24, 16777215))
        self.label_icon_location.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_location.setPixmap(QPixmap(u":/icons/icons/water_w.svg"))

        self.horizontalLayout_11.addWidget(self.label_icon_location)

        self.label_location = QLabel(self.env_frame)
        self.label_location.setObjectName(u"label_location")
        font2 = QFont()
        font2.setFamilies([u"Noto Sans SC"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_location.setFont(font2)
        self.label_location.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_11.addWidget(self.label_location)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.radioButton_sea = QRadioButton(self.env_frame)
        self.buttonGroup_location = QButtonGroup(MainWindow)
        self.buttonGroup_location.setObjectName(u"buttonGroup_location")
        self.buttonGroup_location.addButton(self.radioButton_sea)
        self.radioButton_sea.setObjectName(u"radioButton_sea")
        self.radioButton_sea.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.radioButton_sea.setChecked(True)

        self.verticalLayout_3.addWidget(self.radioButton_sea)

        self.radioButton_bay = QRadioButton(self.env_frame)
        self.buttonGroup_location.addButton(self.radioButton_bay)
        self.radioButton_bay.setObjectName(u"radioButton_bay")
        self.radioButton_bay.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.radioButton_bay)


        self.horizontalLayout_14.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_icon_weather = QLabel(self.env_frame)
        self.label_icon_weather.setObjectName(u"label_icon_weather")
        self.label_icon_weather.setMaximumSize(QSize(24, 16777215))
        self.label_icon_weather.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_weather.setPixmap(QPixmap(u":/icons/icons/partly_cloudy_day_w.svg"))

        self.horizontalLayout_12.addWidget(self.label_icon_weather)

        self.label_weather = QLabel(self.env_frame)
        self.label_weather.setObjectName(u"label_weather")
        self.label_weather.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_12.addWidget(self.label_weather)


        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.radioButton_calm = QRadioButton(self.env_frame)
        self.buttonGroup_weather = QButtonGroup(MainWindow)
        self.buttonGroup_weather.setObjectName(u"buttonGroup_weather")
        self.buttonGroup_weather.addButton(self.radioButton_calm)
        self.radioButton_calm.setObjectName(u"radioButton_calm")
        self.radioButton_calm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.radioButton_calm.setChecked(True)

        self.verticalLayout_4.addWidget(self.radioButton_calm)

        self.radioButton_storm = QRadioButton(self.env_frame)
        self.buttonGroup_weather.addButton(self.radioButton_storm)
        self.radioButton_storm.setObjectName(u"radioButton_storm")
        self.radioButton_storm.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.radioButton_storm)


        self.horizontalLayout_14.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_icon_time = QLabel(self.env_frame)
        self.label_icon_time.setObjectName(u"label_icon_time")
        self.label_icon_time.setMaximumSize(QSize(24, 16777215))
        self.label_icon_time.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_time.setPixmap(QPixmap(u":/icons/icons/routine_w.svg"))

        self.horizontalLayout_13.addWidget(self.label_icon_time)

        self.label_time = QLabel(self.env_frame)
        self.label_time.setObjectName(u"label_time")
        self.label_time.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_13.addWidget(self.label_time)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.radioButton_day = QRadioButton(self.env_frame)
        self.buttonGroup_time_of_day = QButtonGroup(MainWindow)
        self.buttonGroup_time_of_day.setObjectName(u"buttonGroup_time_of_day")
        self.buttonGroup_time_of_day.addButton(self.radioButton_day)
        self.radioButton_day.setObjectName(u"radioButton_day")
        self.radioButton_day.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")
        self.radioButton_day.setChecked(True)

        self.verticalLayout_5.addWidget(self.radioButton_day)

        self.radioButton_night = QRadioButton(self.env_frame)
        self.buttonGroup_time_of_day.addButton(self.radioButton_night)
        self.radioButton_night.setObjectName(u"radioButton_night")
        self.radioButton_night.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 10pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_5.addWidget(self.radioButton_night)


        self.horizontalLayout_14.addLayout(self.verticalLayout_5)


        self.verticalLayout_6.addWidget(self.env_frame, 0, Qt.AlignHCenter)

        self.label_battle_log = QLabel(self.midle_frame)
        self.label_battle_log.setObjectName(u"label_battle_log")
        self.label_battle_log.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")
        self.label_battle_log.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_battle_log)

        self.plainTextEdit = QPlainTextEdit(self.midle_frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(605, 0))
        self.plainTextEdit.setMaximumSize(QSize(605, 16777215))
        self.plainTextEdit.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;")
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.plainTextEdit, 0, Qt.AlignHCenter)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.pushButton_rules = QPushButton(self.midle_frame)
        self.pushButton_rules.setObjectName(u"pushButton_rules")
        font3 = QFont()
        font3.setFamilies([u"Noto Sans SC"])
        font3.setPointSize(10)
        self.pushButton_rules.setFont(font3)
        self.pushButton_rules.setStyleSheet(u"QPushButton {\n"
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
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/rule_w.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_rules.setIcon(icon2)
        self.pushButton_rules.setIconSize(QSize(16, 16))

        self.verticalLayout_6.addWidget(self.pushButton_rules, 0, Qt.AlignHCenter)


        self.horizontalLayout_16.addWidget(self.midle_frame)

        self.ship_2_info_frame = QFrame(self.centralwidget)
        self.ship_2_info_frame.setObjectName(u"ship_2_info_frame")
        self.ship_2_info_frame.setMinimumSize(QSize(380, 0))
        self.ship_2_info_frame.setMaximumSize(QSize(370, 16777215))
        self.ship_2_info_frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border-image: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"border: 1px solid rgba(255, 255, 255, 0);\n"
"border-radius: 7px")
        self.verticalLayout_2 = QVBoxLayout(self.ship_2_info_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.label_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_ship_2.setObjectName(u"label_ship_2")
        self.label_ship_2.setStyleSheet(u"color: rgb(0, 0, 170);\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")
        self.label_ship_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_ship_2)

        self.progressBar_ship_2 = QProgressBar(self.ship_2_info_frame)
        self.progressBar_ship_2.setObjectName(u"progressBar_ship_2")
        self.progressBar_ship_2.setStyleSheet(u"QProgressBar {\n"
"color: white;\n"
"font-size: 15pt;\n"
"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(0, 0, 170, 200);\n"
"border-radius: 7px;\n"
"border-style: outset;\n"
"width: 360px;\n"
"height: 25px;\n"
"}\n"
"\n"
"QProgressBar:chunk {\n"
"background-color: rgb(0, 0, 170);\n"
"border-radius: 7px;\n"
"border-style: outset;\n"
"border: 1px solid rgba(0, 0, 170, 200);\n"
"}")
        self.progressBar_ship_2.setValue(100)
        self.progressBar_ship_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.progressBar_ship_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_icon_name_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_icon_name_ship_2.setObjectName(u"label_icon_name_ship_2")
        self.label_icon_name_ship_2.setMaximumSize(QSize(24, 16777215))
        self.label_icon_name_ship_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_name_ship_2.setPixmap(QPixmap(u":/icons/icons/flag_w.svg"))

        self.horizontalLayout_6.addWidget(self.label_icon_name_ship_2)

        self.label_name_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_name_ship_2.setObjectName(u"label_name_ship_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(210)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_name_ship_2.sizePolicy().hasHeightForWidth())
        self.label_name_ship_2.setSizePolicy(sizePolicy2)
        self.label_name_ship_2.setMinimumSize(QSize(210, 0))
        self.label_name_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_6.addWidget(self.label_name_ship_2)

        self.label_value_name_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_value_name_ship_2.setObjectName(u"label_value_name_ship_2")
        self.label_value_name_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_6.addWidget(self.label_value_name_ship_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_icon_shipType_2 = QLabel(self.ship_2_info_frame)
        self.label_icon_shipType_2.setObjectName(u"label_icon_shipType_2")
        self.label_icon_shipType_2.setMaximumSize(QSize(24, 16777215))
        self.label_icon_shipType_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_shipType_2.setPixmap(QPixmap(u":/icons/icons/sailing_w.svg"))

        self.horizontalLayout_7.addWidget(self.label_icon_shipType_2)

        self.label_shipType_2 = QLabel(self.ship_2_info_frame)
        self.label_shipType_2.setObjectName(u"label_shipType_2")
        sizePolicy2.setHeightForWidth(self.label_shipType_2.sizePolicy().hasHeightForWidth())
        self.label_shipType_2.setSizePolicy(sizePolicy2)
        self.label_shipType_2.setMinimumSize(QSize(210, 0))
        self.label_shipType_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_7.addWidget(self.label_shipType_2)

        self.label_value_shipType_2 = QLabel(self.ship_2_info_frame)
        self.label_value_shipType_2.setObjectName(u"label_value_shipType_2")
        self.label_value_shipType_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_7.addWidget(self.label_value_shipType_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_icon_hp_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_icon_hp_ship_2.setObjectName(u"label_icon_hp_ship_2")
        self.label_icon_hp_ship_2.setMaximumSize(QSize(24, 16777215))
        self.label_icon_hp_ship_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_hp_ship_2.setPixmap(QPixmap(u":/icons/icons/favorite_w.svg"))

        self.horizontalLayout_8.addWidget(self.label_icon_hp_ship_2)

        self.label_hp_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_hp_ship_2.setObjectName(u"label_hp_ship_2")
        sizePolicy2.setHeightForWidth(self.label_hp_ship_2.sizePolicy().hasHeightForWidth())
        self.label_hp_ship_2.setSizePolicy(sizePolicy2)
        self.label_hp_ship_2.setMinimumSize(QSize(210, 0))
        self.label_hp_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_8.addWidget(self.label_hp_ship_2)

        self.label_value_hp_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_value_hp_ship_2.setObjectName(u"label_value_hp_ship_2")
        self.label_value_hp_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_8.addWidget(self.label_value_hp_ship_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_icon_damage_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_icon_damage_ship_2.setObjectName(u"label_icon_damage_ship_2")
        self.label_icon_damage_ship_2.setMaximumSize(QSize(24, 16777215))
        self.label_icon_damage_ship_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_damage_ship_2.setPixmap(QPixmap(u":/icons/icons/local_police_w.svg"))

        self.horizontalLayout_9.addWidget(self.label_icon_damage_ship_2)

        self.label_damage_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_damage_ship_2.setObjectName(u"label_damage_ship_2")
        sizePolicy2.setHeightForWidth(self.label_damage_ship_2.sizePolicy().hasHeightForWidth())
        self.label_damage_ship_2.setSizePolicy(sizePolicy2)
        self.label_damage_ship_2.setMinimumSize(QSize(210, 0))
        self.label_damage_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_9.addWidget(self.label_damage_ship_2)

        self.label_value_damage_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_value_damage_ship_2.setObjectName(u"label_value_damage_ship_2")
        self.label_value_damage_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_9.addWidget(self.label_value_damage_ship_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_icon_speed_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_icon_speed_ship_2.setObjectName(u"label_icon_speed_ship_2")
        self.label_icon_speed_ship_2.setMaximumSize(QSize(24, 16777215))
        self.label_icon_speed_ship_2.setStyleSheet(u"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_speed_ship_2.setPixmap(QPixmap(u":/icons/icons/keyboard_double_arrow_right_w.svg"))

        self.horizontalLayout_10.addWidget(self.label_icon_speed_ship_2)

        self.label_speed_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_speed_ship_2.setObjectName(u"label_speed_ship_2")
        sizePolicy2.setHeightForWidth(self.label_speed_ship_2.sizePolicy().hasHeightForWidth())
        self.label_speed_ship_2.setSizePolicy(sizePolicy2)
        self.label_speed_ship_2.setMinimumSize(QSize(210, 0))
        self.label_speed_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"font-weight: bold;\n"
"padding-top: 10px;")

        self.horizontalLayout_10.addWidget(self.label_speed_ship_2)

        self.label_value_speed_ship_2 = QLabel(self.ship_2_info_frame)
        self.label_value_speed_ship_2.setObjectName(u"label_value_speed_ship_2")
        self.label_value_speed_ship_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_10.addWidget(self.label_value_speed_ship_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_6)

        self.pushButton_enter_ship_2 = QPushButton(self.ship_2_info_frame)
        self.pushButton_enter_ship_2.setObjectName(u"pushButton_enter_ship_2")
        self.pushButton_enter_ship_2.setFont(font1)
        self.pushButton_enter_ship_2.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"background-color: rgba(0, 0, 170, 100);\n"
"border: 1px solid rgba(0, 0, 170, 200);\n"
"border-radius: 7px;\n"
"width: 360px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 170, 150);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(0, 0, 170, 200);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"background-color: rgba(200, 200, 200, 100);\n"
"border: rgba(200, 200, 200, 200)\n"
"}")
        self.pushButton_enter_ship_2.setIcon(icon)
        self.pushButton_enter_ship_2.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_enter_ship_2, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_16.addWidget(self.ship_2_info_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SeaBattle", None))
        self.label_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u0420\u0410\u0411\u041b\u042c 1", None))
        self.label_icon_name_ship_1.setText("")
        self.label_name_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_name_ship_1.setText(QCoreApplication.translate("MainWindow", u"name_1", None))
        self.label_icon_shipType_1.setText("")
        self.label_shipType_1.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_shipType_1.setText(QCoreApplication.translate("MainWindow", u"shipType_1", None))
        self.label_icon_hp_ship_1.setText("")
        self.label_hp_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_hp_ship_1.setText(QCoreApplication.translate("MainWindow", u"hp_1", None))
        self.label_icon_damage_ship_1.setText("")
        self.label_damage_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043d \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_damage_ship_1.setText(QCoreApplication.translate("MainWindow", u"damage_1", None))
        self.label_icon_speed_ship_1.setText("")
        self.label_speed_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_speed_ship_1.setText(QCoreApplication.translate("MainWindow", u"speed_1", None))
        self.pushButton_enter_ship_1.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u0440\u0430\u0431\u043b\u044f 1", None))
        self.pushButton_start_battle.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0410\u0427\u0410\u0422\u042c \u0411\u041e\u0419", None))
        self.label_icon_location.setText("")
        self.label_location.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None))
        self.radioButton_sea.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0440\u0435", None))
        self.radioButton_bay.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0445\u0442\u0430", None))
        self.label_icon_weather.setText("")
        self.label_weather.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430", None))
        self.radioButton_calm.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0442\u0438\u043b\u044c", None))
        self.radioButton_storm.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0442\u043e\u0440\u043c", None))
        self.label_icon_time.setText("")
        self.label_time.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441\u0443\u0442\u043e\u043a", None))
        self.radioButton_day.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043d\u044c", None))
        self.radioButton_night.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0447\u044c", None))
        self.label_battle_log.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041e\u0414 \u0411\u0418\u0422\u0412\u042b:", None))
        self.pushButton_rules.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0430\u0432\u0438\u043b\u0430 \u0438\u0433\u0440\u044b", None))
        self.label_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u041a\u041e\u0420\u0410\u0411\u041b\u042c 2", None))
        self.label_icon_name_ship_2.setText("")
        self.label_name_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_name_ship_2.setText(QCoreApplication.translate("MainWindow", u"name_2", None))
        self.label_icon_shipType_2.setText("")
        self.label_shipType_2.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_shipType_2.setText(QCoreApplication.translate("MainWindow", u"shipType_2", None))
        self.label_icon_hp_ship_2.setText("")
        self.label_hp_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u0425\u041f \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_hp_ship_2.setText(QCoreApplication.translate("MainWindow", u"hp_2", None))
        self.label_icon_damage_ship_2.setText("")
        self.label_damage_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u043d \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_damage_ship_2.setText(QCoreApplication.translate("MainWindow", u"damage_2", None))
        self.label_icon_speed_ship_2.setText("")
        self.label_speed_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u043a\u043e\u0440\u0430\u0431\u043b\u044f:", None))
        self.label_value_speed_ship_2.setText(QCoreApplication.translate("MainWindow", u"speed_2", None))
        self.pushButton_enter_ship_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0441\u0442\u0438 \u0434\u0430\u043d\u043d\u044b\u0435 \u043a\u043e\u0440\u0430\u0431\u043b\u044f 2", None))
    # retranslateUi

