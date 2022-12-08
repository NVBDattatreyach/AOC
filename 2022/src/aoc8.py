with open("input.txt","r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    rows,columns=len(input),len(input[0])
    visible_count=0
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
                visible_count+=1
                new_line=line[:j]+"0"+line[j+1:]
                line=new_line
                input[i]=line
    max_bottom=[int(x) for x in reversed(input[-1])]
    print(visible_count)
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
                visible_count+=1
print(visible_count+2*rows+2*(columns-2))
                 
