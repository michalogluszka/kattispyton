import sys
# for tests
file = open("character-01.in") 
# for submission
file = sys.stdin

data = file.read().splitlines()

numberOfRows = int(data[0])

for i in range(1,numberOfRows+1):
    line = data[i].split(' ')