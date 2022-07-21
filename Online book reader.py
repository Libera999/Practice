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

class User_action:
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

class User:
    def __init__(self,id,details):
       self.userid=id
       self.details=details

class Display:
    def __init__(self,book,user):
        self.active_book=book
        self.active_user=user
        self.page=0

    def update_page(self):
        pass

    def display_book(self,book):
        self.page = 0
        self.active_book = book

        self.update_page()

    def next_page(self):
        self.page+=1
        self.update_page()

    def previous_page(self):
        self.page-=1
        self.update_page()



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

