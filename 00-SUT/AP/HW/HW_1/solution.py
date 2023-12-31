import re


class Account:
    def __init__(self, username, password, nationalcode, creditcard, email):
        self.username = self.username_validation(username)
        self.password = self.password_validation(password)
        self.nationalcode = self.nationalcode_validation(nationalcode)
        self.creditcard = self.creditcard_validation(creditcard)
        self.email = self.email_validation(email)

    def username_validation(self, username):
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
        else:
            return username

    def password_validation(self, password):
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
        else:
            return password

    def nationalcode_validation(self, nationalcode):
        digits = list(map(int, str(nationalcode)))
        # to check all digits are not the same
        if len(set(digits)) == 1:
            raise Exception("invalid NationalCode")
        else:
            last_digit = digits[-1]
            digits.pop()  # to eliminate the control digit itself
            summation = 0
            for i in range(len(digits)):
                summation += digits[i] * (len(digits) + 1 - i)
            remainder = summation % 11
            if remainder < 2:
                control_digit = remainder
            else:
                control_digit = 11 - remainder
            if last_digit != control_digit:
                raise Exception("invalid NationalCode")
            else:
                return nationalcode

    def creditcard_validation(self, creditcard):
        if not len(creditcard) == 16:
            raise Exception("invalid CreditCard")
        else:
            digits = list(map(int, str(creditcard)))
            summation = 0
            for i in range(len(digits)):
                # the conditions(odd and even indexes) are vice versa because the indexes start from 0
                if i % 2 == 0:
                    temp = digits[i] * 2
                    if temp > 9:
                        temp = temp - 9
                else:
                    temp = digits[i]
                summation += temp
            A = summation % 10
            if A != 0:
                raise Exception("invalid CreditCard")
            else:
                return creditcard

    def email_validation(self, email):
        parts = str(email).split("@")
        # to make sure that there is only one @ in the string
        if len(parts) != 2:
            raise Exception("invalid Email")
        else:
            username = parts[0]
            match_1 = re.match(r"^[a-zA-Z._\d]", username)
            if match_1 is None:
                raise Exception("invalid Email")
            parts = parts[1].split(".")
            if len(parts) != 2:
                raise Exception("invalid Email")
            else:
                domain = parts[0]
                match_2 = re.match(r"^[a-zA-Z]+$", domain)
                match_3 = re.match(r"^[0-9]$", domain)
                if match_2 is None and match_3 is None:
                    raise Exception("invalid Email")
                tld = parts[1]
                match_4 = re.match(r"^[a-zA-Z]{2,3}$", tld)
                if match_4 is None:
                    raise Exception("invalid Email")
                if email.count(".") > 2:
                    raise Exception("invalid Email")

            return email


class Order:
    def __init__(self, name, price, products: dict):
        self.name = name
        self.price = price
        self.products = products
        self.posted = False

    def add_product(self, product, amount, price_product):
        if self.posted is True:
            raise Exception("Unfortunately, your products have been sent by truck and you can't change anything.")
        if product in self.products:
            self.products[product] += amount
            self.price += amount * price_product
        else:
            self.products[product] = amount
            self.price += amount * price_product

    def remove_product(self, product, amount, price_product):
        if self.posted is True:
            raise Exception("Unfortunately, your products have been sent by truck and you can't change anything.")
        if product in self.products:
            if self.products[product] > amount:
                self.price -= amount * price_product
                self.products[product] -= amount
            else:
                raise Exception("The request is over the limit.")

        else:
            return f"{product} is not in your cart."

    def send_order(self):
        self.posted = True
        final = str()
        for key in self.products.items():
            final = final + key[0] + ": " + str(key[1]) + ", "
        return f"Hi {self.name} ,You have ordered {final[0:-2]} and the price will be {self.price}$."
