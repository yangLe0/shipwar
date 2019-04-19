#简单工厂模式，通过一个类达到解耦的模式

class CarStore(object):
    def __init__(self):
        self.factory = Factory()
    def order(self, car_type):
        return self.factory.select_car_by_type(car_type)

class Factory(object):
    def select_car_by_type(self,car_type):
        if car_type=="索纳塔":
            return Suonata()
        elif car_type=="ix35":
            return Ix35()
        elif car_type=="名图":
            return Mingtu()

class Car(object):
    def move(self):
        print("车动")
    def music(self):
        print("车放歌")
    def stop(self):
        print("车停")

class Suonata(Car):
    pass
class Ix35(Car):
    pass
class Mingtu(Car):
    pass
car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()