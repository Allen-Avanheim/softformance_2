from string import punctuation


class PasswordChecker:
    """
    The program accepts a sequence of comma-separated transaction passwords
    and checks them according to the bank's criteria.
    Passwords that match the criteria will be printed separated by commas.
    """
    __valid_passwords = []

    def __init__(self, passwords):
        self.__passwords = passwords.split(',')

    @staticmethod
    def __check_length(password: str) -> bool:
        len_of_password = len(password)
        first_condition = len_of_password > 6
        second_condition = len_of_password < 4
        return first_condition or second_condition

    @staticmethod
    def __check_spaces(password: str) -> bool:
        if len(password) != len(password.replace(' ', '')):
            return True
        return False

    @staticmethod
    def __check_password(password_to_check: str) -> bool:
        is_upper = False
        is_lower = False
        is_digit = False
        is_sign = False
        for char in password_to_check:
            if char.isupper():
                is_upper = True
            if char.islower():
                is_lower = True
            if char.isdigit():
                is_digit = True
            if char in punctuation:
                is_sign = True
            if is_sign and is_upper and is_lower and is_digit:
                return True
        return False

    def __check_passwords(self) -> None:
        for password in self.__passwords:
            if self.__check_length(password) or self.__check_spaces(password):
                continue
            if self.__check_password(password):
                self.__valid_passwords.append(password)

    def print_valid_passwords(self) -> None:
        self.__check_passwords()
        print(','.join(self.__valid_passwords))


if __name__ == '__main__':
    string_of_passwords = input()
    password_checker = PasswordChecker(string_of_passwords)
    password_checker.print_valid_passwords()
