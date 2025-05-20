for x in range(10):
    if x==5:
        #break
        continue
    print(x)
else:
    print("else")
    name =["changeName","updatename","webname"]
    for m in range(len(name)):
        if m==2:
            break
        print(name[m])