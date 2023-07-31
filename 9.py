import string


class Alphabet:

    def __init__(self, language, letters_str):
        self.lang = language
        self.letters = list(letters_str)

    # Все буквы алфавита
    def print(self):
        print(self.letters)

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        len(self.letters)


# Английский алфавит
class EngAlphabet(Alphabet):
    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    # Возвращаем количество букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print("English Example:\nMy name is Natasha. I  from Belarus.")


# Тесты
if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('Щ'))
    print(eng_alphabet.is_en_letter('F'))
    EngAlphabet.example()
