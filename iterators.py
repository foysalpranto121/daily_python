list=[1,2,3,4,"Rahim","Karim"]
for i in list:
    print(i)
    x=iter(list)
    print(x.__next__())
    print(x.__next__())
    print(next(x))

## scope
#local scope
#global scope
def fun():
    x=10 #local scope
    print(x)



fun()# can not acess from outside function

x=20 #global scope
def fun1():
    global x
    print(x)

fun1()
print(x) #acess outsude from function


