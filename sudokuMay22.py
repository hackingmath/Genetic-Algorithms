'''Sudoku Solver using Genetic Algorithm'''

input_board = [[6,0,0,0,3,0,0,0,0],
               [4,0,3,8,0,5,0,0,0],
               [0,2,8,7,0,0,0,0,0],
               [8,0,0,0,0,4,3,6,0],
               [0,0,0,0,2,0,0,0,0],
               [0,3,4,6,0,0,0,0,1],
               [0,0,0,0,0,3,6,5,0],
               [0,0,0,5,0,8,7,0,2],
               [0,0,0,0,1,0,0,0,9]]

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

def box(board,num):
    output = []
    box_sum = 0
    for n in range(3):
        output.append(board[3*(num//3)+n][(3*(num%3)):(3*(num%3))+3])
    for r in output:
        box_sum += sum(r)
    return box_sum

def score(board):
    '''Takes in 9x9 matrix and scores
    rows, cols and boxes by how far their sum
    is away from 45. Returns sum of scores, so
    lower score is better.'''
    score = 0
    col_totals = [0 for k in range(len(board[0]))]
    for i, row in enumerate(board):
        #score is lowered by how far row sum is from 45
        score += abs(45 - sum(row))
        col_total = 0
        for j in range(len(board[0])):
             col_totals[j] += board[i][j]
    for x in col_totals:
        score += abs(45 - x)
    for b in range(9):
        score += abs(45 - box(board,b))
        
    return score



print(score(solved_board))
##for i in range(9):
##    print(box(input_board,i))
