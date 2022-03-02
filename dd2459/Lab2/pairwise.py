from random import randint

def generatePairwise(numberOfElements=10, highest=1000,lowest=1):
    defaults = []
    typicals = []
    testCases = []

    # generate default elements for defaults list
    for x in range(numberOfElements):
        defaults.append(randint(lowest, highest))
    # generate typical for typicals list
    while len(typicals) < len(defaults):
        newTypical = randint(lowest, highest)
        if newTypical != defaults[len(typicals)]:
            typicals.append(newTypical)
    
    #0-wise testcase
    testCases.append(defaults)

    #print("0-wise: ", testCases)
    
    #1-wise testcases
    for element in range(numberOfElements):
        newTestCase= defaults[0:element] + typicals[element:element +1] + defaults[element + 1:]
        testCases.append(newTestCase)

    #print("1-wise: ", testCases)

    #2-wise testcases
    for element1 in range(numberOfElements):
        for element2 in range(element1 +1 , numberOfElements):
            newTestCase = defaults[0:element1] + typicals[element1:element1 +1] + defaults[element1 +1: element2] + typicals[element2:element2 + 1] + defaults[element2 + 1:]
            testCases.append(newTestCase)
    return testCases

tests= generatePairwise();
#print(tests)
#print(len(tests))