import sys
# for tests
file = open("test0.in") 
# for submission
#file = sys.stdin

data = file.read().splitlines()

for line in data:    
    x = int(line.split(' ')[0])
    y = int(line.split(' ')[1])
    if(x==0 and y==0):
        break
    
    if x+y==13:
        print("Never speak again.")
    elif x>y:
        print("To the convention.")
    elif x<y:
        print("Left beehind.")
    elif x==y:
        print("Undecided.")