import string


class Alphabet:
    def __init__(self, language: str, letters: str):
        self.lang = language
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def __repr__(self):
        return repr(self.letters)

    def size():
        return len(self.letters)


class EngAlphabet(Alphabet):
    __size = len(string.ascii_uppercase)

    def __init__(self):
        super().__init__(language='En', letters=string.ascii_uppercase)

    def is_english_letter(self, letter):
        if letter.upper() in self.letters:
            return True
        return False

    def size(self):
        return type(self).__size

    @staticmethod
    def example():
        print('English Example:\nMy name is Natasha. I  from Belarus')


if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    print(eng_alphabet)
    print(eng_alphabet.size())
    print(eng_alphabet.is_english_letter('Щ'))
    print(eng_alphabet.is_english_letter('F'))
    EngAlphabet.example()
