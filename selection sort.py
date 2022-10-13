unsorted_array = [5, 4, 6, 8, 12, 1, 7]

def selection_sort(a):
    for i in range(len(a) - 1):
        smallest = i
        for j in range(i+1,len(a)):
            if a[j] < a[smallest]:
                smallest = j
        a[i], a[smallest] = a[smallest], a[i]
    print(a)

selection_sort(unsorted_array)

