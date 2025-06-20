n = int(input("Enter size of array: "))
arr = []
for i in range(n):
    num = int(input("Enter the " + str(i + 1) + "th number: "))
    arr.append(num)

# now bubble sort it

for i in range(n - 1, -1, -1):
    for j in range(0, i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)
