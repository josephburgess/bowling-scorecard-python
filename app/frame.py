class Frame:
    def __init__(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third

    def get_first(self):
        return self.first

    def get_second(self):
        return self.second

    def get_third(self):
        return self.third

    def get_total(self):
        return self.first + self.second + self.third

    def is_strike(self):
        return self.first == 10

    def is_spare(self):
        return self.first != 10 and self.first + self.second == 10
