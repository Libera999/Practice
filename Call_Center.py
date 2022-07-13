from collections import deque
from abc import ABCMeta, abstractmethod
from random import random

class Employee(metaclass=ABCMeta):

    def __init__(self, name, free):
            self.name = name
            self.free = free

    def receiveCall(self):
        self.free=False
        print(f"This employee {self.name} received the call")

    def endCall(self):
        self.free=True
        print(f"This employee {self.name} ended the call")

    def escalateCall(self):
        self.free=True
        print(f"This employee {self.name} escalated the call")
        return self.rank+1                                      #to what level to escalate the call

class Director(Employee):
    pass

class Manager(Employee):
     pass

class Respondent(Employee):
     pass


class Call:
    def __init__(self,rank):
        self.rank=rank

class CallHandler:
    def __init__(self,respond,managers,director,call):
         self.respond=respond
         self.managers=managers
         self.director=director
         self.call=call

    def dispatchCall(self):

        if self.call.rank==1:
            free_resp=self.respond.popleft()
            free_resp.receiveCall()
        elif self.call.rank==2:
            free_manager=self.managers.popleft()
            free_manager.receiveCall()
        elif self.call.rank==3:
            self.director.receiveCall()

resp = deque([Respondent("Ann Smith", True), Respondent("John Smith", True)])
managers = deque([Manager("Bill Gates", True), Manager("Dolly Bones", True)])
director = Director("Director", True)

call=Call(rank=1)
callHandle=CallHandler(resp,managers,director,call)
callHandle.dispatchCall()