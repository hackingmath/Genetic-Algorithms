'''Genetic Quote with Colin
November 29, 2017'''

import random

target = "Oh, say can you see, by the dawn's early light?"
characters = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.',?!"

#function to create a "guess" list of characters the same length as target
def makeList():
    charList = [] #empty list to fill with random characters
    for i in range(len(target)):
        charList.append(random.choice(characters))

    #print(''.join(charList))
    return charList

#function to "score" the guess list by comparing it to target

def score(mylist):
    '''Returns one integer: the number of matches with target'''
    matches = 0
    for i in range(len(target)):
        if mylist[i] == target[i]:
            matches += 1
    return matches

#function to "mutate" a list by randomly changing one letter

def mutate(mylist):
    '''Returns mylist with one letter changed'''
    newlist = list(mylist)
    new_letter = random.choice(characters)
    index = random.randint(0,len(target)-1)
    newlist[index] = new_letter
    return newlist

#create a list, set the list to be the bestList
#set the score of bestList to be the bestScore
random.seed()
bestList = makeList()
bestScore = score(bestList)

counter = 0

#make an infinite loop that will create a mutation
#of the bestList, score it
while True:
     
    guess = mutate(bestList)
    guessScore = score(guess)
    #print(''.join(bestList),bestScore)

#if the score of the newList is lower than the bestList,
#"continue"
    if guessScore <= bestScore:
        continue

#otherwise if the score of the newlist is the optimal score,
#print the list and break out of the loop
    print(''.join(guess),guessScore,counter)
    if guessScore == len(target):
        break

#otherwise, set the bestList to the value of the newList
#and the bestScore to be the value of the score of the newList
    bestList = list(guess)
    bestScore = guessScore

    counter += 1

'''guessList = makeList()
print(''.join(guessList),score(guessList))
guess2 = mutate(guessList)
print(''.join(guess2),score(guess2))'''
