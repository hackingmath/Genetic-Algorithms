'''Sudoku Solver using Genetic Algorithm'''

import random
import copy
import pprint

N_BOARDS = 50000
matingpool = []

#unsolved board:

board1 = [[6,0,0,0,3,0,0,0,0],
        [4,0,3,8,0,5,0,0,0],
        [0,2,8,7,0,0,0,0,0],
        [8,0,0,0,0,4,3,6,0],
        [0,0,0,0,2,0,0,0,0],
        [0,3,4,6,0,0,0,0,1],
        [0,0,0,0,0,3,6,5,0],
        [0,0,0,5,0,8,7,0,2],
        [0,0,0,0,1,0,0,0,9]]

class Board(object):
    def __init__(self):
        self.boardList = self.createNewBoard()

    def createNewBoard(self):
        '''Takes a starting board and replaces zeroes
        with numbers'''
        newboard = copy.deepcopy(board1)
        for row in newboard:
            for i,num in enumerate(row):
                if num == 0:
                    n = random.randint(1,9)
                    while n in row:
                        n = random.randint(1,9)
                    row[i] = n
        return newboard

    def mutate(self):
        '''creates new row in board'''
        output = Board()
        #choose random number for row
        newboard = copy.deepcopy(self.boardList)
        #print("one:",board1)
        #change a random number of rows:
        rep = random.randint(0,len(newboard)-1)
        for r in range(rep):
            ind = random.randint(0,len(newboard)-1)
            #go through the row in board
            for i,col in enumerate(newboard[ind]):
                #check if number is fixed in board1
                if board1[ind][i] != 0:
                    newboard[ind][i] = board1[ind][i]
                else:
                    #If not, put in random integer
                    num1 = random.randint(1,9)
                    '''while num1 in newboard[ind]:
                        num1 = random.randint(1,9)'''
                    newboard[ind][i] = num1
                
        output.boardList = newboard[:]        
        return output

    def crossover(self,boardb):
        child = Board()
        ind = random.randint(1,len(self.boardList)-2)
        child.boardList = self.boardList[:ind]+boardb.boardList[ind:]
        return child

    def box(self,num):
        output = []
        box_sum = 0
        for n in range(3):
            output.append(self.boardList[3*(num//3)+n][(3*(num%3)):(3*(num%3))+3])
        for r in output:
            box_sum += sum(r)
        return box_sum

    def score(self):
        '''Takes in 9x9 matrix and scores
        rows, cols and boxes by how far their sum
        is away from 45. Returns sum of scores, so
        lower score is better.'''
        output = 0
        col_totals = [0 for k in range(len(self.boardList[0]))]
        for i, row in enumerate(self.boardList):
            #score is lowered by how far row sum is from 45
            output += abs(45 - sum(row))
            col_total = 0
            for j in range(len(self.boardList[0])):
                 col_totals[j] += self.boardList[i][j]
        for x in col_totals:
            output += abs(45 - x)
        for b in range(9):
            output += abs(45 - self.box(b))
            
        return output

board2=[[6,0,0,0,3,0,0,0,0],
        [4,0,3,8,0,5,0,0,6],
        [0,2,8,7,0,0,0,0,3],
        [8,0,2,0,5,4,3,6,0],
        [0,0,0,3,2,0,0,0,0],
        [0,3,4,6,8,0,0,0,1],
        [0,0,0,0,7,3,6,5,0],
        [3,0,0,5,0,8,7,1,2],
        [0,0,0,0,1,0,0,3,9]]

solved_board = [[6,5,7,4,3,2,1,9,8],
                [4,1,3,8,9,5,2,7,6],
                [9,2,8,7,6,1,5,4,3],
                [8,9,2,1,5,4,3,6,7],
                [1,7,6,3,2,9,4,8,5],
                [5,3,4,6,8,7,9,2,1],
                [2,8,1,9,7,3,6,5,4],
                [3,6,9,5,4,8,7,1,2],
                [7,4,5,2,1,6,8,3,9]]





#print(score(solved_board))
##for i in range(9):
##    print(box(board1,i))

generation = 0
no_improvements = 0
reps = 0

a = Board()
best = a
highScore = best.score()
globalbest = best
globalhigh = highScore

popn = [Board() for i in range(N_BOARDS)]

while reps < 20:
    reps += 1
    if highScore < globalhigh:
        globalhigh = highScore
        globalbest = best
    generation = 0
    no_improvements = 0

    a = Board()
    best = a
    highScore = best.score()

    popn = [Board() for i in range(N_BOARDS)]
    
    while highScore > 0:
        #increment generation
        generation += 1
        if no_improvements == 20:
            break
        print("gen:",generation)
        matingPool = copy.deepcopy(popn)
        matingPool.sort(key=Board.score)
        best_board = matingPool[0]
        newscore = best_board.score()
        if newscore == 0:
            pprint.pprint(i.boardList)
            break
        if newscore >= highScore:
            no_improvements += 1
            continue
        best = best_board
        highScore = newscore
        print("high:",highScore)
        print("globalhigh:",globalhigh)
        pprint.pprint(best.boardList)

        popn = popn[:N_BOARDS]
        matingPool = matingPool[:200]

        #do crossover
        mutations = []
        for i in range(1000):
            mutation = best.mutate()
            popn.append(mutation)
        for i in range(1000):
            parenta,parentb = random.sample(matingPool,2)
            popn.append(parenta.crossover(parentb))

        #add some random new boards
        for j in range(1000):
            popn.append(Board())

pprint.pprint(globalbest.boardList)
print("bestever:",globalhigh)
