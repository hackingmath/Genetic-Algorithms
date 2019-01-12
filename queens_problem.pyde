'''Queens Problem
January 11, 2019
with Curtis'''

import random

RANK = 4

class Cell:
    def __init__(self,r,c,queen,sz):
        self.queen = queen
        self.sz = sz
        self.loc = PVector(c*self.sz,r*self.sz)
        
        
    def update(self):
        noFill()
        rect(self.loc.x,
             self.loc.y,
             self.sz,self.sz)
        if self.queen:
            fill(0)
            text("Q",self.loc.x+self.sz/2.0,
                 self.loc.y+self.sz/2.0)

class Grid:
    def __init__(self,rank,numList):
        self.sz = 600/float(rank)
        self.numList = numList
        self.cellList = []
        for i,v in enumerate(numList):
            self.cellList.append(Cell(i//rank,
                                      i%rank,
                                      'Q' if v == 1 else '',
                                      self.sz))
    def update(self):
        for cell in self.cellList:
            cell.update()
            
    def score(self):
        #stack numlist
        self.newList = []
        count = 0
        for i in range(RANK):
            self.newList.append([])
            for j in range(RANK):
                self.newList[i].append(self.numList[count])
                count += 1
        for row in self.newList:
            if row.count(1) != 1:
                
            
def setup():
    global g
    size(600,600)
    textSize(24)
    indices = random.sample(list(range(RANK**2)),RANK)
    cList = [0]*RANK**2
    for i in indices:
        cList[i] = 1
    g = Grid(RANK,cList)
    println(cList)
    
def draw():
    global g
    g.update()
    n = g.score()
    println(n)
    noLoop()
