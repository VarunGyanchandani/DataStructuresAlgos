def linear_search(l1, n, key):
    for i in range(0, n):
        if (l1[i] == key):
            return i
    return -1


l1 = [1, 10, 20, 3, 5, 4, 2, 7, 13, 9]
key = 7

n = len(l1)
res = linear_search(l1, n, key)
if (res == -1):
    print("Element not found")
else:
    print("Element found at index: ", res)