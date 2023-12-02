#!/usr/bin/env python3

class Book:
    pass
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def is_page_count_integer(self):
        return isinstance(self.page_count, int)
    