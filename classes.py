class Person:

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay

    def talk(self):
        print(self.first,self.pay)


bob=Person("Bob",1,True)
bob.talk()

Jack=Person("Jack", True, 2)
Jack.talk()



