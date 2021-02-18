class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police == True:
            print(f'{self.color.title()} {self.name} {self.model} '
                  f'Полиция там {self.road_type}')
        else:
            print(f'{self.color.title()} {self.name} {self.model} '
                  f'туда {self.road_type}')

    def stop(self):
        print('Стой')

    def turn(self, direction):
        print(f'Поверни {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed} km/h')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 60 and self.road_type != 'трасса':
            print('ПРЕДУПРЕЖДЕНИЕ НЕ РАЗГОНЯЙСЯ')
        elif self.speed > 110:
            print('ПРЕДУПРЕЖДЕНИЕ НЕ РАЗГОНЯЙСЯ')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 60 and self.road_type != 'трасса':
            print('ПРЕДУПРЕЖДЕНИЕ НЕ РАЗГОНЯЙСЯ')
        elif self.speed > 110:
            print('ПРЕДУПРЕЖДЕНИЕ НЕ РАЗГОНЯЙСЯ')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type

    def speed_limit(self):
        if self.speed > 40:
            print('ПРЕДУПРЕЖДЕНИЕ НЕ РАЗГОНЯЙСЯ')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police, model, road_type):
        super().__init__(speed, color, name, is_police)
        self.model = model
        self.road_type = road_type


car1 = TownCar(65, 'красный', 'Toyota', False, 'Camry', 'улица')
car1.go()
car1.show_speed()
car1.speed_limit()
car1.turn('на лево')
car1.stop()

print()
car2 = SportCar(100, 'черный', 'Ferrari', False, 'F40', 'трасса')
car2.go()
car2.show_speed()
car2.speed_limit()
car2.turn('на право')
car2.speed = 70
car2.show_speed()
car2.turn('на лево')
car2.speed = 150
car2.show_speed()
car2.speed_limit()

print()
car3 = WorkCar(45, 'черный', 'Volvo', False, 'FH16', 'улица')
car3.go()
car3.show_speed()
car3.speed_limit()
car3.stop()

print()
car4 = PoliceCar(100, 'красный', 'Ford', True, 'Полиция', 'улица')
car4.go()
car4.show_speed()
car4.stop()