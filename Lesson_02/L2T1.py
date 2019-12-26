try:
    a = float(input("Enter First Number: "))
    b = float(input("Enter Second Number: "))
except ValueError:
    print("Wrong input!")
try:
    print(int(a + b))
except NameError:
    print("Sorry")
try:
    print(a - b)
except NameError:
    print("Very sorry")
try:
    print(a + b)
except NameError:
    print("Told ya")
