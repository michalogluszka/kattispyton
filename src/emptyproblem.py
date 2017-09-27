import sys
# for tests
#file = open("new.in") 
# for submission
file = sys.stdin

data = file.read().splitlines()

dic = {'a':'@'
      ,'b':'8'
      ,'c':'('
      ,'d':'|)'
      ,'e':'3'
      ,'f':'#'
      ,'g':'6'
      ,'h':'[-]'
      ,'i':'|'
      ,'j':'_|'
      ,'k':'|<'
      ,'l':'1'
      ,'m':'[]\/[]'
      ,'n':'[]\[]'
      ,'o':'0'
      ,'p':'|D'
      ,'q':'(,)'
      ,'r':'|Z'
      ,'s':'$'
      ,'t':'\'][\''
      ,'u':'|_|'
      ,'v':'\/'
      ,'w':'\/\/'
      ,'x':'}{'
      ,'y':'`/'
      ,'z':'2'}

result = ''
for x in data[0]:    
    if x.lower() in dic:
        result+=dic[x.lower()]
    else:
        result+=x

print(result)
      
    