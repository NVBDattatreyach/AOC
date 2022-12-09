import os
import time

class Knot:
    def __init__(self):
        self.x=0
        self.y=0
    def up(self):
        self.y+=1
    def down(self):
        self.y-=1
    def left(self):
        self.x-=1
    def right(self):
        self.x+=1
    def __str__(self):
        return "x:{} y:{}".format(self.x,self.y)
    def move_adjacent(self,other):
        if(self.y-other.y>1):
            self.down()
            if(self.x>other.x):
                self.left()
            elif(self.x<other.x):
                self.right()
        elif(self.y-other.y<-1):
            self.up()
            if(self.x>other.x):
                self.left()
            elif(self.x<other.x):
                self.right()
        elif(self.x-other.x>1):
            self.left()
            if(self.y>other.y):
                self.down()
            elif(self.y<other.y):
                self.up()
        elif(self.x-other.x<-1):
            self.right()
            if(self.y>other.y):
                self.down()
            elif(self.y<other.y):
                self.up()
    def is_adjacent(self,other):
        return max(abs(self.x-other.x),abs(self.y-other.y))<=1

HERE=os.path.dirname(os.path.abspath(__file__))

knots=[Knot() for _ in range(10)]
tail_position=set()
with open(os.path.join(HERE,"../input/input_9.txt"),"r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    max_x=0
    min_x=0
    max_y=0
    min_y=0
    for line in input:
        move,steps=line.split(" ")
        print("== {} ==".format(line))
        for j in range(int(steps)):
            if(move=='U'):
                knots[0].up()
            elif(move=='D'):
                knots[0].down()
            elif(move=='R'):
                knots[0].right()
            else:
                knots[0].left()
            max_x=max(max_x,knots[0].x)
            min_x=min(min_x,knots[0].x)
            max_y=max(max_y,knots[0].y)
            min_y=min(min_y,knots[0].y)
            for i in range(1,10):
                knots[i].move_adjacent(knots[i-1])
                max_x=max(max_x,knots[i].x)
                min_x=min(min_x,knots[i].x)
                max_y=max(max_y,knots[i].y)
                min_y=min(min_y,knots[i].y)
                
            tail_position.add((knots[-1].x,knots[-1].y))
            
print(len(tail_position),min_x,min_y,max_x,max_y)
                
        
