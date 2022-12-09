import os


class Position:
    def __init__(self):
        self.x=0
        self.y=0
    def up(self):
        self.x+=1
    def down(self):
        self.x-=1
    def left(self):
        self.y-=1
    def right(self):
        self.y+=1
    def __str__(self):
        return "x:{} y:{}".format(self.x,self.y)
    def move_adjacent(self,other):
        if(self.x-other.x>1):
            self.down()
            self.y=other.y
        elif(self.x-other.x<-1):
            self.up()
            self.y=other.y
        elif(self.y-other.y>1):
            self.left()
            self.x=other.x
        elif(self.y-other.y<-1):
            self.right()
            self.x=other.x
        else:
            pass
    def is_adjacent(self,other):
        return max(abs(self.x-other.x),abs(self.y-other.y))<=1

HERE=os.path.dirname(os.path.abspath(__file__))

head=Position()
tail=Position()
tail_position=set()
with open(os.path.join(HERE,"../input/input_9.txt"),"r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    for line in input:
        move,steps=line.split(" ")
        print("== {} ==".format(line))
        for j in range(int(steps)):
            if(move=='U'):
                head.up()
            elif(move=='D'):
                head.down()
            elif(move=='R'):
                head.right()
            else:
                head.left()
            tail.move_adjacent(head)
            print("head :{}\ttail :{}".format(head,tail))
            tail_position.add((tail.x,tail.y))
print(len(tail_position))
                
        

