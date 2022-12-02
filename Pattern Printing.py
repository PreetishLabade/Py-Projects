a = input("Please enter a number")
b = int(input("Please enter 1 for incrementing pattern and 0 for decrementing pattern"))
c = bool(b)
i = 1

if type(a) == int:
    while i !=a+1 and b == True:
        print(i * "*")
        i = i + 1

    while a !=i and b == False:
        print(a * "*")
        a = a - 1
else:
    print("Please enter valid input")

