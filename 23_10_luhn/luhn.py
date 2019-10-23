class Luhn():
    def __init__(self, cc_number):
        self.cc_number = cc_number
        self.seconds = []
        self.firsts = []

    def check(self):
        self.clean()
        self.select_digits()
        self.double_seconds()

        total_sum = sum(self.firsts) + sum(self.seconds)
        return total_sum % 10 == 0
    
    def clean(self):
        self.cc_number = self.cc_number.replace(' ', '').replace('-', '')

    def select_digits(self):
        for idx, number in enumerate(self.cc_number[::-1]):
            if (idx % 2) != 0:
                self.seconds.append(int(number))
            else:
                self.firsts.append(int(number))

    def double_seconds(self):
        self.seconds = [number*2 - 9 if number*2 > 9 else number*2 for number in self.seconds] 
