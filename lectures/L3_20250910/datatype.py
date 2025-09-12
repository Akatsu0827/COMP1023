# var_complex = 1 + 2.5j
# print(type(var_complex))  # <class 'complex'>

# print(var_complex * var_complex)  # (-5.25+5j)

# var_1 , var_2 = (1021, 1023)

# var_3 = 1021, 1023

# print(var_3)

# var1 = 10

# address = id(var1)

# print(address)

# var1 = 20

# print(id(var1))

# import ctypes

# print(ctypes.cast(address, ctypes.py_object).value)

# var2 = [1, 1, 4, 5, 1, 4]

# print(id(var2))

# var2[2] = 1919810

# print(id(var2))

var3 = 10

# print(id(var3))
# print(id(float(var3)))

# var3 = float(var3)

print(id(var3))

var4 = var3

print(id(var4))

var4 += 10

print(var3)
print(id(var4))