import sys
from math import ceil
from time import sleep

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QThread, Signal

from ui_main import Ui_MainWindow
import ship
from ui_rules import Ui_Dialog_rules
from ui_edit import Ui_Dialog_edit

SLEEP_TIME = 1  # Задержка выведения лога битвы
TOTAL_POINTS = 10  # Доступное игроку количество очков
SEPARATOR = f"{'':-<32}"  # Разделитель в логе итераций боя


class SeaBattle(QMainWindow):
    def __init__(self):
        super(SeaBattle, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ship_1 = ship.BattleShip()
        self.ship_2 = ship.BattleShip()
        self.reloadShipInfo()
        self.ui.pushButton_enter_ship_1.clicked.connect(self.openShipInfoWindow)
        self.ui.pushButton_enter_ship_2.clicked.connect(self.openShipInfoWindow)
        self.ui.pushButton_rules.clicked.connect(self.openRulesWindow)
        self.ui.radioButton_sea.toggled.connect(self.changeLocation)
        self.ui.radioButton_calm.toggled.connect(self.changeWeather)
        self.ui.radioButton_day.toggled.connect(self.changeTime)
        self.ui.pushButton_start_battle.clicked.connect(self.startBattle)

    def reloadShipInfo(self):
        def setValue(name_label, type_label, hp_label, damage_label, speed_label, name_value, type_value, hp_value,
                     damage_value, speed_value):
            name_label.setText(name_value)
            type_label.setText(type_value)
            hp_label.setText(str(hp_value))
            damage_label.setText(str(damage_value))
            speed_label.setText(str(speed_value))

        setValue(self.ui.label_value_name_ship_1, self.ui.label_value_shipType_1, self.ui.label_value_hp_ship_1,
                 self.ui.label_value_damage_ship_1, self.ui.label_value_speed_ship_1, self.ship_1.name,
                 self.ship_1.shipType, self.ship_1.hp_start, self.ship_1.damage, self.ship_1.speed)
        setValue(self.ui.label_value_name_ship_2, self.ui.label_value_shipType_2, self.ui.label_value_hp_ship_2,
                 self.ui.label_value_damage_ship_2, self.ui.label_value_speed_ship_2, self.ship_2.name,
                 self.ship_2.shipType, self.ship_2.hp_start, self.ship_2.damage, self.ship_2.speed)

    def openShipInfoWindow(self):
        def setWindowValue(text, name, type, hp_points, damage_points, speed, flag):
            self.ui_window_edit.label_enter.setText(text)
            self.ui_window_edit.lineEdit_name.setText(name)
            self.ui_window_edit.comboBox_shipType.setCurrentText(type)
            self.ui_window_edit.lineEdit_hp.setText(str(hp_points))
            self.ui_window_edit.lineEdit_damage.setText(str(damage_points))
            self.ui_window_edit.lineEdit_speed.setText(str(speed))
            self.flag = flag
            if not self.ui_window_edit.lineEdit_hp.text().isdigit():
                self.ui_window_edit.pushButton_save.setEnabled(False)
            self.ui_window_edit.pushButton_save.clicked.connect(self.enterShipInfo)
            self.ui_window_edit.pushButton_close.clicked.connect(self.ship_window.close)

        self.ship_window = QtWidgets.QDialog(self)
        self.ui_window_edit = Ui_Dialog_edit()
        self.ui_window_edit.setupUi(self.ship_window)
        self.ship_window.show()
        sender = self.sender()
        if sender.text() == 'Ввести данные корабля 1':
            setWindowValue('Ввод данных корабля 1', self.ship_1.name, self.ship_1.shipType, str(self.ship_1.hp_points),
                           str(self.ship_1.damage_points), str(self.ship_1.speed_points), 1)
        else:
            setWindowValue('Ввод данных корабля 2', self.ship_2.name, self.ship_2.shipType, str(self.ship_2.hp_points),
                           str(self.ship_2.damage_points), str(self.ship_2.speed_points), 2)

    def enterShipInfo(self):
        def setShipValue(ship, label_ship):
            ship.setupShipPoints(name, shipType, hp, damage, speed)
            if self.ui.radioButton_bay.isChecked():
                ship.speed = ship.speed / 2
            if self.ui.radioButton_storm.isChecked():
                ship.hp_start = int(ship.hp_start / 2)
            if self.ui.radioButton_night.isChecked():
                ship.damage = int(ship.damage * 2)
            self.reloadShipInfo()
            label_ship.setText(ship.name)
            self.checkStartButton()

        name = self.ui_window_edit.lineEdit_name.text()
        shipType = self.ui_window_edit.comboBox_shipType.currentText()
        hp = self.ui_window_edit.lineEdit_hp.text()
        damage = self.ui_window_edit.lineEdit_damage.text()
        speed = self.ui_window_edit.lineEdit_speed.text()
        if not name:
            self.ui_window_edit.label_warning.setText('Введите название корабля')
        elif not all([hp.isdigit(), damage.isdigit(), speed.isdigit()]):
            self.ui_window_edit.label_warning.setText('HP, урон и скорость должны быть числовыми значениями')
        elif int(hp) + int(damage) + int(speed) > TOTAL_POINTS:
            self.ui_window_edit.label_warning.setText(f'Суммарное количество очков HP, урона и скорости больше {TOTAL_POINTS}')
        else:
            if self.flag == 1:
                setShipValue(self.ship_1, self.ui.label_ship_1)
            else:
                setShipValue(self.ship_2, self.ui.label_ship_2)
            self.ship_window.close()

    def checkStartButton(self):
        if all([self.ship_1.name, int(self.ship_1.hp_points), int(self.ship_1.damage_points), int(self.ship_1.speed_points),
                self.ship_2.name, int(self.ship_2.hp_points), int(self.ship_2.damage_points), int(self.ship_2.speed_points)]):
            self.ui.pushButton_start_battle.setEnabled(True)
        else:
            self.ui.pushButton_start_battle.setEnabled(False)

    def startBattle(self):
        self.ship_1.hp = self.ship_1.hp_start
        self.ship_2.hp = self.ship_2.hp_start
        self.ui.progressBar_ship_1.setValue(100)
        self.ui.progressBar_ship_2.setValue(100)
        self.enableButtons(False)
        self.ui.plainTextEdit.appendPlainText('БОЙ НАЧАЛСЯ!')
        self.thread = BattleThread(self.ship_1, self.ship_2, parent=None)
        self.thread.start()
        self.thread.write_log.connect(self.printLog)
        self.thread.update_hp_1.connect(self.reloadHpBar1)
        self.thread.update_hp_2.connect(self.reloadHpBar2)
        self.thread.enable_buttons.connect(self.enableButtons)

    def printLog(self, text):
        self.ui.plainTextEdit.appendPlainText(text)

    def reloadHpBar1(self, value):
        self.ui.progressBar_ship_1.setValue(value)

    def reloadHpBar2(self, value):
        self.ui.progressBar_ship_2.setValue(value)

    def enableButtons(self, value):
        self.ui.pushButton_start_battle.setEnabled(value)
        self.ui.pushButton_enter_ship_1.setEnabled(value)
        self.ui.pushButton_enter_ship_2.setEnabled(value)
        self.ui.radioButton_sea.setEnabled(value)
        self.ui.radioButton_bay.setEnabled(value)
        self.ui.radioButton_calm.setEnabled(value)
        self.ui.radioButton_storm.setEnabled(value)
        self.ui.radioButton_day.setEnabled(value)
        self.ui.radioButton_night.setEnabled(value)

    def changeLocation(self):
        if self.ui.radioButton_sea.isChecked():
            self.ship_1.speed = self.ship_1.speed * 2
            self.ship_2.speed = self.ship_2.speed * 2
            self.reloadShipInfo()
        else:
            self.ship_1.speed = self.ship_1.speed / 2
            self.ship_2.speed = self.ship_2.speed / 2
            self.reloadShipInfo()

    def changeWeather(self):
        if self.ui.radioButton_calm.isChecked():
            self.ship_1.hp_start = int(self.ship_1.hp_start * 2)
            self.ship_2.hp_start = int(self.ship_2.hp_start * 2)
            self.reloadShipInfo()
        else:
            self.ship_1.hp_start = int(self.ship_1.hp_start / 2)
            self.ship_2.hp_start = int(self.ship_2.hp_start / 2)
            self.reloadShipInfo()

    def changeTime(self):
        if self.ui.radioButton_day.isChecked():
            self.ship_1.damage = int(self.ship_1.damage / 2)
            self.ship_2.damage = int(self.ship_2.damage / 2)
            self.reloadShipInfo()
        else:
            self.ship_1.damage = int(self.ship_1.damage * 2)
            self.ship_2.damage = int(self.ship_2.damage * 2)
            self.reloadShipInfo()

    def openRulesWindow(self):
        self.rules_window = QtWidgets.QDialog(self)
        self.ui_window_rules = Ui_Dialog_rules()
        self.ui_window_rules.setupUi(self.rules_window)
        self.rules_window.show()
        self.ui_window_rules.label_rules_text.setText(
            f'''Игроку необходимо указать название, тип и ТТХ 2-х кораблей,
которые будут участвовать в бою.
Суммарно для всех ТТХ (хп, урон, скорость) доступно 10 очков.
Очки прочности вычисляются по формуле: HP = hp.points x 100.
Очки урона вычисляются по формуле: DMG = dmg.points x 10.
Очки скорости вычисляются по формуле: SPEED = speed.points.
Урон наносится DMG +/-10%.
Очки скорости влияют на вероятность корабля увернуться от получения урона:
шанс_уворота = SPEED х 0,05.
Каждый тип корабля обладает своими уникальными способностями:
Броненосец - получает в два раза меньше урона;
Торпедный катер - имеет удвоенную скорость (SPEED х 2);
Противокорабельная лодка - имеет повышенный урон (DMG x 1.5).
Бухта - скорость кораблей снижается в 2 раза.
Шторм - HP кораблей снижается в 2 раза.
Ночь - урон кораблей увеличивается в 2 раза.''')
        self.ui_window_rules.pushButton_close.clicked.connect(self.rules_window.close)


class BattleThread(QThread):
    write_log = Signal(str)
    update_hp_1 = Signal(int)
    update_hp_2 = Signal(int)
    enable_buttons = Signal(bool)

    def __init__(self, ship_1, ship_2, parent=None):
        super(BattleThread, self).__init__(parent)
        self.ship_1 = ship_1
        self.ship_2 = ship_2

    def run(self):
        def battleIteration(hp_bar, ship_1, ship_2):
            damage = ship_1.dealDamage()
            self.write_log.emit(f"Корабль '{ship_1.name}' атакует на {damage} урона")
            sleep(SLEEP_TIME)
            ship_2.takeDamage(damage)
            if ship_2.damageReceived == 0:
                self.write_log.emit(f"Корабль '{ship_2.name}' уворачивается")
            if not ship_2.isAlive:
                self.write_log.emit(f"Корабль '{ship_2.name}' получает {ship_2.damageReceived} урона\n"
                      f"Корабль '{ship_2.name}' уничтожен!\n"
                      f"Корабль '{ship_1.name}' побеждает в бою!")
                self.write_log.emit(SEPARATOR)
                hp_bar(0)
                self.enable_buttons.emit(True)
                return False
            self.write_log.emit(f"Корабль '{ship_2.name}' получает {ship_2.damageReceived} урона\n"
                  f"Оставшиеся очки прочности корабля '{ship_2.name}' = {ship_2.hp}")
            self.write_log.emit(SEPARATOR)
            hp_bar(ceil(ship_2.hp / ship_2.hp_start * 100))
            sleep(SLEEP_TIME * 2)
            return True

        attack_order = [self.ship_1, self.ship_2]
        hp_bar_order = [self.update_hp_1.emit, self.update_hp_2.emit]
        alive_flag = True
        while alive_flag:
            alive_flag = battleIteration(hp_bar_order[1], *attack_order)
            attack_order.reverse()
            hp_bar_order.reverse()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SeaBattle()
    window.show()

    sys.exit(app.exec())
