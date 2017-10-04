import sys
# for tests
file = open("datum.1.in") 
# for submission
# file = sys.stdin

data = file.readline().strip('\n').split(' ')

print(data)

D = data[0]
M = data[1]

