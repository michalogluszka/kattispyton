# pylint: disable=invalid-name
import sys

# for tests
# file = open("A.0.in")
# for submission
file = sys.stdin

data = file.read().splitlines()

counter = 0

while 1:
    line = data[counter].split(" ")

    canSell = 0
    
    N = int(line[0])    
    M = int(line[1])
    
    if(N==0 and M==0):
        break

    counter += 1

    jacks = []
    jills = []

    for i in range(counter, N + counter):
        jacks.append(int(data[i]))
        counter += 1

    for i in range(counter, M + counter):
        jills.append(int(data[i]))
        counter += 1

    i_n = 0
    i_m = 0

    while(i_n < N and i_m < M):
        if jacks[i_n] < jills[i_m]:
            i_n += 1
        elif jacks[i_n] > jills[i_m]:
            i_m += 1
        else:
            i_n += 1
            i_m += 1
            canSell += 1

    print(canSell)
