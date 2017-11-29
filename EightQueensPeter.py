'''My take on Sheppard's 8-Queen Program
November 29, 2017'''

import random

size = 8

class Board(object):
    def __init__(self,genes,size):
        self.board = [['.'] * size for i in range(size)]
        for index in range(len(genes.genes)):
            row = genes.genes[index][0]
            col = genes.genes[index][1]
            self.board[row][col] = 'Q'

    def display(self):
        for i in range(size):
            print(self.board[i])

class Genes(object):
    def __init__(self):
        #generate 8 random [r,c] values:
        nums = [i for i in range(size)]
        row,col = random.sample(nums,size),random.sample(nums,size)
        self.genes = list(zip(row,col))
        #print("genes:",self.genes)

    def mutate(self):
        index = random.randint(0, len(self.genes) - 1)
        child = Genes()
        child.genes = list(self.genes)
        newGene = (random.randint(0,size-1),
                       random.randint(0,size-1))
        while newGene == child.genes[index]:
            newGene = (random.randint(0,size-1),
                       random.randint(0,size-1))
        child.genes[index] = newGene
        return child

    def calcFitness(self,board):
        self.rows_with_Queens = set()
        self.cols_with_Queens = set()
        self.up_diagonals_with_Queens = set()
        self.down_diagonals_with_Queens = set()
        for row in range(size):
            for col in range(size):
                if board.board[row][col] == 'Q':
                    self.rows_with_Queens.add(row)
                    self.cols_with_Queens.add(col)
                    self.up_diagonals_with_Queens.add(row+col)
                    self.down_diagonals_with_Queens.add(size-1-row+col)

        total = size - len(self.rows_with_Queens) + \
                size - len(self.cols_with_Queens) + \
                size - len(self.up_diagonals_with_Queens) + \
                size - len(self.down_diagonals_with_Queens)

        return total


def main(size=8):
    geneSet = Genes()
    board1 = Board(geneSet,size)
    board1.display()
    print(geneSet.genes,geneSet.calcFitness(board1))

    random.seed()
    bestParent = Genes()
    bestFitness = bestParent.calcFitness(board1)
    print("best:", bestParent.genes,bestFitness)

    while True:

        child = Genes()
        child.genes = list(bestParent.mutate().genes)
        #print("child1:", child.genes,child.calcFitness(board1))
        #print("bestP:",bestParent.genes,bestParent.calcFitness(board1))
        childFitness = child.calcFitness(board1)
        if bestFitness <= childFitness:
            continue
        print("child:", bestFitness, ''.join(child.genes))
        if childFitness == 0:
            break
        bestFitness = childFitness
        bestParent.genes = list(child.genes)

if __name__ == '__main__':
    main()