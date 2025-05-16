#type casting
name ='12334'
print(int(name))
print(type(int(name)))
num =50
print(float(num))
print(str(num))
print(type(str(num)))
print(bool(num))
print(type(bool(num)))

# Lists
l1=[1,2,3,4]
print(type(l1))
print(l1[2])
l1[1]=100
print(l1)
l2=["apple","banana","cherry"]
print(l2)
l3=[True,False]
print(l3)
print(type(l3))
l4=[1,2.5,"apple",True]
print(l4)
#Acess list element
name=["changeName","updatename","webname"]
print(name[2])
#update list element
name[2]="python"
print(name)
#delete list element
del name[1]
print(name)
#add list element
#append
name.append("java")
print(name)
#insert list element
name.insert(1,"c++")
print(name)
#remove
name.remove("java")
print(name)

