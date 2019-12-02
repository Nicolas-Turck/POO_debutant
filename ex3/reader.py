# coding: utf8
from library import *
class Reader():
    """class for the reader select and reead the book"""
    def __init__(self):
        self.book = None
        self.pages = 0
        self.current_pages = 0
        
        

    def borrow_book(self, Library, title):
        """method for verify is title si in list book 
        and got to method get book in class Library"""
        self.book=Library.get_book(title)
        if self.book is None:
            try:
                pass
                
            except book_error as identifier:
                pass
            else:
                self.pages=1
                
        
       
        
    def go_to_page(self, pages):
        """ method for go to pages selected"""
        if current_pages !=  pages:
            current_pages = pages
            read(pages)
    
    def next_page(self):
        """method for go to the next page  """
        self.page = pages+1
        current_pages = pages
        read(pages)

    def previous_page(self):
        """method for return previous page"""
        self.page = pages-1
        current_pages = pages
        read(pages)

    def read(self, pages):
        """method for display the current page """
        print(current_pages)
        print("read the page............")
        

    def read_book(self):
        """method for book is open while the book is not finish"""
        while self.current_pages != len(self.book.pages):
            self.current_pages += 1
            print("read")
        else:
            print("you finish the book ")
        
