from abc import ABC, abstractmethod


class Duck(ABC):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
    def fly(self):
        print("fly")

    @abstractmethod
    def quack(self):
        raise NotImplementedError


class LoudDuck(Duck):
    def quack(self):
        print("QUACK! QUACK")


class GentleDuck(Duck):
    def quack(self):
        print("quack!")


class WildDuck(Duck):

    def fly(self):
        print('fly')

    def details(self):
        print(self.name, "Wild")

    def quack(self):
        print("Scream")


class VillageDuck(Duck):

    def quack(self):
        print("Silent")

    def fly(self):
        print("Doesn't fly")


a = LoudDuck('Chacha')
a.quack()