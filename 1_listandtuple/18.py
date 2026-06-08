def selection_sort(lst):

    n = len(lst)
    for i in range(n):
        count = i
        for j in range(i+1, n):
            if lst[j] < lst[count]:
                count = j
        lst[i],lst[count] = lst[count],lst[i]



test_1 = [64, 25, 12, 22, 11]
test_2 = []
test_3 = [5]
test_4 = [3, 3, 3, 1, 1]

selection_sort(test_1)
selection_sort(test_2)
selection_sort(test_3)
selection_sort(test_4)

print(test_1)
print(test_2)
print(test_3)
print(test_4)