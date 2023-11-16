class CardHolder():
    def __init__(self, card_num, pin, f_name, l_name, balance):
        self.card_num = str(card_num)
        self.pin = pin
        self.f_name = f_name
        self.l_name = l_name
        self.balance = balance

    # Getter Methods
    def get_card_num(self):
        return self.card_num

    def get_pin(self):
        return self.pin

    def get_fname(self):
        return self.f_name

    def get_lname(self):
        return self.l_name

    def get_balance(self):
        return self.balance

    # Setter Methods
    def set_card_num(self, new_num):
        self.card_num = new_num

    def set_pin(self, new_pin):
        self.pin = new_pin

    def set_fname(self, new_f_name):
        self.f_name = new_f_name

    def set_lname(self, new_l_name):
        self.l_name = new_l_name

    def set_balance(self, new_balance):
        self.balance = new_balance
# 0123
    def print_output(self):
        print(f"Card number:      {self.card_num}")
        print(f"Pin:              **{str(self.pin)[2:]}")
        print(f"Frist name:       {self.f_name}")
        print(f"Last name:        {self.l_name}")
        print(f"Balance:          {self.balance}$")
