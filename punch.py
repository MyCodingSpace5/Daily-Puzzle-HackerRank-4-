# Enter your code here. Read input from STDIN. Print output to STDOUT

def allpossiblities(char, size):
    array = []
    combination = []
    combinations = []
    
    for charitem in char:
        for arrayitem in array:
            if(arrayitem == charitem):
                array.append(char)
            else:
                continue
while(len(combinations) < len(array) ^ size):
    for item in size:
        combination.append(array[random.randint(0, len(array))])
    for combinationitem in combinations:
        if(combination == combination):
            combination = []
            break
        else:
            continue
if(combination == None):
    continue
else:
    combinations.append(combination)
    continue
