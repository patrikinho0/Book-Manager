import unittest
from book import Book
from utils import *
import json
import os


class TestMathMethods(unittest.TestCase):
    
    def setUp(self):
          self.sample_book = {
            "isbn": 30,
            "name": "Potop",
            "description": "opis",
            "publish_year": 1928,
            "author": "Henryk Sienkiewicz",
            "price": 40
        }
    def test_add_book(self):
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_directory, "books.json")
        
        existing_data = []
        switch = False
            
        add_new_book(
             self.sample_book["isbn"],
             self.sample_book["name"],
             self.sample_book["description"],
             self.sample_book["publish_year"],
             self.sample_book["author"],
             self.sample_book["price"]
          )
        
        with open(path, 'r') as file:
            existing_data = json.load(file)
        
        for element in existing_data:
                if element.get("name") == existing_data[-1].get("name"):
                    switch = True
                else:
                    switch = False
        self.assertTrue(switch)

    def test_display_all_books(self):

          switch = False

          displayed_data = display_all_books()

          for element in displayed_data:
               if element != None:
                    switch = True
               else:
                    switch = False
          self.assertTrue(switch)

    def test_display_lower_price(self):
         
         switch = False

         lower_priced_books = display_lower_price(50)

         for element in lower_priced_books:
              if element != None:
                   switch = True
              else:
                   switch = False
         self.assertTrue(switch)
    
    def test_display_higher_price(self):
         
         switch = False

         higher_priced_books = display_higher_price(50)

         for element in higher_priced_books:
              if element != None:
                   switch = True
              else:
                   switch = False
         self.assertTrue(switch)
    
    def test_display_author_books(self):
         
         switch = False

         author_books = display_author_books("Slowacki")

         for element in author_books:
              if element != None:
                   switch = True
              else:
                   switch = False
         self.assertTrue(switch)
    
    def test_display_lower_year(self):
         
         switch = False

         lower_year_books = display_lower_year(1900)

         for element in lower_year_books:
              if element != None:
                   switch = True
              else:
                   switch = False
         self.assertTrue(switch)


    
    def test_display_higher_year(self):
         
         switch = False

         higher_year_books = display_higher_year(1900)

         for element in higher_year_books:
              if element != None:
                   switch = True
              else:
                   switch = False
         self.assertTrue(switch)

if __name__ == '__main__':
    unittest.main()