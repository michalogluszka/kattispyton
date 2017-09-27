import sys
# for tests
#file = open("1.in") 
file = sys.stdin

data = file.read().splitlines()
# for submission

numberOfRows = int(data[0])

for i in range(1,numberOfRows+1):
    line = data[i].split(' ')
    net = int(line[1]) - int(line[2])
    r = int(line[0])
    if(net < r):
        print("do not advertise")
    elif(net > r):
        print("advertise")
    else:
        print("does not matter")