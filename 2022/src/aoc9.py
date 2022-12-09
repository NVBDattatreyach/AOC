import os
import math
HERE=os.path.dirname(os.path.abspath(__file__))

class Knot:
    def __init__(self):
        self.x=0
        self.y=0
    def move_x(self,k):
        self.x+=k
    def move_y(self,k):
        self.y+=k
    def __str__(self):
        return "x:{} y:{}".format(self.x,self.y)
    def move_adjacent(self,other):
        distance=max(abs(self.x-other.x),abs(self.y-other.y))
        if(distance>1):
            if(self.x==other.x):
                self.move_y((other.y-self.y)//2)
            elif(self.y==other.y):
                self.move_x((other.x-self.x)//2)
            else:
                self.move_x(math.copysign(1,(other.x-self.x)/2))
                self.move_y(math.copysign(1,(other.y-self.y)/2))
                

knots=[Knot() for _ in range(10)]
tail_position=set()
up=lambda a:a.move_y(1)
down=lambda a:a.move_y(-1)
left=lambda a:a.move_x(-1)
right=lambda a:a.move_x(1)

moves={'U':up,'D':down,'L':left,'R':right}
with open(os.path.join(HERE,"../input/input_9.txt"),"r") as f:
    input=[x.strip("\n") for x in f.readlines()]
    for line in input:
        move,steps=line.split(" ")
        for j in range(int(steps)):
            moves[move](knots[0])
            for i in range(1,10):
               knots[i].move_adjacent(knots[i-1])
            tail_position.add((knots[-1].x,knots[-1].y))
            
print(len(tail_position))

        

