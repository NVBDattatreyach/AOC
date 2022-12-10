import os
HERE=os.path.dirname(os.path.abspath(__file__))
def visualize(crt_pos,x):
    if(crt_pos==0):
        print("")
    if(x-1<=crt_pos<=x+1):
        print("#",end="")
    else:
        print("..",end="")

    return (crt_pos+1)%40
with open(os.path.join(HERE,"../input/input_10.txt"),"r") as f:
    input=[line.strip("\n") for line in f.readlines()]
    x=1
    cpu_cycle=1
    crt_pos=0
    for line in input:
        op=line.split(" ")[0]
        if(op=='noop'):
            # if(x-1<=crt_pos<=x+1):
            #     print("#",end="")
            # else:
            #     print(".",end="")
            # cpu_cycle+=1
            crt_pos=visualize(crt_pos,x)
            cpu_cycle+=1
        else:
            # if(x-1<=crt_pos<=x+1):
            #     print("#",end="")
            # else:
            #     print(".",end="")
            crt_pos=visualize(crt_pos,x)
            cpu_cycle+=1
            crt_pos=visualize(crt_pos,x)
            cpu_cycle+=1
            v=int(line.split(" ")[1])
            x+=v

              


        
