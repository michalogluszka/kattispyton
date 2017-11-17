import sys
# for tests
file = open("sample.in") 
# for submission
# file = sys.stdin

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

data = file.read().splitlines()

for word in data:
    sort = sorted(word)
    nf = factorial(len(sort))

    distinct = list(set(sort))   

    bottom = 1   

    for l in distinct:
        x = sort.count(l)
        bottom = bottom*factorial(x)               
    result = nf//bottom
    print(int(result))


