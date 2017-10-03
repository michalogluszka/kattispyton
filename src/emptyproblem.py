import sys
# for tests
file = open("sample.in") 
# for submission
#file = sys.stdin

testCases = int(file.readline().rstrip("\n"))


for i in range(0,testCases):
    emptyLine = file.readline().rstrip("\n")
    
    number = file.readline().rstrip("\n").split(' ')
    NG = int(number[0])
    NM = int(number[1])
    
    SG = sorted(list(map(int,file.readline().rstrip("\n").split(' '))))
    SM = sorted(list(map(int,file.readline().rstrip("\n").split(' '))))

    sg = 0
    sm = 0

    sgEliminated = 0
    smEliminated = 0

    while sg < NG and sm < NM:
        if SG[sg] == SM[sm]:
            smEliminated+=1
            sm+=1
        elif SG[sg]>SM[sm]:
            smEliminated+=1
            sm+=1
        elif SG[sg]<SM[sm]:
            sgEliminated+=1
            sg+=1    

    sgLeft = NG - sgEliminated
    ngLeft = NM - smEliminated

    if sgLeft == ngLeft:
         print("uncertain")
    elif sgLeft < ngLeft:
         print("MechaGodzilla")
    else:
         print("Godzilla")