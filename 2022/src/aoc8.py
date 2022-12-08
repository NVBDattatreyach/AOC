import os

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,"../input/input_8.txt"),"r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    rows,columns=len(input),len(input[0])
    visible_count=0
    location=set()
    max_top=[int(x) for x in input[0]]
    for i,line in enumerate(input[1:-1],1):
        max_left=int(line[0])
        for j,c in enumerate(line[1:-1],1):
            visible=False
            if(int(c)>max_top[j]):
                visible=True
                max_top[j]=int(c)
            if(int(c)>max_left):
                visible=True
                max_left=int(c)
            if(visible):
                location.add((i,j))
    max_bottom=[int(x) for x in reversed(input[-1])]
    for i,line in enumerate(reversed(input[1:-1]),1):
        max_right=int(line[-1])
        for j,c in enumerate(reversed(line[1:-1]),1):
            visible=False
            if(int(c)>max_bottom[j]):
                visible=True
                max_bottom[j]=int(c)
            if(int(c)>max_right):
                visible=True
                max_right=int(c)
            if(visible):
                location.add((rows-1-i,columns-1-j))
left_visible=0
right_visible=0
top_visible=0
bottom_visible=0
for i in range(rows):
    if(input[i][0]!='0'):
        left_visible+=1
    if(input[i][-1]!='0'):
        right_visible+=1
for i in range(1,columns-1):
    if(input[0][i]!='0'):
        top_visible+=1
    if(input[-1][i]!='0'):
        bottom_visible+=1
print(len(location)+left_visible+right_visible+top_visible+bottom_visible)
print(len(location)+2*rows+2*(columns-2)) 
