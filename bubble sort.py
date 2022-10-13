unsorted_list = [4, 8, 19, 3, 2, 1 ,0, 5, 4, 48, 15, -5]

def bubble_sort(a):
    for i in range(1, len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
    print(a)

bubble_sort(unsorted_list)