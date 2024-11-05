class LibraryItem:
    def __init__(self, ID):
        self.ID = ID

    def __str__(self):
        return f'Item with ID: {self.ID}'

class Book(LibraryItem):
    def __init__(self, ID, title, author, ISBN):
        super().__init__(ID)
        self.title = title
        self.author = author
        self.ISBN = ISBN

    def __str__(self):
        return super().__str__() + f' is a book with title {self.title}, author {self.author} and ISBN {self.ISBN}.'
    
class DVD(LibraryItem):
    def __init__(self, ID, title, director, release_date):
        super().__init__(ID)
        self.title = title
        self.director = director
        self.release_date = release_date

    def __str__(self):
        return super().__str__() + f' is a DVD with title {self.title}, director {self.director} and release date {self.release_date}.'
    
class Magazine(LibraryItem):
    def __init__(self, ID, title, issue, publisher):
        super().__init__(ID)
        self.title = title
        self.issue = issue
        self.publisher = publisher

    def __str__(self):
        return super().__str__() + f' is a magazine with title {self.title}, issue {self.issue} and publisher {self.publisher}.'
    
items = [Book(1, 'The Hobbit', 'J.R.R. Tolkien', '978-0-395-07122-1'), DVD(2, 'The Godfather', 'Francis Ford Coppola', '1972'), Magazine(3, 'National Geographic', 'March 2021', 'National Geographic Society')]
for item in items:
    print(item)
