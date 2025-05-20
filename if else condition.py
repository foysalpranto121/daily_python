#if else condition
# a==b a is equal to b
# a!=b a is not equal to b
# a<b a is less than b
# a>b a is greater than b
# a<=b a is less than or equal to b
# a>=b a is greater than or equal to b
a=10
b=20
if (a==b):
    print("now print")

    
elif (a>b):
        print("a is greater than b")
elif (a<b):
        print("a is less than b")
else:
        print("b is greater than a")
### nested if else
age = 25
has_license = True

if age >= 18:
    print("Age check passed.")
    if has_license:
        print("License check passed.")
        print("Eligible to drive.")
    else:
        print("License check failed.")
        print("Not eligible to drive.")
else:
    print("Age check failed.")
    print("Not eligible to drive.")

