# predicted 12/15

#1
def a():
    return 5
print(a())#predicted outcome:5 actual outcome:5

#2
def a():
    return 5
print(a()+a())#predicted outcome:10 actual outcome:10

#3
def a():
    return 5
    return 10
print(a())#predicted outcome:5 actual outcome:5

#4
def a():
    return 5
    print(10)
print(a())#predicted outcome:5 actual outcome:5

#5
def a():
    print(5)
x = a()
print(x)#predicted outcome:5,5 actual outcome:5,none

#6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))#predicted outcome:3,5,error actual outcome:3,5,error

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))#predicted outcome:2 5 actual outcome:25

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())#predicted outcome:100,10 actual outcome:100,10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))#predicted outcome:7 actual outcome:7
print(a(5,3))#predicted outcome:14 actual outcome:14
print(a(2,3) + a(5,3))#predicted outcome:21 actual outcome:21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))#predicted outcome:8 actual outcome:8

#11
b = 500
print(b)#predicted outcome:500 actual outcome:500
def a():
    b = 300
    print(b)
print(b)#predicted outcome:500 actual outcome:500
a()#predicted outcome:300 actual outcome:300
print(b)#predicted outcome:500 actual outcome:500

#12
b = 500
print(b)#predicted outcome:500 actual outcome:500
def a():
    b = 300
    print(b)
    return b
print(b)#predicted outcome:500 actual outcome:500
a()#predicted outcome:300 actual outcome:300
print(b)#predicted outcome:500 actual outcome:500

#13
b = 500
print(b)#predicted outcome:500 actual outcome:500
def a():
    b = 300
    print(b)
    return b
print(b)#predicted outcome:500 actual outcome:500
b=a()#predicted outcome:300 actual outcome:300
print(b)#predicted outcome:300 actual outcome:300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()#predicted outcome:1,3,2 actual outcome:1,3,2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()#predicted outcome:1,3,5 actual outcome:1,3,5
print(y)#predicted outcome:10 actual outcome:10