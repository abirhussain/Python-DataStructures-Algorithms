##################  Integer ########################
num_1 = 24
num_2 = num_1  # both variable pointing same memory address

print("Before num_2 value is updated:")
print("num_1 =", num_1)
print("num_2 =", num_2)

print("\nnum_1 points to:", id(num_1))
print("num_2 points to:", id(num_2))

num_2 = 50  # num_2 will point another memory address

print("\nAfter num_2 value is updated:")
print("num_1 =", num_1)
print("num_2 =", num_2)

print("\nnum_1 points to:", id(num_1))
print("num_2 points to:", id(num_2))


################## Dictionary  ###################


dict_1 = {"value": 24}

dict_2 = dict_1

print("\n\nBefore value is updated:")
print("dict_1 =", dict_1)
print("dict_2 =", dict_2)

print("\ndict_1 points to:", id(dict_1))
print("dict_2 points to:", id(dict_2))

dict_2["value"] = 50

print("\nAfter value is updated:")
print("dict_1 =", dict_1)
print("dict_2 =", dict_2)

print("\ndict_1 points to:", id(dict_1))
print("dict_2 points to:", id(dict_2))
