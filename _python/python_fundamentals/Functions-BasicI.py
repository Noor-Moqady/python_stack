# #1 will print 5
def a():
    return 5
print(a())

# #2 will print 10
def a():
    return 5
print(a()+a())

# #3 will print 5
def a():
    return 5
    return 10
print(a())

# #4 will print 5
def a():
    return 5
    print(10)
print(a())

#5 will print 5, none because print in the function is not return value print cause none !!!
def a():
    print(5)
x = a()
print(x)


# #6 will print 3,5,none
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))


#7 will print 25
def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#8 will print 100,10
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#9 will print 7,14,21
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))


#10 will print 8
def a(b,c):
    return b+c
    return 10
print(a(3,5))


#11 will print 500,500,300,500
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#12 will print 500,500,300,500
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)


#13 will print 500,500,300,300
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)


#14 will print 1,3,2
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()


#15 will print 1,3,5,10
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)





