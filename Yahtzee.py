#this code recommends strategy for a simplified variant of the popular game yahtzee
import numpy as np
def areSame(a):
    return all(x==a[0] for x in a)
def score(a):
    if areSame(a):
        return 25
    else:
        s = 0
        for i in range(0,3):
            s += a[i]
        return s
def EV(array, dice):
    TotalSum = 0
    n = 0
    temparray = array[:]
    if len(dice) == 1:
        for i in range(1,7):
            temparray[dice[0]] = i
            TotalSum += score(temparray)
            n += 1
    if len(dice) == 2:
        for i in range(1,7):
            for j in range(1,7):
                temparray[dice[0]] = i
                temparray[dice[1]] = j
                TotalSum += score(temparray)
                n += 1
    return TotalSum/n
def choosedice(arr):
    current = score(arr)
    a = EV(arr, [0])
    b = EV(arr, [1])
    c = EV(arr, [2])
    d = EV(arr, [0,1])
    e = EV(arr, [0,2])
    f = EV(arr, [1,2])
    rollall = 785/72
    ind = np.argmax([current, a,b,c,d,e,f, rollall])
    return(ind)

roll = []
for i in range(3):
    print('Enter dice', i+1); roll.append(int(input()))
print('Your score is currently:','\n' ,score(roll))
recommend =['Do not re-roll', 'Re-roll the first dice','Re-roll the the second dice', 'Re-roll the third dice',
            'Re-roll the first and second dice', 'Re-roll the first and third dice', 'Re-roll the second and third dice',
            'Re-roll all dice']
print(recommend[int(choosedice(roll))])
