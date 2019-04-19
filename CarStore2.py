#工厂方法模式，基类放一个方法不实现，子类来实现。整个流程已经规定好了，只要调用order就可以下订单。流程在规定
#好的前提下，并且放到了基类里，但是有些方法没有实现（故意不实现），这样在父类里定义方法（接口），在子类里实现方法
#基类里不能确定功能，交给子类定义
class Store(object):
    def select_car(self):
        pass
    def order(self, car_type):
        return self.select_car(car_type)

class BMWCarStore(Store):
    def select_car(self, car_type):
        return BMWFactory.select_car_by_type(car_type)

bmw_store=BMWCarStore()
bmw = bmw_store.order("720li")

class CarStore(Store):
    def select_car(self, car_type):
        return Factory().select_car_by_type(car_type)

class BMWFactory(object):
    def select_car_by_type(self,car_type):
        pass
        # if car_type=="mini":
        #     return Suonata()
        # elif car_type=="720li":
        #     return
class Factory(object):
    def select_car_by_type(self,car_type):
        if car_type=="索纳塔":
            return Suonata()
        elif car_type=="名图":
            return

class Car(object):
    def move(self):
        print("车动")
    def music(self):
        print("车放歌")
    def stop(self):
        print("车停")
class Suonata():
    pass
car_store = CarStore()
car = car_store.order("索纳塔")
car.move()
car.music()
car.stop()