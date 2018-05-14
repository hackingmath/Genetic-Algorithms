'''Knapsack Problem
May 14, 2018'''

import random

#(weight, value)
boxes = [(5,10),(4,40),(6,30),(3,50)]
#boxes = [(2,3),(3,4),(4,5),(5,6)]
'''boxes = [(12,4),
         (1,2),
         (4,10),
         (1,1),
         (2,2)]'''

MAXWEIGHT = 10
MAXPOPN = 100
population = []
MAXGENS = 100
generation = 1
matingPool = []

class Pack(object):
    def __init__(self):
        '''Returns a list as a solution'''
        self.boxList = [random.randint(0,1) for i in range(len(boxes))]
        self.weight = 0
        self.value = 0
        for i in range(len(boxes)):
            self.weight += self.boxList[i]*boxes[i][0]
            self.value += self.boxList[i]*boxes[i][1]
        #print(self.value,end = ',')
        

    def score(self):
        '''Returns one integer: the value of the list'''
        #this was for if there should only be n items
        '''if sum(self.boxList) != 4:
            return 0'''
        if self.weight > MAXWEIGHT:
            return 0
        return self.value

    def crossover(self,parent2):
        child = Pack()
        index = random.randint(0,len(boxes)-1)
        child.boxList = self.boxList[:index]+parent2.boxList[index:]
        return child

    def mutate(self):
        child = Pack()
        for i,v in enumerate(self.boxList):
            if random.random() < 0.5:
                n = random.randint(0,1)
                child.boxList[i] = n
        return child

population = [Pack() for i in range(MAXPOPN)]
'''for p in population:
    print(p.value)'''
newpopn = []

bestList = Pack() #first one is the best so far
bestScore = bestList.score()

for g in range(MAXGENS):
    #print(bestList.boxList,"score:",bestScore,"weight:",bestList.weight,g)
    matingPool = []
    #sort popn list
    population.sort(key=Pack.score)
    matingPool = population[::-1]
    '''for a in matingPool[:10]:
        print(a.score(),end=',')'''
    '''b = population[0]
    sc = b.score()
    if sc == 0:
        b = b.mutate()
    if sc > bestScore:
        bestList = b #new bestList
        print("best:",bestList.boxList)
        bestScore = sc
        child = bestList.mutate()
        print("child",child.boxList)
        matingPool.append(child)
    for i in range(sc):
        matingPool += [b]
    #go through pop'n list'''
    for p in population:
        sc = p.score() #score each list
        if sc == 0:
            population.remove(p)
        #print("score:",sc)
        if sc > bestScore:
            bestList = p #new bestList
            print("best:",bestList.boxList)
            bestScore = sc
            child = bestList.mutate()
            print("child",child.boxList)
            matingPool.append(child)
        #for i in range(sc):
        matingPool.append(p)
    for i in range(MAXPOPN):
        parent1,parent2 = random.sample(matingPool,2)
        child = parent1.crossover(parent1)
        newpopn = [child] + newpopn
    newpopn = newpopn[:MAXPOPN]
    population = newpopn[::] #newpopulation becomes population
    mutants = random.sample(population,50)
    for m in mutants:
        m.mutate()
    population += mutants
    #print(len(population))
    print(bestList.boxList,"score:",bestScore,"weight:",bestList.weight,g)

'''for p in population[:10]:
    print(p.boxList,p.value)'''

