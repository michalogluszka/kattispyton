import sys
# for tests
# file = open("02_simple.in") 
# for submission
file = sys.stdin

data = file.read().splitlines()

numberOfRows = int(data[0])

for i in range(numberOfRows+1):
    if(data[i].startswith("Simon says ")):
        print(data[i][len("Simon says "):len(data[i])])
