unsorted_list = [4, 8, 19, 3, 2, 1 ,0]

def insertion_sort(a):
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
    print(a)

insertion_sort(unsorted_list)