number = int(input("Choississez un nombre pour voir sa table de multiplication : "))

for i in range(11):
    result = number * i
    print(f"{number} x {i} = {result}")
