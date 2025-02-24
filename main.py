from random import random, choices
from time import sleep


TOTAL_POINTS = 10
SHIP_TYPES = {1: "Броненосец",
              2: "Торпедный катер",
              3: "Противокорабельная лодка"}
SLEEP_TIME = 1


class BattleShip:
    def __init__(self, name , ship_type, hp, damage, speed):
        self.name = name
        self.ship_type = ship_type
        self.hp = hp
        self.damage = damage
        self.speed = speed

    @property
    def ship_type(self):
        return self._ship_type

    @ship_type.setter
    def ship_type(self, ship_type):
        types = SHIP_TYPES
        self._ship_type = types[ship_type]

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp * 100
        self.is_alive = True
        self.damage_received = 0

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage * 15 if self.ship_type == "Противокорабельная лодка" else damage * 10

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed * 2 if self.ship_type == "Торпедный катер" else speed

    def get_info(self):
        print(f"{'Корабль':.<17}{self.name}\n"
              f"{'Тип':.<17}{self._ship_type}\n"
              f"{'Прочность':.<17}{self._hp}\n"
              f"{'Средний урон':.<17}{self._damage}\n"
              f"{'Скорость':.<17}{self._speed}")

    def deal_damage(self):
        k = random() * (11 - 9) + 9
        return round(self._damage * round(k, 1) * 0.1)

    def take_damage(self, damage):
        if self.dodge_damage():
            print(f"Корабль '{self.name}' уворачивается")
            self.damage_received = 0
        else:
            self.damage_received = round(damage / 2) if self._ship_type == "Броненосец" else damage
            self._hp -= self.damage_received
            self.is_alive = True if self._hp > 0 else False

    def dodge_damage(self):
        return (choices((True, False), weights=(self.speed * 0.05, 1 - self.speed * 0.05))[0])


def get_rules():
    print(f"Правила игры:\n"
          f"Игроку необходимо указать название, тип и ТТХ 2-х короблей, которые будут участвовать в бою.\n"
          f"Суммарно для всех ТТХ (хп, урон, скорость) доступно {TOTAL_POINTS} очков (значение не может быть = 0)\n"
          f"Очки прочности вычисляются по формуле: HP = hp.points x 100\n"
          f"Очки урона вычисляются по формуле: DMG = dmg.points x 10\n"
          f"Очки скорости вычисляются по формуле: SPEED = speed.points\n"
          f"Урон наносится DMG +/-10%\n"          
          f"Очки скорости влияют на вероятность коробля увернуться от получения урона: шанс_уворота = SPEED х 0,05\n"
          f"Каждый тип корабля обладает своими уникальными способностями:\n"
          f"Броненосец - получает в два раза меньше урона\n"
          f"Торпедный катер - имеет удвоенную скорость (SPEED х 2)\n"
          f"Противокорабельная лодка - имеет повышенный урон (DMG x 1.5)\n"
          f"А знаете, где ещё есть танки, авиация и корабли? Конечно же, в...")


def input_digit():
    while True:
        s = input()
        try:
            return int(s)
        except ValueError:
            print('Введен неправильный тип. Ожидалось целое число.')


def ship_input():
    name = input("Название корабля:\n")
    print(f"Выберите тип коробля от 1 до {len(SHIP_TYPES)}, где:")
    print(*[f"{key} - {value}" for key, value in SHIP_TYPES.items()], sep="\n")
    ship_type = input_digit()
    while ship_type not in SHIP_TYPES:
        print("Указанный тип отсутствует, повторите ввод")
        print(*[f"{key} - {value}" for key, value in SHIP_TYPES.items()], sep="\n")
        ship_type = input_digit()
    print(f"Укажите ТТХ корабля (доступно {TOTAL_POINTS} очков)")
    print(f"Очки прочности: число от 1 до {TOTAL_POINTS - 2} (итоговое ХП = очки прочности х 10):")
    hp = input_digit()
    while hp < 1 or hp > TOTAL_POINTS - 2:
        print(f"Указаное количество очков прочности не попадает в диапазон от 1 до {TOTAL_POINTS - 2}")
        hp = input_digit()
    print(f"Очки урона: число от 1 до {TOTAL_POINTS - hp - 1}")
    damage = input_digit()
    while damage < 1 or damage > TOTAL_POINTS - hp - 1:
        print(f"Указаное количество очков урона не попадает в диапазон от 1 до {TOTAL_POINTS - hp - 1}")
        damage = input_digit()
    print(f"Очки скорости:")
    speed = TOTAL_POINTS - hp - damage
    print(speed)
    return name, ship_type, hp, damage, speed


def start_game():
    print(f"{"":-<32}")
    print(f"Введите данные первого корабля")
    input_1 = ship_input()
    ship_1 = BattleShip(input_1[0], input_1[1], input_1[2], input_1[3], input_1[4])
    ship_1.get_info()
    print(f"{"":-<32}")
    input("нажмите Enter, чтобы продолжить")
    print(f"{"":-<32}")
    print("Введите данные второго корабля")
    input_2 = ship_input()
    ship_2 = BattleShip(input_2[0], input_2[1], input_2[2], input_2[3], input_2[4])
    ship_2.get_info()
    print(f"{"":-<32}")
    print("Бой начался!")
    print(f"{"":-<32}")
    sleep(SLEEP_TIME * 2)
    return ship_1, ship_2


def battle(battle_ship_1, battle_ship_2):
    while True:
        damage = battle_ship_1.deal_damage()
        print(f"Корабль '{battle_ship_1.name}' атакует на {damage} урона")
        sleep(SLEEP_TIME)
        battle_ship_2.take_damage(damage)
        if not battle_ship_2.is_alive:
            print(f"Корабль '{battle_ship_2.name}' получает {battle_ship_2.damage_received} урона")
            print(f"Корабль '{battle_ship_2.name}' уничтожен!\n"
                  f"Корабль '{battle_ship_1.name}' побеждает в бою!")
            break
        print(f"Корабль '{battle_ship_2.name}' получает {battle_ship_2.damage_received} урона\n"
              f"Оставшиеся очки прочности коробля '{battle_ship_2.name}' = {battle_ship_2.hp}")
        print(f"{"":-<32}")
        sleep(SLEEP_TIME * 2)
        damage = battle_ship_2.deal_damage()
        print(f"Корабль '{battle_ship_2.name}' атакует на {damage} урона")
        sleep(SLEEP_TIME)
        battle_ship_1.take_damage(damage)
        if not battle_ship_1.is_alive:
            print(f"Корабль '{battle_ship_1.name}' получает {battle_ship_1.damage_received} урона\n"
                  f"Корабль '{battle_ship_1.name}' уничтожен!\n"
                  f"Корабль '{battle_ship_2.name}' побеждает в бою!")
            break
        print(f"Корабль '{battle_ship_1.name}' получает {battle_ship_1.damage_received} урона\n"
              f"Оставшиеся очки прочности коробля '{battle_ship_1.name}' = {battle_ship_1.hp}")
        print(f"{"":-<32}")
        sleep(SLEEP_TIME * 2)
print("<---BATTLE SHIP, ver. 1.0--->")


start = input("Нажмите Enter, чтобы начать игру (для получения правил игры введите info)\n")
if start == "info":
    get_rules()
    input("Нажмите Enter, чтобы начать игру")
player1 , player2 = start_game()
battle(player1, player2)