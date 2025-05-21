class Rahim :
    name=""
    number="" #properties


a= Rahim()
b= Rahim() #store in variable
c= Rahim()

a.name='kasem'# create object
b.name='fahim'
c.number='017'
print(a.name)
print(b.name)
print(c.number)

#inheritance
class Baba: #parrent class,base class
    car="bmw"
    tk="100 core"
    home="dhanmondi"
class Kaka (Baba): #child class,drive class
        BrokenHome="Asulia"
        BrokenCar="Rickshaw"
k=Kaka()
print(k.car)
print(k.home)
print(k.BrokenHome)
#Multiple inheritance

class Dad:
    car="bmw"
    tk="100 core"
    home="dhanmondi"
class Mom:
   school="dhanmondi"
   desh="RASS"

class Me:
    home="dhanmondi"
    country="bangladesh"
class Kaka (Dad,Mom,Me): #child class,drive class
        BrokenHome="Asulia"
        BrokenCar="Rickshaw"
k=Kaka()
print(k.car)
print(k.home)
print(k.desh)
print(k.BrokenHome)
### Multilevel inheritance
class Dad:
    car="bmw"
    tk="100 core"
    home="dhanmondi"
class Mom(Dad):
   school="dhanmondi"
   desh="RASS"
m=Mom()
print(m.car)

class Me(Mom):
    home="dhanmondi"
    country="bangladesh"
class Kaka (Me): #child class,drive class
        BrokenHome="Asulia"
        BrokenCar="Rickshaw"
k=Kaka()
print(k.car)
print(k.home)
print(k.desh)
print(k.BrokenHome)

## hybrid and hierarchical inheritance


