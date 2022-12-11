import os


HERE=os.path.dirname(os.path.abspath(__file__))

        
        

class Monkey:
    all_monkeys=[]
    def __init__(self,items,op,x,a,b,id):
        self.cur_items=items
        self.op_str=op
        self.x=x
        self.a=a
        self.b=b
        self.inspect_count=0
        self.id=id
    def inspect(self):
        for old in self.cur_items:
            new=eval(self.op_str)%self.x
            if(new==0):
                self.all_monkeys[self.a].cur_items.append(new)
            else:
                self.all_monkeys[self.b].cur_items.append(eval(self.op_str))
        self.inspect_count+=len(self.cur_items)
        self.cur_items.clear()


    def __str__(self):
        return f"{self.cur_items}"
    def write_to_file(self):
        with open("new_input_11.txt","a") as g:
            g.write("Monkey{id}\n")
            g.write("  Starting items: {self.cur_items}\n")
            g.write("  Operation: new = {self.op_str}\n")
            g.write("  Test: divisible by")
            
def custom_strip(s:str,c):
    return s[s.find(c)+1:]


def parse(input):
    for i in range(0,len(input),7):
        items_str=custom_strip(input[i+1],':').replace(" ","")
        items=[int(x) for x in items_str.split(",")]
        op_str=custom_strip(input[i+2],'=').strip(" ")
        x=int(input[i+3].split(" ")[-1])
        a=int(input[i+4].split(" ")[-1])
        b=int(input[i+5].split(" ")[-1])
        yield Monkey(items,op_str,x,a,b,i//7)

with open(os.path.join(HERE,"../input/input_11.txt"),"r") as f:
    input=[line.strip("\n") for line  in f.readlines()]
for m in parse(input):
    Monkey.all_monkeys.append(m)
for i in range(20):
    for m in Monkey.all_monkeys:
        m.inspect()
    print(f"completed round {i+1}")
    # print(f"After round {i+1}")
    # for j,m in enumerate(Monkey.all_monkeys):
        #     print(f"Monkey {j}:{m}")
first,second=sorted([m.inspect_count for m in Monkey.all_monkeys])[-2:]

print(first*second)
