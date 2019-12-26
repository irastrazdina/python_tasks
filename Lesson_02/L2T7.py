str_1 = input("Enter First Word: ")
str_2 = input("Enter Second Word: ")
 
stringlength = len(str_1)
slicedString = str_1[stringlength ::-1]
print(str.lower(slicedString))
 
stringlength = len(str_2)
slicedString = str_2[stringlength ::-1]
print(str.lower(slicedString))
