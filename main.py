from random import uniform, choices
from time import sleep


TOTAL_POINTS = 10  # Доступное игроку количество очков
DODGE_CF = 0.05  # Геймплейный коэффициент уворота на каждое очко скорости
SHIP_TYPES = {
    1: 'Броненосец',
    2: 'Торпедный катер',
    3: 'Противокорабельная лодка'
}
LOCATION_TYPES = {
    1: ['Море', 'скорость кораблей не изменяется'],
    2: ['Бухта', 'скорость кораблей снижается в 2 раза'],
}
WEATHER_TYPES = {
    1: ['Штиль', 'количество HP кораблей не изменяется'],
    2: ['Шторм', 'HP кораблей снижается в 2 раза'],
}
TIME_OF_DAY = {
    1: ['День', 'урон кораблей не изменяется'],
    2: ['Ночь', 'урон кораблей увеличивается в 2 раза'],
}
SLEEP_TIME = 1  # Задержка выведения лога битвы
SEPARATOR = f"{'':-<32}"  # Разделитель в логе итераций боя


class BattleShip:
    def __init__(self, name, ship_type, hp, damage, speed):
        self.name = name
        self.shipType = SHIP_TYPES[ship_type]
        self.hp = hp * 100  # Геймпплейное увеличение очков прочности х100
        self.damage = damage * 15 if self.shipType == 'Противокорабельная лодка' else damage * 10  # Модификатор урона для типа коробля "Противокорабельная лодка"
        self.speed = float(speed * 2) if self.shipType == 'Торпедный катер' else float(speed)
        self._is_alive = True
        self._damage_received = 0  # Начальное значение полученного урона

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def damage_received(self):
        return self._damage_received

    def getInfo(self):
        print(f"{'Корабль':.<17}{self.name}\n"
              f"{'Тип':.<17}{self.shipType}\n"
              f"{'Прочность':.<17}{self.hp}\n"
              f"{'Средний урон':.<17}{self.damage}\n"
              f"{'Скорость':.<17}{self.speed}")

    def dealDamage(self):
        k = round(uniform(0.9, 1.1), 2)  # Коэффициент для создания ВБР при стрельбе +/- 10%
        return round(self.damage * k)

    def takeDamage(self, damage):
        if self.dodgeDamage():
            print(f"Корабль '{self.name}' уворачивается")
            self._damage_received = 0
        else:
            self._damage_received = round(damage / 2) if self.shipType == 'Броненосец' else damage  # Модификатор получения урона для типа коробля "Броненосец"
            self.hp -= self._damage_received
            self._is_alive = True if self.hp > 0 else False

    def dodgeDamage(self):
        return choices((True, False), weights=(self.speed * DODGE_CF, 1 - self.speed * DODGE_CF))[0]


def getRules():
    print(f'Правила игры:\n'
          f'Игроку необходимо указать название, тип и ТТХ 2-х короблей, которые будут участвовать в бою.\n'
          f'Суммарно для всех ТТХ (хп, урон, скорость) доступно {TOTAL_POINTS} очков (значение не может быть = 0)\n'
          f'Очки прочности вычисляются по формуле: HP = hp.points x 100\n'
          f'Очки урона вычисляются по формуле: DMG = dmg.points x 10\n'
          f'Очки скорости вычисляются по формуле: SPEED = speed.points\n'
          f'Урон наносится DMG +/-10%\n'
          f'Очки скорости влияют на вероятность коробля увернуться от получения урона: шанс_уворота = SPEED х 0,05\n'
          f'Каждый тип корабля обладает своими уникальными способностями:\n'
          f'Броненосец - получает в два раза меньше урона\n'
          f'Торпедный катер - имеет удвоенную скорость (SPEED х 2)\n'
          f'Противокорабельная лодка - имеет повышенный урон (DMG x 1.5)\n'
          f'А знаете, где ещё есть танки, авиация и корабли? Конечно же, в...')


def inputDigit():
    while True:
        s = input()
        try:
            return int(s)
        except ValueError:
            print('Введен неправильный тип. Ожидалось целое число.')


def shipPropertyInput():
    name = input('Название корабля:\n')
    print(f'Выберите тип коробля от 1 до {len(SHIP_TYPES)}, где:')
    print(*[f'{key} - {value}' for key, value in SHIP_TYPES.items()], sep='\n')
    ship_type = inputDigit()
    while ship_type not in SHIP_TYPES:
        print('Указанный тип отсутствует, повторите ввод:')
        print(*[f'{key} - {value}' for key, value in SHIP_TYPES.items()], sep='\n')
        ship_type = inputDigit()
    print(f'Укажите ТТХ корабля (доступно {TOTAL_POINTS} очков)')
    print(f'Очки прочности: число от 1 до {TOTAL_POINTS - 2} (итоговое ХП = очки прочности х 10):')
    hp = inputDigit()
    while hp < 1 or hp > TOTAL_POINTS - 2:
        print(f'Указаное количество очков прочности не попадает в диапазон от 1 до {TOTAL_POINTS - 2}')
        hp = inputDigit()
    print(f'Очки урона: число от 1 до {TOTAL_POINTS - hp - 1}')
    damage = inputDigit()
    while damage < 1 or damage > TOTAL_POINTS - hp - 1:
        print(f'Указаное количество очков урона не попадает в диапазон от 1 до {TOTAL_POINTS - hp - 1}')
        damage = inputDigit()
    print('Очки скорости:')
    speed = TOTAL_POINTS - hp - damage
    print(speed)
    return BattleShip(name, ship_type, hp, damage, speed)


def startGame():
    def shipInput(ship_index):
        print(SEPARATOR)
        print(f'Введите данные {ship_index} корабля:')
        ship = shipPropertyInput()
        ship.getInfo()
        print(SEPARATOR)
        return ship

    def environmentInput(env_name, env_types):
        print(f'Выберите тип {env_name} от 1 до {len(env_types)}, где:')
        print(*[f'{key} - {value[0]} ({value[1]})' for key, value in env_types.items()], sep='\n')
        env_type = inputDigit()
        while env_type not in env_types:
            print('Указанный тип отсутствует, повторите ввод:')
            print(*[f'{key} - {value[0]} ({value[1]})' for key, value in env_types.items()], sep='\n')
            env_type = inputDigit()
        return env_type

    ship_1 = shipInput('первого')
    input('нажмите Enter, чтобы продолжить')
    ship_2 = shipInput('второго')
    input('нажмите Enter, чтобы продолжить')
    print(SEPARATOR)
    battle_location = environmentInput('боевой локации', LOCATION_TYPES)
    print(SEPARATOR)
    battle_weather = environmentInput('погоды', WEATHER_TYPES)
    print(SEPARATOR)
    battle_time = environmentInput('времени суток', TIME_OF_DAY)
    print(SEPARATOR)
    if LOCATION_TYPES[battle_location][0] == 'Бухта':
        ship_1.speed = ship_1.speed / 2
        ship_2.speed = ship_2.speed / 2
    if WEATHER_TYPES[battle_weather][0] == 'Шторм':
        ship_1.hp = ship_1.hp // 2
        ship_2.hp = ship_2.hp // 2
    if TIME_OF_DAY[battle_time][0] == 'Ночь':
        ship_1.damage = ship_1.damage * 2
        ship_2.damage = ship_2.damage * 2
    print(f'Боевая локация - {LOCATION_TYPES[battle_location][0]}')
    print(f'Погода - {WEATHER_TYPES[battle_weather][0]}')
    print(f'Время суток - {TIME_OF_DAY[battle_time][0]}')
    print(SEPARATOR)
    ship_1.getInfo()
    print(SEPARATOR)
    ship_2.getInfo()
    print(SEPARATOR)
    input('нажмите Enter, чтобы продолжить')
    print(SEPARATOR)
    print('Бой начался!')
    print(SEPARATOR)
    sleep(SLEEP_TIME * 2)
    return ship_1, ship_2


def battle(battle_ship_1, battle_ship_2):
    def battleIteration(ship_1, ship_2):
        damage = ship_1.dealDamage()
        print(f"Корабль '{ship_1.name}' атакует на {damage} урона")
        sleep(SLEEP_TIME)
        ship_2.takeDamage(damage)
        if not ship_2.is_alive:
            print(f"Корабль '{ship_2.name}' получает {ship_2.damage_received} урона\n"
                  f"Корабль '{ship_2.name}' уничтожен!\n"
                  f"Корабль '{ship_1.name}' побеждает в бою!")
            return False
        print(f"Корабль '{ship_2.name}' получает {ship_2.damage_received} урона\n"
              f"Оставшиеся очки прочности коробля '{ship_2.name}' = {ship_2.hp}")
        print(SEPARATOR)
        sleep(SLEEP_TIME * 2)
        return True

    attack_order = [battle_ship_1, battle_ship_2]
    alive_flag = True
    while alive_flag:
        alive_flag = battleIteration(*attack_order)
        attack_order.reverse()


print('<---BATTLE SHIP, ver. 1.2--->')
start = input('Нажмите Enter, чтобы начать игру (для получения правил игры введите info)\n')
if start == 'info':
    getRules()
    input('Нажмите Enter, чтобы начать игру')
player1, player2 = startGame()
battle(player1, player2)
