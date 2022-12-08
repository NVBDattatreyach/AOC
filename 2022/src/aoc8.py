import os

bottom_to_original=lambda a,b,c:(c-b-1,a)    
original = lambda a,b,c:(a,b)
top_to_original=lambda a,b,c:(b,a)
right_to_original=lambda a,b,c:(a,c-1-b)

def score(s,a,f):
    global score_arr
    c=len(s)
    st=[0]
    for i,ch in enumerate(s[1:-1],1):
        while(len(st)>0):
            if(int(ch)>int(s[st[-1]])):
                st.pop()
            else:
                x,y=f(a,i,c)
                score_arr[x][y]*=i-st[-1]
                break
        if(len(st)==0):
            x,y=f(a,i,c)
            score_arr[x][y]*=i
        st.append(i)
    
def traverse(l,f):
    r=len(l)
    c=len(l[0])
    for a in range(r):
        s=""
        for b in range(c): 
            x,y=f(a,b,c)
            ch=l[x][y]
            s+=ch
        score(s,a,f)

HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(HERE,"../input/input_8.txt"),"r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    rows,cols=len(input),len(input[0])
    score_arr=[[1 if (1<=j<cols-1) else 0 for j in range(cols)] if (1<=i<rows-1)
        else [0 for j in range(cols)] for i in range(rows)
    ]
    traverse(input,bottom_to_original)
    traverse(input,right_to_original)
    traverse(input,top_to_original)
    traverse(input,original)
    ans=max([ max(x) for x in score_arr])
    print(ans)

