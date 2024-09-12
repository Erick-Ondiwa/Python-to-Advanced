# Python Magic methods are the methods starting and ending with double underscores ‘__’.
# They are defined by built-in classes in Python and commonly used for operator overloading.
#
# They are also called Dunder methods, Dunder here means “Double Under (Underscores)”.

class Book:
    def __init__(self, title, author, no_of_pages):
        self.title = title
        self.author = author
        self.no_of_pages = no_of_pages

    def __str__(self):
        return f"{self.title} by {self.author}"


book1 = Book(title="A Doll's House", author="Henrik Ibsen", no_of_pages=176)
print(book1)

