import os
HERE=os.path.dirname(os.path.abspath(__file__))
a=-20
ss_sum=0
with open(os.path.join(HERE,"../input/input_10.txt"),"r") as f:
    cycle=1
    x=1
    while(a<=220):
        input=f.readline().strip("\n")
        if(input!=""):
            op=input.split(" ")[0]
            if(op=='noop'):
                if(cycle==a+40):
                    ss_sum+=cycle*x
                    a=a+40
                cycle+=1
            else:
                if(cycle<=a+40<cycle+2):
                   ss_sum+=(a+40)*x 
                   a+=40
                cycle+=2
                x+=int(input.split(" ")[1])
        else:
            break
                
print(ss_sum)

         

