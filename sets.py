# set ( data science and data analysis and machine learning most)
# use second bracket or carliet bracket
# can not use same data twice
# unordered
# unindexed
# unchangable
# duplicate not allowed
# set is mutable

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
print("apple" in set1)  # access data

print(len(set1))
print(set2)
# join set
print(set1.union(set2))
print(set1.intersection(set2))
# add data
set1.add("orange")
print(set1)
# remove data
set1.remove("apple")
print(set1)
set2.pop()  # remove one item but u dont know which one
print(set2)
# clear data
set1.clear()
print(set1)

## loop set
set1 = {"apple", "banana", "cherry"}
for x in set1:
    print(x)
#while loop set  only possible when we make it in list
#copy set
set1 = {"apple", "banana", "cherry"}
set2 = set1.copy()
print(set2)
# convert set to list
set1 = {"apple", "banana", "cherry"}
list1 = list(set1)
print(list1)