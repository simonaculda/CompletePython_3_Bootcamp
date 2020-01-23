class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):  # returns the string representation of an object
        return f"{self.title} by {self.author} "

    def __len__(self):  # return the length
        return self.pages

    def __del__(self):
        print("A book object has been deleted")


b = Book('Python', 'Simona', 200)
print(b)
print(len(b))
del b
#print(b)

