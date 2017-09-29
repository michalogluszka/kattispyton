import sys
# for tests
file = open("A.0.in") 
# for submission
#file = sys.stdin

currentJack = 0
currentJill = 0
jacks = []
canSell = 0
nextJack = 0

while(1):

    
    line = file.readline().rstrip('\n')
    
    if(line == '0 0'):
        break
    elif(len(line.split(' '))==2):    
        jack = int(line[0])
        jill = int(line[2])            
        currentJack = 0
        currentJill = 0
        jacks = []
        canSell = 0
        nextJack = 0
    else:         
        if(currentJack < jack):
            jacks.append(line)    
            currentJack+=1
        elif(currentJill < jill):
            currentJill+=1            
            
            ticker = nextJack
            for x in range(ticker,len(jacks)):                                
                if int(line) == int(jacks[x]):           
                    canSell+=1                
                    nextJack=x+1
                    break                
                elif int(line) > int(jacks[x]):
                    nextJack = x+1  
                    break;                 
                else:                    
                    break;                

        if(currentJack == jack and currentJill == jill): 
            print(canSell)