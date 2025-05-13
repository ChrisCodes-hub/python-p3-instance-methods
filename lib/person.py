#!/usr/bin/env python3

class Person:
    def __init__(self,name="Guido"):
        self.name = name
    
    def talk(self):
        print("Hello World!")

    def walk(self) :
        print("The person is walking.")   

guido=Person()       