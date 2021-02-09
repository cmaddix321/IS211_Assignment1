class Book:

  def __init__(self, author="", title=""):
    self.author = author
    self.title = title

  def display(self):
    print(self.title + " written by " + self.author)

if __name__ == "__main__":
    pass


x = Book("John Steinbeck","Of Mice and Men")
y = Book("Harper Lee","To Kill a Mockingbird")

x.display()
y.display()
