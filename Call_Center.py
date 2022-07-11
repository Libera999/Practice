from collections import deque
from abc import ABCMeta, abstractmethod
from random import random

class Call:
    def __init__(self):
        self.caller_num=0
        self.employee_handler_num=0

    def set_handler(self):

    def end_call(self):

class Employee(metaclass=ABCMeta):
    def __init__(self):
        self.name=''
        self.is_free=True

    def receiveCall(self):
        self.free=False
        print(f"This employee {self.name} received the call")

class Respondent(Employee):


class CallHandler:
    def __init__(self):
