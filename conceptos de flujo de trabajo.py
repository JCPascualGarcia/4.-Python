num1=int(input("Dame un número "))
num2=int(input("Dame otro número "))

if num1 > num2:
    print(num1, " Es mayor que ", num2)
elif num1 == num2:
    print(num1, " Es igual que ", num2)
else:
    print(num1, " Es menor que ", num2)

counter = 0

while counter <= 3:
    print("Una ronda")
    counter = counter + 1