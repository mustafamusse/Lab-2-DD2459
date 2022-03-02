def memberinArray(element, array):
    left = 0
    right = len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left <= right:
        if element < array[x]:
            right = x - 1
        else:
            left = x + 1
        x = (left + right) // 2

    return (array[x] == element)

print(memberinArray(6,[1,2,3,4,5]))
print(memberinArray(4,[1,2,3,4,5]))