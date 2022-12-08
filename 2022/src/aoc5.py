initial_arrangement=[
    "zjnwps",
    "gst",
    "vqrlh",
    "vstd",
    "qztdbmj",
    "mwtjdczl",
    "lpmwgtj",
    "ngmtbfqh",
    "rdgcpbqw"
]


def move(n,a,b):
    global initial_arrangment
    temp=initial_arrangement[a-1][-n:]
    initial_arrangement[a-1]=initial_arrangement[a-1][:-n]
    initial_arrangement[b-1]=initial_arrangement[b-1]+temp
    
with open("input.txt","r") as f:
    for line in f.readlines():
        line=line.strip("\n")
        _,n,_,a,_,b=line.split(" ")
        move(int(n),int(a),int(b))

for s in initial_arrangement:
    print(s[-1].upper(),end="")
