my_file = open("combinations.txt", 'r')
combinations = my_file.readlines()
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1

def Comparison(x, b):
    for i in x:
        if i in b:
            g = True
        else:
            return False
    return g
def CreateNewComb(el):
    allpossiblevars = []
    s = []
    for i in combinations:
        i = i.replace(',', '')
        i = Convert(i.replace('\n', ''))
        s.append(i)
    for i in s:
        if Comparison(set(i), el):
            allpossiblevars.append(i)
    return allpossiblevars
def SortingForZero(arr:list, comb:list, n: int):
    for x in arr:
        if x[n] == comb[n] or comb[n] == 0:
            x[n] = 0
    return list(filter(lambda x: x[n] == 0, arr))

def SortingForOne(arr:list, comb:list, n: int):
    arr = list(filter(lambda x: x[n] != comb[n] and comb[n] in x, arr))
    return arr

def SortingForTwo(arr:list, comb:list, n: int):
    arr = list(filter(lambda x: comb[n] not in x, arr))
    return arr
