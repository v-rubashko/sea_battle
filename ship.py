from random import uniform, choices

TOTAL_POINTS = 10  # Доступное игроку количество очков
DODGE_CF = 0.05  # Геймплейный коэффициент уворота на каждое очко скорости


class BattleShip:
    def __init__(self):
        super(BattleShip, self).__init__()
        self.name = ''
        self.shipType = 'Броненосец'
        self.hp_points = 0
        self.damage_points = 0
        self.speed_points = 0
        self.setupShipStats(self.hp_points, self.damage_points, self.speed_points)
        self._isAlive = True
        self._damageReceived = 0  # Начальное значение полученного урона

    def setupShipPoints(self, name, ship_type, hp_points, damage_points, speed_points):
        self.name = name
        self.shipType = ship_type
        self.hp_points = hp_points
        self.damage_points = damage_points
        self.speed_points = speed_points
        self.setupShipStats(int(self.hp_points), int(self.damage_points), int(self.speed_points))

    def setupShipStats(self, hp, damage, speed):
        self.hp_start = hp * 100 # Геймпплейное увеличение очков прочности х100
        self.hp = self.hp_start
        self.damage = damage * 20 if self.shipType == 'ПК лодка' else damage * 10  # Модификатор урона для типа корабля "Противокорабельная лодка"
        self.speed = float(speed * 2) if self.shipType == 'Торп. катер' else float(speed)

    @property
    def isAlive(self):
        return self._isAlive

    @property
    def damageReceived(self):
        return self._damageReceived

    def dealDamage(self):
        k = round(uniform(0.9, 1.1), 2)  # Коэффициент для создания ВБР при стрельбе +/- 10%
        return round(self.damage * k)

    def takeDamage(self, damage):
        if self.dodgeDamage():
            self._damageReceived = 0
            self._isAlive = True
        else:
            self._damageReceived = round(damage / 2) if self.shipType == 'Броненосец' else damage  # Модификатор получения урона для типа корабля "Броненосец"
            self.hp -= self._damageReceived
            self._isAlive = True if self.hp > 0 else False

    def dodgeDamage(self):
        return choices((True, False), weights=(self.speed * DODGE_CF, 1 - self.speed * DODGE_CF))[0]

