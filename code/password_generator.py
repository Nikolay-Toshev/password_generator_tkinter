import random
import string


class PassWord:

    def __init__(self, password_length: int, number: int, special_symbol: int):
        self.password_length = password_length
        self.number = number
        self.special_symbol = special_symbol
        self.letters_ascii = string.ascii_letters
        self.numbers_ascii = string.digits
        self.symbols_ascii = "!@#$%&*"

    def is_input_correct(self):
        if self.number + self.special_symbol <= self.password_length:
            return True
        return False

    def add_numbers(self):
        pass_nums = []
        for i in range(self.number):
            pass_nums.append(random.choice(self.numbers_ascii))
        return pass_nums

    def add_symbol(self):
        pass_symbols = []
        for i in range(self.special_symbol):
            pass_symbols.append(random.choice(self.symbols_ascii))
        return pass_symbols

    def add_letter(self):
        pass_letters = []

        if self.is_input_correct():
            number_of_letters = self.password_length - self.number - self.special_symbol

            for i in range(number_of_letters):
                pass_letters.append(random.choice(self.letters_ascii))

            return pass_letters

    def get_password(self):
        if self.is_input_correct():

            raw_password = self.add_letter() + self.add_numbers() + self.add_symbol()
            password = ''
            while raw_password:
                password += random.choice(raw_password)
                raw_password.remove(password[-1])

            return password
        return 'Wrong input'


def generate(password_length, number, special_symbol, number_of_passwords, ):
    passwords = []
    for i in range(number_of_passwords):
        password = PassWord(password_length, number, special_symbol)
        passwords.append(password.get_password())
    return '\n\n'.join(passwords)
