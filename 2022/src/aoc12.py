import os
HERE=os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,"../input/input_12.txt"),"r") as f:
    input=[l.strip("\n") for l in f.readlines()]

m=len(input)
n=len(input[0])
s_index=[-1,-1]
e_index=[-1,-1]
new_input=[]
for index,line in enumerate(input):
    if(s_index[1]==-1):
        s_index[1]=line.find("S")
        if(s_index[1]!=-1):
            s_index[0]=index
    if(e_index[1]==-1):
        e_index[1]=line.find("E")
        if(e_index[1]!=-1):
            e_index[0]=index
    new_input.append(list(line))
queue=[]
queue.append((s_index[0],s_index[1],0))
vis={}
new_input[s_index[0]][s_index[1]]='a'
new_input[e_index[0]][e_index[1]]='z'
print(f"Starting {s_index} Ending {e_index}")
valid=lambda a,b,i,j:(a+i,b+j) if a+i>=0 and a+i<m and b+j>=0 and b+j<n and (a+i,b+j) not in vis and ord(new_input[a+i][b+j])- ord(new_input[a][b])<=1 else None
vis[(s_index[0],s_index[1])]=True
moves=[(-1,0),(1,0),(0,-1),(0,1)]

while(len(queue)>0):
    cur=queue.pop(0)
    d=cur[2]
    for move in moves:
        x=valid(cur[0],cur[1],move[0],move[1])
        if(x!=None):
            print(x)
            vis[x]=True
            queue.append((x[0],x[1],d+1))
            if(x[0]==e_index[0] and x[1]==e_index[1]):
                print(f"{d+1}")
                exit(0)
