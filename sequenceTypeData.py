#sequence type data( list, tuple, range)
#list type
li=['apple','banana','cherry']
print(li)
print(type(li))
li[2]='orange'
print(li)
#mutable list can change
#tuple type
#not mutable tuple cannot change
tu=('apple','banana','cherry')
print(tu)
print(type(tu))
# tu[2]='orange'
# print(tu)
#range type data
x= range(6)
print(x)
for n in x: #looping range
    print(n)



