list_of_numbers = [1, 2, 3, 4, 5]
# range byte 0 to 255
byte = bytes(list_of_numbers)
# inmutable byte can not change
print(byte)
print(type(byte))
# Bytearray
list_of_numbers = [1, 2, 3, 4, 5]
b1 = bytearray(list_of_numbers)
print(b1)
print(type(b1))
b1[0] = 10
# mutable bytearray can change
print(b1)
print(b1[0])

# Non type data
x = None
print(x)
print(type(x))
