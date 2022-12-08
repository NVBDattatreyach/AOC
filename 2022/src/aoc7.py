class Node:
    def __init__(self,name,parent,type,size):
        self.name=name
        self.parent=parent
        self.type=type
        self.size=size
        self.children={}
        # name : obj

solution=0
current_unused=0
sizes=[]
ans=70000000
def dfs(node):
    global solution
    global sizes
    for child in node.children:
#        print("{} : {}".format(child,node.children[child].type))
        if(node.children[child].type=='f'):
            node.size+=node.children[child].size
        else:
            dfs(node.children[child])
            node.size+=node.children[child].size
            sizes.append(node.size)
    if(node.size<=1_00_000):
        solution+=node.size

with open("input.txt","r") as f:
    root=Node('/',None,'d',0)
    root.parent=root
    line=f.readline().strip("\n")
    cur_node=root
    while(line!=''):
        cmd=line.split(" ")[1]
        if(cmd=="cd"):
            tgt=line.split(" ")[2]
            if(tgt==".."):
                cur_node=cur_node.parent
            elif(tgt=='/'):
                cur_node=root
            else:
                if(tgt not in cur_node.children):
                    new_node=Node(tgt,cur_node,'d',0)
                    cur_node.children[tgt]=new_node
                    cur_node=new_node
                else:
                    cur_node=cur_node.children[tgt]
            line=f.readline().strip("\n")
        else:
            line=f.readline().strip("\n")
            while(line!=''):
                if(line[0]=='$'):
                    break
                else:
                    first,second=line.split(" ")
                    if(first!='dir'):
                        new_node=Node(second,cur_node,'f',int(first))
                        cur_node.children[second]=new_node
                line=f.readline().strip("\n")
dfs(root)
print(root.size)
current_unused=70000000-root.size
for x in sorted(sizes):
    if(x>=30000000-current_unused):
        print(x)
        break
