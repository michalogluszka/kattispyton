import sys
# for tests
file = open("A.0.in") 
# for submission
#file = sys.stdin

currentJack = 0
currentJill = 0
jacks = {}
canSell = 0
lastJack = 0

while(1):

    
    line = file.readline().rstrip('\n')
    
    if(line == '0 0'):
        break
    elif(len(line.split(' '))==2):    
        jack = int(line[0])
        jill = int(line[2])            
        currentJack = 0
        currentJill = 0
        jacks = {}
        canSell = 0
    else:         
        if(currentJack < jack):
            jacks[line] = 1    
            currentJack+=1
        elif(currentJill < jill):
            currentJill+=1
            
            for(x in range(0,len(jacks)))
                if(jacks[x] == line)                
                    canSell+=1
        if(currentJack == jack and currentJill == jill): 
            print(canSell)