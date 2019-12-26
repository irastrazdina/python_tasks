a = int(input("Enter Number: "))
 
if a % 2 == 0:
    print("Odd")
elif a % 2 == 0 and a in range(2, 27):
    print("In first range")
elif a % 2 != 0 and a in range(29, 53):
    print("In second range")
else:
    print("It's something")
