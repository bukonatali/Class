# class School:
#     pass
#
#
# ex = School()
# ex_1 = School()
# ex_1 = School()

class School:
    # Статические поля (переменные класса)
    default_name = 'Natasha'
    default_age = 29

    def __init__(self, name, nationality):
        # Динамические поля (переменные объекта)
        self.name = name
        self.nationality = nationality

    def turn_on(self):
        pass
    def ride(self):
        pass
School_object = School('Maksim', 'belarus')

print(School_object.default_name)
print(School_object.name)

print(dir(School))

    # def print(self):
    #     print("Hello")

# ex = School()
# ex.print()
# ex_1 = School()
# ex_1.print()
# ex_2 = School()
# ex_2.print()










