L = [4,5,1,2,9,7,10,8]

print("Original List: ", L)

count = 0

for i in L:
    count += i

avg = count / len(L)
print("Sum of the list: ", count)
print("Average of the list: ", avg)

L.sort()

print("Smallest number in the list: ", L[0])
print("Largest number in the list: ", L[-1])