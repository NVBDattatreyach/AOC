sum=0

def priority(c):
    if(c.islower()):
        return ord(c)-ord('a')+1
    else:
        return ord(c)-ord('A')+27
myDict=dict.fromkeys("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",0)
with open("input.txt","r") as f:
    for line in f.readlines():
        unq=set(sorted(line.strip("\n")))
        for c in unq:
            myDict[c]+=1
            if(myDict[c]==3):
                sum+=priority(c)
                myDict=dict.fromkeys(myDict,0) 
                break

print(sum)
