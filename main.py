from random import uniform, choices
from time import sleep


TOTAL_POINTS = 10  # Доступное игроку количество очков
DODGE_CF = 0.05  # Геймплейный коэффициент уворота на каждое очко скорости
SHIP_TYPES = {
    1: 'Броненосец',
    2: 'Торпедный катер',
    3: 'Противокорабельная лодка'
}
SLEEP_TIME = 1  # Задержка выведения лога битвы
SEPARATOR = f'{'':-<32}'  # Разделитель в логе итераций боя


class BattleShip:
    def __init__(self, name, ship_type, hp, damage, speed):
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
        self._ship_type = SHIP_TYPES[ship_type]

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, hp):
        self._hp = hp * 100  # Геймпплейное увеличение очков прочности х100
        self.is_alive = True
        self.damage_received = 0  # Начальное значение полученного урона

    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, damage):
        self._damage = damage * 15 if self.ship_type == 'Противокорабельная лодка' else damage * 10  # Модификатор урона для типа коробля "Противокорабельная лодка"

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        self._speed = speed * 2 if self.ship_type == 'Торпедный катер' else speed  # Модификатор скорости для типа коробля "Торпедный катер"

    def get_info(self):
        print(f'{'Корабль':.<17}{self.name}\n'
              f'{'Тип':.<17}{self._ship_type}\n'
              f'{'Прочность':.<17}{self._hp}\n'
              f'{'Средний урон':.<17}{self._damage}\n'
              f'{'Скорость':.<17}{self._speed}')

    def deal_damage(self):
        k = round(uniform(0.9, 1.1), 2)  # Коэффициент для создания ВБР при стрельбе +/- 10%
        return round(self._damage * k)

    def take_damage(self, damage):
        if self.dodge_damage():
            print(f'Корабль "{self.name}" уворачивается')
            self.damage_received = 0
        else:
            self.damage_received = round(damage / 2) if self._ship_type == 'Броненосец' else damage  # Модификатор получения урона для типа коробля "Броненосец"
            self._hp -= self.damage_received
            self.is_alive = True if self._hp > 0 else False

    def dodge_damage(self):
        return choices((True, False), weights=(self.speed * DODGE_CF, 1 - self.speed * DODGE_CF))[0]


def get_rules():
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


def input_digit():
    while True:
        s = input()
        try:
            return int(s)
        except ValueError:
            print('Введен неправильный тип. Ожидалось целое число.')


def ship_property_input():
    name = input('Название корабля:\n')
    print(f'Выберите тип коробля от 1 до {len(SHIP_TYPES)}, где:')
    print(*[f'{key} - {value}' for key, value in SHIP_TYPES.items()], sep='\n')
    ship_type = input_digit()
    while ship_type not in SHIP_TYPES:
        print('Указанный тип отсутствует, повторите ввод')
        print(*[f'{key} - {value}' for key, value in SHIP_TYPES.items()], sep='\n')
        ship_type = input_digit()
    print(f'Укажите ТТХ корабля (доступно {TOTAL_POINTS} очков)')
    print(f'Очки прочности: число от 1 до {TOTAL_POINTS - 2} (итоговое ХП = очки прочности х 10):')
    hp = input_digit()
    while hp < 1 or hp > TOTAL_POINTS - 2:
        print(f'Указаное количество очков прочности не попадает в диапазон от 1 до {TOTAL_POINTS - 2}')
        hp = input_digit()
    print(f'Очки урона: число от 1 до {TOTAL_POINTS - hp - 1}')
    damage = input_digit()
    while damage < 1 or damage > TOTAL_POINTS - hp - 1:
        print(f'Указаное количество очков урона не попадает в диапазон от 1 до {TOTAL_POINTS - hp - 1}')
        damage = input_digit()
    print('Очки скорости:')
    speed = TOTAL_POINTS - hp - damage
    print(speed)
    return BattleShip(name, ship_type, hp, damage, speed)


def start_game():
    def ship_input(ship_index):
        print(SEPARATOR)
        print(f'Введите данные {ship_index} корабля')
        ship = ship_property_input()
        ship.get_info()
        print(SEPARATOR)
        return ship

    ship_1 = ship_input('первого')
    input('нажмите Enter, чтобы продолжить')
    ship_2 = ship_input('второго')
    print('Бой начался!')
    print(SEPARATOR)
    sleep(SLEEP_TIME * 2)
    return ship_1, ship_2


def battle(battle_ship_1, battle_ship_2):
    def battle_iteration(ship_1, ship_2):
        damage = ship_1.deal_damage()
        print(f'Корабль "{ship_1.name}" атакует на {damage} урона')
        sleep(SLEEP_TIME)
        ship_2.take_damage(damage)
        if not ship_2.is_alive:
            print(f'Корабль "{ship_2.name}" получает {ship_2.damage_received} урона\n'
                  f'Корабль "{ship_2.name}" уничтожен!\n'
                  f'Корабль "{ship_1.name}" побеждает в бою!')
            return False
        print(f'Корабль "{ship_2.name}" получает {ship_2.damage_received} урона\n'
              f'Оставшиеся очки прочности коробля "{ship_2.name}" = {ship_2.hp}')
        print(SEPARATOR)
        sleep(SLEEP_TIME * 2)
        return True

    attack_order = [battle_ship_1, battle_ship_2]
    alive_flag = True
    while alive_flag:
        alive_flag = battle_iteration(*attack_order)
        attack_order.reverse()


print('<---BATTLE SHIP, ver. 1.1--->')
start = input('Нажмите Enter, чтобы начать игру (для получения правил игры введите info)\n')
if start == 'info':
    get_rules()
    input('Нажмите Enter, чтобы начать игру')
player1, player2 = start_game()
battle(player1, player2)
