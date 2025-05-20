#types of functions
#1. built in functions
#2. user defined functions
#3. lambda functions
#4 recursive functions

#user defined functions
#define def keyword

#syntax
# def functionName():
#     code
#     return
def myfunction( a,b):  # parameters
    sum =a+b
    print(sum)
    # sub=a-b
    #
    # print(sub)
myfunction(10,20) #pasing arguments and passing parameters value
myfunction(20,30)

def newFunction(x,y,z):
    multi=x*y*z
    print(multi)
newFunction(11,16,11)

## recursion : a function that calls itself, limit of recursion is 1000,
# def ReFun ():
#     print("hello")
#     ReFun()
#
# ReFun()
# zip function
list1 =[" pranto","fahim","kasem"]
list2=["developper","programmer pro","programmer"]

zipList=zip(list1,list2)
print(list(zipList))


#debugging
x=10
while x>1:
    print(x)
    x=x-1
## lambda functions : short hand function, anonymous function, function without name

add=lambda a,b:a+b
print(add(10,20))
minus =lambda  m,n:m-n
print(minus(10,20))

emni = lambda a,b,c,d: a+b/c-d
print(emni(10,20,30,40))
