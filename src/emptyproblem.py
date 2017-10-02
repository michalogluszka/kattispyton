# pylint: disable=invalid-name
import sys

# for tests
file = open("A.0.in")
# for submission
# file = sys.stdin

#    Search for number in array
def binary_search(number, array, lo, hi):
 
    if hi < lo: return -1       # no more numbers
    mid = (lo + hi) // 2        # midpoint in array
    if number == array[mid]:
        return mid                  # number found here
    elif number < array[mid]:
        return binary_search(number, array, lo, mid - 1)     # try left of here
    else:
        return binary_search(number, array, mid + 1, hi)     # try above here
 
def my_search(int, array):     # convenience interface to binary_search()
    return binary_search(int, array, 0, len(array) - 1)

counter = 0

while 1:
    
    line = file.readline().replace('\n','').split(' ')
    
    canSell = 0
    
    N = int(line[0])        
    M = int(line[1])
    
    if(N==0 and M==0):
        break    

    jacks = []
    jills = []

    for i in range(0, N):
        line = int(file.readline()[0])
        jacks.append(line)
        counter += 1

    # for i in range(0, M):
    #     line = int(file.readline()[0])
    #     if my_search(line,jacks) >= 0:
    #         canSell+=1              

    print(canSell)

