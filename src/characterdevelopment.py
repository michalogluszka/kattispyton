import sys
# for tests
file = open("character-02.in") 
# for submission
#file = sys.stdin

data = file.read().splitlines()

number = int(data[0])

if(number==1):
    print(0)
elif(number==2):
    print(1)
else:
    total = 2**number - 1 - number
    print(total)


    
