import re


class Account:
    def __init__(self, username:str, password:str, nationalcode, creditcard, email):
        self.unsername = username
        self.password = password
        self.nationalcode = nationalcode
        self.creditcard = creditcard
        self.email = email
        pass

    def username_validation(self, username: str) -> None:
        '''
        we check the username to meet the desired condition. It should start with at least 1 letter ( upper or lower
        case), followed by either a "." or "_" , then again letters and finish.
         :param username: -
         :return: if the username is not ok raise an Exception
        '''
        regex_pattern = r"^[a-zA-Z]+[._][a-zA-Z]+$"
        match = re.match(regex_pattern, username)
        if match is None:
            raise Exception("invalid UserName")

    def password_validation(self, password: str) -> None:
        '''
        here we check that the password should have at least 1 lowercase letter, one uppercase letter,one digit and
        one of the symbols.Then we make sure that it is a combination of them with more than 8 characters.
         :param password: -
         :return: if the password is not ok raise an Exception
        '''
        regex_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$])[A-Za-z\d!@#$]{8,}$"
        match = re.match(regex_pattern, password)
        if match is None:
            raise Exception("invalid Password")

    def nationalcode_validation(self, nationalcode):
        nationalcode=str(nationalcode)
        sum=0
        for i in nationalcode:
            sum+= i * (len(nationalcode)-i.index()



    def creditcard_validation(self, creditcard):
        pass

    def email_validation(self, email):
        pass


class Order:
    def __init__(self, name, price, products):
        pass

    def add_product(self, product, amount, price_product):
        pass

    def remove_product(self, product, amount, price_product):
        pass

    def send_order(self):
        pass
