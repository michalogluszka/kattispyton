import sys
# for tests
file = open("sample.in") 
# for submission
#file = sys.stdin

testCases = int(file.readline().rstrip("\n"))


for i in range(0,testCases):
    emptyLine = file.readline().rstrip("\n")
    
    number = file.readline().rstrip("\n").split(' ')
    NG = number[0]    
    NM = number[1]
    
    SG = sorted(list(map(int,file.readline().rstrip("\n").split(' '))))
    SM = sorted(list(map(int,file.readline().rstrip("\n").split(' '))))

    print(SG)
    print(SM)

    # if(gozzilla == mecha):
    #     print("uncertain")
    # elif(gozzilla < mecha):
    #     print("MechaGodzilla")
    # else:
    #     print("Godzilla")