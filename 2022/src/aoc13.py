import json
import os
import functools

def parse(s):
    return json.loads(s)
    

HERE=os.path.dirname(__file__)
index=0
ans=0
res=[]
def compare(l,r):
    if(type(l)==int and type(r)==int):
        if(l<r):
            return -1
        elif(l==r):
            return 0
        else:
            return 1
    elif(type(l)==list and type(r)==list):
        for i,j in zip(l,r):
            x=compare(i,j)
            if(x==-1 or x==1):
                return x
        if(len(l)<len(r)):
            return -1
        elif(len(l)==len(r)):
            return 0
        else:
            return 1
    else:
        if(type(l)==int):
            return compare([l],r)
        else:
            return compare(l,[r])
input=[]
with open(os.path.join(HERE,"../input/input_13.txt"),"r") as f:
    while True:
        left=f.readline().strip("\n")
        right=f.readline().strip("\n")
        l=parse(left)
        r=parse(right)
        input.append(l)
        input.append(r)
        x=f.readline()
        if(x==''):
            break
input.append([[2]])
input.append([[6]])
sorted_input=sorted(input,key=functools.cmp_to_key(compare))
ans=1
for i,x in enumerate(sorted_input):
    if(x==[[2]] or x==[[6]]):
        ans*=(i+1)
print(ans)

"""
st : [ 1 , [ 2 , 3 
"""
    
