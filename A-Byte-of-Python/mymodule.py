def func(x):
    print x, '**', x, "=", x**x

version = 'v0.9'

if __name__ == '__main__':
    print '__name__:', __name__
    print 'This program is being run by itself'
    func(2)
    print version
else:
    print '__name__:', __name__
    print 'I am being imported from another module'
