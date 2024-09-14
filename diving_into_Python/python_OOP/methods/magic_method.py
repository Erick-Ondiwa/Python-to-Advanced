# Python Magic methods are the methods starting and ending with double underscores ‘__’.
# They are defined by built-in classes in Python and commonly used for operator overloading.
# * These methods allow you to emulate the behavior of built-in types
# They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

class Book:
    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

# This method is used to check for equality between two or more objects
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

# This method is used to check whether certain object attributes are less than the others
    def __lt__(self, other):
        return self.no_of_pages < other.no_of_pages

    def __gt__(self, other):
        return self.no_of_pages < other.no_of_pages

    def __add__(self, other):
        return self.no_of_pages + other.no_of_pages

    def __contains__(self, item):
        return item in self.title or item in self.author

    # This method is used to retrieve an attribute by key
    def __getitem__(self, item):
        return


book1 = Book(title="A Doll's House", author="Henrik Ibsen", no_of_pages=176)
book2 = Book(title="Blossoms of the Savanna", author="H.R Olekulet", no_of_pages=390)
book3 = Book(title="The River and the Source", author="Erick Kondiwa", no_of_pages=402)
book4 = Book(title="The Pearl", author="Martin Luther", no_of_pages=210)
book5 = Book(title="The River Between", author="S.K Erick", no_of_pages=256)

books = [book1, book2, book3, book4, book5]
idx = 0
for book in books:
    # book[2] += 1
    print(book)

print(book1 == book2)
print(book1 < book2)
print(book1 + book2)


