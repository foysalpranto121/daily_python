# loop list
# list = ["rahim", "kodu", "kasem", "asim", "kamal"]
# for name in list:
#     print(name)
#  # for +akta variable(store ) +in + then use  previous variable where we use data
# # use range() function and len() function to create a suitable iterable
# for i in range(len(list)):
#     print(list[i])

#print  all items using while loop to go trough the index numbers

list = ["rahim", "kodu", "kasem", "asim", "kamal"]
y=0
while y < len(list):
    print(list[y])
    y=y+1





# list comphrehension
number=[1,2,3,4,5]
#condition expression
square=[numbers*2 for numbers in number]
plus=[number+4 for number in number]
print(plus)
print(square)
# normal way
x=[1,2,3,4,5]
for i in x:
    print(i*2)

#sort list
#assending order
num=[2,10,4,22,6,12]
num.sort()
print(num)
#decending order
num.sort( reverse=True)
print(num)
#COPY LIST
x=[1,2,3,4,5]
y=x.copy()
print(y)
print(x)
#join two list
list1=[1,2,3]
list2=[4,5,6]
list3=list1+list2
print(list3)

##more loop
rahim =0
while rahim < 10:
    print("yes u are rahim",rahim)
    rahim=rahim+1
friends=["rahim","kodu","kasem","asim","kamal"]
for friend in friends:
    if friend == "kodu":
       break
        #continue
    print(friend)