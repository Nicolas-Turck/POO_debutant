from book import *
from books_list import *
class Library():
    """class for range book objet and select it and return it """
    def __init__(self):
        self.book_all = list()
        #self.title = title

    def add_book(self, book):
        """method for add book in the library """
        self.book_all.append(book)
        #self.book_all.append(book)
        #Library(book_all)
        #print(book_all)
        

    def get_book(self, title):
        """method for verify is book is in library and return it to reader"""
        print(title)
        #print(book)
        #book.library(book)
        for book in self.book_all:
            #print(book_all)
            if title == book.title:
                print(book.__dict__)
                print(book.pages)
                return book
            else:
                 print("not found")                
            #if title != self.book:
                #print("non")
                
                #print(book)
           
                   
        
            
                
               
            

