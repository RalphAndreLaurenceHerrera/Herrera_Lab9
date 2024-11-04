# Asks the number of rows from the user.
rowswant = int(input("Enter the number of rows you want to show: "))
# Starting number
num = 1
# Pattern Code
# Is rowscount ≤ rowswanted?
for rowscount in range(1, rowswant + 1):
    # Is columncount < rowscount?
    for columnscount in range(rowscount):
        print(num, end=" ")
        num += 1
    print()
