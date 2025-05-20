#can store key and value
#key must be unique
#ordered
#changeable
#key value pair
#NOT allow duplicate key
#carliet bracket
studentInfo={ "Data":

    { "name":"Rahim",
    "age":20,
    "city":"Dhaka",
      "Roll":100
    },
              "year ": 2022

}

print(studentInfo)
print(studentInfo["Data"]["name"])
#dictionaries access by key

print(studentInfo["year "])
# x= studentInfo.values()

x=studentInfo.keys()

print(x)
y=studentInfo.values()

print(y)
##change items

studentInfo["Data"]["Roll"] = 101  ## [ call dictionary] and [key]
print(studentInfo["Data"]["Roll"])

studentInfo["Data"]["Roll"] = 102
print(studentInfo["Data"]["Roll"])

#update value
# studentInfo.update({"Data":"rahim is a good boy"})
# print(studentInfo["Data"])
# studentInfo.pop("Data")
# print(studentInfo)
# studentInfo.clear()
# print(studentInfo)
studentInfo.popitem() # remove last item
print(studentInfo)
#loop

for i in studentInfo:
    print(i)
    print(studentInfo[i])
    for x in studentInfo.values():
        print(x)
for x in studentInfo.items():
    print(x)
    for x in studentInfo.keys():
        print(x)

        ### copy dictionary

x=studentInfo.copy()
print(x)