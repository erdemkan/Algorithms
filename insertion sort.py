unsorted_list = [4, 8, 19, 3, 2, 1 ,7, 5, 4, 48, 15, 0]

def insertion_sort(a):
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j], a[j - 1] = a[j - 1], a[j]
            j = j - 1
    print(a)

insertion_sort(unsorted_list)