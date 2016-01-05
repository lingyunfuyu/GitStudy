#!/usr/bin/python
# Filename: method.py

class Person:
    def sayHi(self):
        print 'Hi, how are you?'

p = Person()
p.sayHi()

Person().sayHi()
