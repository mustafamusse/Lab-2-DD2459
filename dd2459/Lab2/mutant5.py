
def insertionSort(array):
    #instead of maxSwap = len(array)
    maxSwap = len(array) - 1
    i = 1
    while i < maxSwap:
        j = i
        while (j > 0) and (array[j] < array[(j - 1)]):
            tmp = array[j]
            array[j] = array[j - 1]
            array[j - 1] = tmp
            j = j - 1 
        i = i + 1
    return array

def memberinArray(element, array):
    left = 0
    right = len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left <= right:
        
        if element < array[x]:
            right = x - 1
        else:
            left = x - 1
        x = (left + right) // 2

    return (array[x] == element)

def IIIMutant5(element, array):
    insertionSort(array)
    print(array)
    memberinArray(element, array)

print(IIIMutant5(3, [1, 2, 48, 293293, 909, 3333, 32, 10, 11, 29, 89898, 3, 20]))

def main():
    print("RandomTesting: ", IIIMutant5(437, [9400, 437, 1904, 7686, 8625, 1606, 6042]))
    
    A = [[943, 754, 104, 979, 13, 822], [265, 754, 104, 979, 13, 822], [943, 22, 104, 979, 13, 822], [943, 754, 943, 979, 13, 822], [943, 754, 104, 934, 13, 822], [943, 754, 104, 979, 886, 822], [943, 754, 104, 979, 13, 149], [265, 22, 104, 979, 13, 822], [265, 754, 943, 979, 13, 822], [265, 754, 104, 934, 13, 822], [265, 754, 104, 979, 886, 822], [265, 754, 104, 979, 13, 149], [943, 22, 943, 979, 13, 822], [943, 22, 104, 934, 13, 822], [943, 22, 104, 979, 886, 822], [943, 22, 104, 979, 13, 149], [943, 754, 943, 934, 13, 822], [943, 754, 943, 979, 886, 822], [943, 754, 943, 979, 13, 149], [943, 754, 104, 934, 886, 822], [943, 754, 104, 934, 13, 149], [943, 754, 104, 979, 886, 149]]
    count = 1
    for elem in A:
        res = IIIMutant5(elem[2], elem)
        if res == False:
            print("Pairwise testing counter: ", count)
            break
        count = count + 1
        
if __name__ == "__main__":
    main()
