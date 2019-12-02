from book import *
from books_list import *
class Library():
    """class for range book objet and select it and return it """
    def __init__(self):
        self.book_all = list()
        
    def add_book(self, book):
        """method for add book in the library """
        self.book_all.append(book)
        
    def get_book(self, title):
        """method for verify is book is in library and return it to reader"""
        print(title)
        
        for book in self.book_all:
            
            if title == book.title:
                return book
            else:
                 print("not found")                
            
           
                   
        
            
                
               
            

