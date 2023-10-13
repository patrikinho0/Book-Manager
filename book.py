class Book:
    def __init__(self, ISBN, name, description, publish_year, author, price):
        self.ISBN = ISBN
        self.name = name
        self.description = description
        self.publish_year = publish_year
        self.author = author
        self.price = price

    def to_dict(newBook):
        newBook_dict = {
            "isbn": newBook.ISBN,
            "name": newBook.name,
            "description": newBook.description,
            "publish_year": newBook.publish_year,
            "author": newBook.author,
            "price": newBook.price
        }
        return newBook_dict