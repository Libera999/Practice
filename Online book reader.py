class Library:
    def __init__(self,books):
        self.books=books

    def add_book(self,book):           #tuple [name, content]
        if self.books.get(book[0])==None:
           self.books[book[0]]=book[1]
           return True
        else:
           return False

    def remove_book(self,book_name): #remove by name
        if self.books.get(book_name)!=None:
            del[self.books[book_name]]
            return True
        else:
            return False

    def find_book(self, book_name):     #find by name, return content
        return self.books.get(book_name)

class User:
    def __init__(self,users):
        self.users=users  #{id: user name}

    def add_user(self,id,user):
        if self.users.get(id)==None:
            self.users[id]=user
            return True
        else:
            return False

    def delete_user(self,id,user):
        if self.users.get(id)!=None:
            del[self.users[id]]
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
print(reader1.books)

r=reader1.find_book(book1[0])
print(r)

