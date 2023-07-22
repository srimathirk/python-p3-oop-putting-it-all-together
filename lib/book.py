#!/usr/bin/env python3

class Book:
    def __init__(self,title,page_count):
        self.title = title
        self.page_count = page_count
    
    def get_page_count(self):
        return self._page_count 
    def set_page_count(self,page_count):
        if(type(page_count) is int):
            print(f"pageCount is {page_count}")
            self._page_count = page_count
        else:
            print("page_count must be an integer")
    page_count = property(get_page_count,set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    def get_title(self):
        return self._title
    def set_title(self,title):
        if (type(title) is str):
            self._title = title.title()
            print(f"title after setting is {title}")
        else:
            print("Title is not in titled case")
    title = property(get_title,set_title)


Dr_seuss = Book("hello kids",99)
print(Dr_seuss.title)
print(Dr_seuss.page_count)
Dr_seuss.page_count = 122
print(Dr_seuss.page_count)

