import copy 

def back(choices, index):
    if len(choices) == 6:
        print(' '.join(map(str, choices)))
    else:
        for i in range(index+1, len(lotto)):
            choices.append(lotto[i])
            back(choices, i)
            choices.pop()
    
while 1:
    inp = list(map(int, input().split(' ')))
    if inp == [0]:
        break
    k = inp[0]
    lotto = inp[1:]
    for i in range(k-6+1):
        li = back([lotto[i]], i)
    print()
