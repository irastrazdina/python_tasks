import calendar
a = int(input("Enter year: "))
b = int(input("Enter month(in numbers): "))
c = calendar.TextCalendar(firstweekday=0)
print(calendar.prmonth(a, b,))
