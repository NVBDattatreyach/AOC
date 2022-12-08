count=0

def fully_contain(first_interval,second_interval):
    first_interval=first_interval.split("-")
    second_interval=second_interval.split("-")
    a=int(first_interval[0])
    b=int(first_interval[1])
    c=int(second_interval[0])
    d=int(second_interval[1])
    return (a<=c and b>=d) or (c<=a and d>=b)
def overlap_at_all(first_interval,second_interval):
    first_interval=first_interval.split("-")
    second_interval=second_interval.split("-")
    a=int(first_interval[0])
    b=int(first_interval[1])
    c=int(second_interval[0])
    d=int(second_interval[1])
    return (a<=c and c<=b) or ( a>c and a<=d) 
    

with open("input.txt","r") as f:
    for line in f.readlines():
        first_interval,second_interval=line[:-1].split(",")
        if(overlap_at_all(first_interval,second_interval)):
            count+=1
print(count)
     
