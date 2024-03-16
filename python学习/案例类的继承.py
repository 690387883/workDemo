class JdCar():
    def __init__(self,carName,carId):
        self.carName=carName
        self.carId=carId

class Taxi(JdCar):
    def __init__(self, carName, carId,comp):
        super().__init__(carName, carId)
        self.comp=comp
    def start(self):
        print('乘客您好！')
        print(f'欢迎乘坐{self.comp},车型是{self.carName},车牌号为{self.carId}')
    def stop(self):
        print('到达目的地')

class MyCar(JdCar):
    def __init__(self, carName, carId,name):
        super().__init__(carName, carId)
        self.name=name
    def start(self):
        print(f'我是{self.name},车型是{self.carName},车牌号为{self.carId}')
    def stop(self):
        print('开心！')

taxi=Taxi('本田','思域','顺丰')
taxi.start()
taxi.stop()

MyCar('本田','额123123','小雷')