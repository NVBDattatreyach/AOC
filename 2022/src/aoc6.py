def test(line,left,right,count_dict):
    for c in line[left:right]:
        if(count_dict[c]>1):
            return False
    return True
def solve(line):
    count=dict.fromkeys("abcdefghijklmnopqrstuvwxyz",0)
    for i,c in enumerate(line):
        if(i<14):
            count[c]+=1
        else:
            if(test(line,i-14,i,count)):
                return i
            else:
                count[line[i-14]]-=1
                count[c]+=1
    return -1
with open("input.txt","r") as f:
    for line in f.readlines():
        print(solve(line.strip("\n")))
