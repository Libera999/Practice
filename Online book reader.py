class Library:
    def __init__(self,books):
        self.books=books

    def add_book(self,book): #tuple [name, content]
        if self.books.get(book[0])==None:
           self.books.get(book[0],book[1])
           return True
        else:
           return False

b1={
    "Course in miracles":"kgjdfkjkj",
    "Bible":"sjfshf"
    }
reader1=Library(b1)
book1=("Seven sacred weeks","kdfkjgd")
reader1.add_book(book1)
print(reader1)