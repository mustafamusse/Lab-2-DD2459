
# Mutant 2
def insertionSortMutant2(array):
    maxSwap = len(array)
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

def memberinArrayMutant2(element, array):
    left = 0
    right = len(array) - 3 # len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left <= right:
        if element < array[x]:
            right = x - 1
        else:
            left = x + 1
        x = (left + right) // 2 

    return (array[x] == element)

def IIIMutant2(element, array):
    sorted = insertionSortMutant2(array)
    print(array)
    return memberinArrayMutant2(element, array)


def main():
    print("RandomTesting: ", IIIMutant2(437, [9400, 437, 1904, 7686, 8625, 1606, 6042]))
    
    A = [[943, 754, 104, 979, 13, 822], [265, 754, 104, 979, 13, 822], [943, 22, 104, 979, 13, 822], [943, 754, 943, 979, 13, 822], [943, 754, 104, 934, 13, 822], [943, 754, 104, 979, 886, 822], [943, 754, 104, 979, 13, 149], [265, 22, 104, 979, 13, 822], [265, 754, 943, 979, 13, 822], [265, 754, 104, 934, 13, 822], [265, 754, 104, 979, 886, 822], [265, 754, 104, 979, 13, 149], [943, 22, 943, 979, 13, 822], [943, 22, 104, 934, 13, 822], [943, 22, 104, 979, 886, 822], [943, 22, 104, 979, 13, 149], [943, 754, 943, 934, 13, 822], [943, 754, 943, 979, 886, 822], [943, 754, 943, 979, 13, 149], [943, 754, 104, 934, 886, 822], [943, 754, 104, 934, 13, 149], [943, 754, 104, 979, 886, 149]]
    count = 1
    for elem in A:
        res = IIIMutant2(elem[2], elem)
        if res == False:
            print("Pairwise testing counter: ", count)
            break
        count = count + 1
        
if __name__ == "__main__":
    main()