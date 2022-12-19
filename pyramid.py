n = int(input("Enter the row size:"))
print("\n")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        mul = i * j
        print(i * j, end=" ")
    print()
