#file read
readText=open("text.text","r")
print(readText.read())
#file write
# writeText=open("pranto.text","w")
# writeText.write("Bye world")
writeText=open("hello.html ","a")
writeText.write("<h1>Bye world</h1>")
writeText.write("<p>Bye world \n</p>")

#file delete
import os
os.remove("pranto.text")
os.rmdir("")