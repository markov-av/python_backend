from random import randint


class Car:
    CAR_SPECS = {
        'ferrary': {"max_speed": 340, "drag_coef": 0.324, "time_to_max": 26},
        'bugatti': {"max_speed": 407, "drag_coef": 0.39, "time_to_max": 32},
        'toyota': {"max_speed": 180, "drag_coef": 0.25, "time_to_max": 40},
        'lada': {"max_speed": 180, "drag_coef": 0.32, "time_to_max": 56},
        'sx4': {"max_speed": 180, "drag_coef": 0.33, "time_to_max": 44},
    }

    def __init__(self, name):
        self.name = name
        self.__max_speed = None
        self.__drag_coef = None
        self.__time_to_max = None


    @property
    def max_speed(self):
        if self.__max_speed is None:
            self.__max_speed = self.CAR_SPECS[self.name]['max_speed']
        return self.__max_speed

    @property
    def draq_coef(self):
        if self.__drag_coef is None:
            self.__drag_coef = self.CAR_SPECS[self.name]['drag_coef']
        return self.__drag_coef

    @property
    def time_to_max(self):
        if self.__time_to_max is None:
            self.__time_to_max = self.CAR_SPECS[self.name]['time_to_max']
        return self.__time_to_max


class Wether:

    def __init__(self, wind_speed):
        self.__wind_speed = wind_speed

    @property
    def wind_speed(self):
        return self.__wind_speed


class Competition:
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Competition, cls).__new__(cls)

        return cls.instance

    def __init__(self, distance, competitors, wether):
        self.distance = distance
        self.competitors = competitors
        self.wether = wether

    def start(self):
        for competitor in self.competitors:
            competitor_time = 0
            car = competitor.name

            for distance in range(self.distance):
                _wind_speed = randint(0, self.wether.wind_speed)

                if competitor_time == 0:
                    _speed = 1
                else:
                    _speed = (competitor_time / competitor.time_to_max) * competitor.max_speed
                    if _speed > _wind_speed:
                        _speed -= (competitor.draq_coef * _wind_speed)

                competitor_time += float(1) / _speed

            print("Car <%s> result: %f" % (car, competitor_time))



competitors_name = ('ferrary', 'bugatti', 'toyota', 'lada', 'sx4')
cars = [Car(name) for name in competitors_name]
wether = Wether(wind_speed=20)
competition = Competition(competitors=cars, wether=wether, distance=10000)

competition.start()
