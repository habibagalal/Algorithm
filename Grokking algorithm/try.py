def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)
        guess = list[mid]
        if guess > item:
            high = mid - 1
        elif guess < item:
            low = mid + 1
        else:
            return guess
    return -1


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 3
result = binary_search(my_list, x)
if result != -1:
    print("the element index is ", str(result))
else:
    print("not found ")
