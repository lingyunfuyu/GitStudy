#!/usr/bin/python
# Filename: str_method.py

name = 'Swaroop' # This is a string object

if name.startswith('Swa'):
    print 'Yes, the string starts with "Swa"'

if 'oo' in name:
    print 'Yes, it contains the string "oo"'

if name.find('war') != -1:
    print 'Yes, it contains the string "war"'

ss = '-+-'
mylist = ['Beijing', 'Tianjin', 'Hangzhou', 'Guangzhou']
print ss.join(mylist)
