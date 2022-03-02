from randomNumber import randomTestdata
from pairwise import generatePairwise

def insertionSortmutant1(array):
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


def memberinArraymutant1(element, array):
    left = 0
    right = len(array) - 1

    x = (left + right) // 2
    while array[x] != element and left <= right: # > is not <= 
        if element < array[x]:
            right = x - 1
        else:
            left = x + 1
        x = (left + right) // 2

    return (array[x] == element)

def IIImutant1(element, array):
    sorted = insertionSortmutant1(array)
    #print(sorted)
    return memberinArraymutant1(element, sorted)


def main():
   
    for i in range (100):
       A = randomTestdata()
       res = IIImutant1(A[2], A)
       if res == True:
           print("Number of attempts for random: ", i)
           break
    
    
    print("now")
    count = 1
    for i in range (100):
        A = generatePairwise()
        
        for elem in A:
            print(elem)
            res = IIImutant1(A[2], elem)
            if res == True:
                print("Pairwise testing counter: ", count)
                exit()
            
        count = count + 1
    
        
if __name__ == "__main__":
    main()
