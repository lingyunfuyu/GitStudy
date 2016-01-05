#/usr/bin/python
# Filename: using_dict.py

# 'ab' is short for 'a'drress'b'ook

ab = {
'Swaroop'	:'swaroopch@byteofpython.info',
'test'		:'test@foxmail.com',
'Larry'		:'larry@wall.org',
'Spammer'	:'spammer@hotmail.com'
}

print "Swaroop's address is %s" % ab['Swaroop']

# Adding a key/value pair
ab['Guido'] = 'guido@python.org'

# Deleting a key/value pair
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)
for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)
    
if 'Guido' in ab: 
#if ab.haskey('Guido'):
    print "\nGuido's address is %s" % ab['Guido']
