# in list we use square bracket
# in tuple we use round bracket/parenthesis bracket
# tuple is immutable( can not change)
# tuple is faster than list
# tuple is more secure than list
# tuple is more memory efficient than list

tuple1 = ("apple", "banana", "cherry")
print(tuple1)
tuple2 = ("apple",1,2,False)
print(tuple2)
print(type(tuple2))
print(len(tuple2))
print(tuple2[2])
print(tuple2[-1])# negative index
print(tuple2[0:2])  # ( index 0 thake 2  print kore )
#update tuple

name=( "changeName","updatename","webname")
newname=list(name)
newname.append("python")
name=tuple(newname)
print(name)

#tuple unpacking

fruits = ("apple", "banana", "cherry", "strawberry", "kiwi")
#(green, yellow, red  )  = fruits
(*a,)=fruits
print(a)
# print(green)
# print(yellow)
# print(red)
####Loop through a tuple

for x in fruits:

    print(x)

    for x in range(len(fruits)):
        print(fruits[x])
        #print(fruits[x[0]])



#using while loop
user=("rahim","kodu","khan")
x=0
while x<len(user):
    print(user[x])
    x=x+1

    #join tuple

    tuple1 = ("apple", "banana", "cherry")
    tuple2 = (1, 5, 7, 9, 3)
    tuple3 = tuple1 + tuple2
    print(tuple3)
## Method
#count

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
x = tuple1.count("apple")
print(x)
#index

tuple1 = ("apple", "banana", "cherry", "apple", "cherry")
x = tuple1.index("apple")
print(x)