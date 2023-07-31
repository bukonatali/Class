# Два метода в классе, один принимает в себя либо строку, либо число.
# Если передают строку, то смотрим: если произведение гласных и согласных букв меньше или равно
# длине слова, выводить все гласные, иначе согласные
# если число то, произведение суммы чётных цифр на длину числа.
# Длину строки и числа искать во втором методе


vowel = 'яиюэоаыеёу'
class Test:
   def __init__(self):
       pass
   def first(self, item):
       if isinstance(item, str):
           vowelQuan = 0
           vowels = ''
           consonants = ''
           for i in item:
               if i in vowel:
                   vowelQuan += 1
                   vowels += i
               else:
                   consonants += i
           if vowelQuan * (self.second(item) - vowelQuan) <= self.second(item):
               print(vowels)
           else:
               print(consonants)
       elif isinstance(item, int):
           sum = 0
           for i in str(item):
               if int(i) % 2 == 0:
                   sum += int(i)
           print(sum * self.second(str(item)))
   def second(self, item):
       return len(item)
if __name__ == '__main__':
   obj1 = Test()
   obj1.first(369525)
   obj2 = Test()
   obj2.first('Шла Саша по шоссе и сосала сушку')