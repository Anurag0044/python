num = input("enter a number ")

total = 0
reverse = ""

for digit in num:
    total = total + int(digit)
    reverse = digit + reverse
print("sum of digit =",total)
print("Reversed number =",reverse)
