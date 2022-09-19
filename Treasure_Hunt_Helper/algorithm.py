my_file = open("combinations.txt", 'r')
combinations = my_file.readlines()

allpossiblevars = []
s = []
import random

def SortingForZero(arr:list, n: int):
    arr = list(filter(lambda x: x[n] == combination[n], arr))
    return arr

def SortingForOne(arr:list, n:int):
    arr = list(filter(lambda x: x[n] != combination[n], arr))
    return arr

def SortingForTwo(arr:list, n:int):
    arr = list(filter(lambda x: combination[n] not in x, arr))
    return arr

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
print('Vvedite kolichestvo res: ')
number = int(input())
match number:
    case 2:
        elements = ['A', 'B']
        combination = ['A', 'B', 'A', 'B', 'A']
        combination_x = ['A', 'A', 'A', 'A', 'A']
    case 3:
        elements = ['A', 'B', 'C']
        combination = ['A', 'B', 'C', 'A', 'B']
        combination_x = ['A', 'B', 'A', 'B', 'A']
    case 4:
        elements = ['A', 'B', 'C', 'D']
        combination = ['A', 'B', 'C', 'D', 'A']
        combination_x = ['A', 'B', 'C', 'A', 'B']
    case 5:
        elements = ['A', 'B', 'C', 'D', 'E']
        combination = ['A', 'B', 'C', 'D', 'E']
        combination_x = ['A', 'B', 'C', 'D', 'A']
    case 6:
        elements = ['A', 'B', 'C', 'D', 'E', 'F']
        combination = ['A', 'B', 'C', 'D', 'E']
    case 7:
        elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        combination = ['A', 'B', 'C', 'D', 'E']
    case 8:
        elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        combination = ['A', 'B', 'C', 'D', 'E']
    case 9:
        elements = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        combination = ['A', 'B', 'C', 'D', 'E']

for i in combinations:
    i = i.replace(',', '')
    i = Convert(i.replace('\n', ''))
    s.append(i)

for i in s:
    if Comparison(set(i), elements):
        allpossiblevars.append(i)

cout = 0
while True:
    if cout == 2:
        print(combination)
        break
    print(combination)
    print('0 - In the row and in the correct spot, 1 - In the row but in the wrong spot, 2 - Not in the row in any spot ')
    response = list(input())
    for i in range(len(response)):
        if response[i] == '0':
            allpossiblevars = SortingForZero(allpossiblevars, i)
        if response[i] == '1':
            allpossiblevars = SortingForOne(allpossiblevars, i)
        if response[i] == '2':
            allpossiblevars = SortingForTwo(allpossiblevars, i)
    combination = random.choice(allpossiblevars)
    cout += 1