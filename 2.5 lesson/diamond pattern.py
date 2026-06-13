rows = int(input("Enter the number of rows:"))
mid = rows // 2 + rows % 2
for i in range(1, mid + 1):
    print(" " * (mid - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()

for i in range(mid - 1, 0, -1):
    print(" " * (mid - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
