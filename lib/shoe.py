#!/usr/bin/env python3

class Shoe:
    pass
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = 'New'

    def cobble(self):
        self.condition = 'New'
        print("Your shoe is as good as new!")

    def is_size_integer(self):
        return isinstance(self.size, int)