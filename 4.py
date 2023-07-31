# демонстрирующий работу разных видов методов класса

# методы экземпляра
class Class:
    def print(self):
        print("Hello")

ex = Class()
ex_1 = Class()
ex_1.print()

# статические методы
class Class():
    @staticmethod
    def staticmethod():
        print('static method')
class children_Class(Class):
    pass
my_obj = Class()
my_obj.staticmethod()
my_obj_1 = children_Class()
my_obj_1.staticmethod()



# методы класса
class Class():
    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.TOTAL_OBJECTS)
class ChildClass(Class):
    TOTAL_OBJECTS=0
    def __init__(self):
        ChildClass.TOTAL_OBJECTS = ChildClass.TOTAL_OBJECTS + 1
    pass
# Создаем объекты
my_obj1 = ChildClass()
my_obj2 = Class()
my_obj3 = Class()
# Вызываем classmethod
ChildClass.total_objects()







