
# __init__是初始化方法，方法中第一个参数必须是self，类似于js中的constructor，每个方法里面必须包含self
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
# dog1=Dog('旺财',3)
# dog2=Dog('大黄',2)
# print('你叫{0}，今年{1}'.format(dog1.name,dog1.age))
# print('你叫{0}，今年{1}'.format(dog2.name,dog2.age))


# 案例1
# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def eat(self,food):
#         print('{0}在吃{1}'.format(self.name,food))
#     def say(self):
#         print('汪汪汪')

# bigDog=Dog('旺财',3)
# bigDog.eat('骨头')
# bigDog.say()

# 案例2 类自身的变量及方法 classmethod类方法，类方法里面不能访问其他方法中变量 类私有变量加双下划线 __name
# class Dog():
#     person = '小雷'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def eat(cls,name):
#         print('{0}的狗{1}在吃骨头'.format(cls.person,name))

# bigDog=Dog('旺财',3)
# bigDog.eat('dd')

# class Dog():
#     person = '小雷'
#     def __init__(self,name):
#         self.__name=name
#     def eat(self):
#         print('{0}的狗{1}在吃骨头'.format(self.__name,Dog.person))
#     def __say(self):
#         print('汪汪汪')
#     def des(self):
#         self.__say()

# bigDog=Dog('旺财')
# bigDog.eat()
# bigDog.des()


# property修饰符，搭配setter，解决私有化变量被访问和修改
# class Dog():
#     def __init__(self,name,food):
#         self.__name=name
#         self.__food=food
#     def eat(self):
#         print('{0}在吃{1}'.format(self.__name,self.__food))
#     @property
#     def food(self):
#         return self.__food
#     @food.setter
#     def food(self,value):
#         self.__food=value

# bigDog=Dog('旺财','骨头')
# bigDog.eat()
# bigDog.food='屎'
# bigDog.eat()

# super关键字
class Animal:
    def __init__(self,name,food):
        self.__name=name
        self.__food=food
    def eat(self):
        print('{0}在吃{1}'.format(self.__name,self.__food))
class cat(Animal):
    def __init__(self,name,food):
        super().__init__(name,food)
        self.name=name
    # def eat(self):
    #     print('{0}hahaha'.format(self.name))

bigCat=cat('Tom','鱼')
bigCat.eat()