# Selection Sort

def selection_sort(a):
    for i in range(len(a)-1):
        minimum = i
        for j in range(i + 1, len(a)):
            if a[j] < a[minimum]:
                minimum = j
        a[i], a[minimum] = a[minimum], a[i]
    print(a)

selection_sort([4,5,6,17,0])

def insertion_sort(n):
    for i in range(1, len(n)):
        key = n[i]
        j = i - 1
        while j >= 0 and key < n[j]:
            n[j+1] = n[j]
            j -= 1
            n[j + 1] = key
    print(n)

selection_sort([5, 6, 0, 7, 8, 9])

# use this to showcase the timeit function
long_list = [
    23, 89, 1, 56, 45, 102, 77, 33, 91, 3, 67, 88, 14, 205, 39, 18, 60, 73, 81, 50,
    99, 34, 12, 6, 150, 121, 44, 10, 97, 22, 8, 200, 105, 31, 66, 49, 71, 109, 90, 17,
    27, 112, 84, 30, 95, 79, 13, 123, 58, 9, 21, 142, 7, 165, 120, 64, 80, 145, 47, 5,
    41, 134, 36, 2, 140, 98, 19, 87, 48, 116, 59, 11, 152, 26, 108, 16, 53, 32, 143, 20,
    24, 70, 157, 86, 155, 119, 128, 107, 25, 93, 117, 148, 104, 40, 103, 82, 115, 122,
    29, 172, 135, 100, 85, 54, 61, 62, 76, 118, 15, 38, 106, 46, 170, 139, 63, 28, 151,
    68, 74, 141, 55, 96, 137, 92, 78, 101, 133, 35, 176, 94, 75, 43, 132, 37, 126, 147
]
