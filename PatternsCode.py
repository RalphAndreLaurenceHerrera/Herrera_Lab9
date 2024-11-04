# Asks the number of rows from the user.
rows = int(input("Enter the number of rows: "))
# Starting number
num = 1
# Pattern Code
for i in range(1, rows + 1):
    for x in range(i):
        print(num, end=" ")
        num += 1
    print()