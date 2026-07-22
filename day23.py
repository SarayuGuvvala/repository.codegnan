def pattern(num):
    for j in range(1, num + 1):
        for i in range(1, j + 1):
            print("*", end=" ")
        print()

num = int(input("Enter a number: "))
pattern(num)
