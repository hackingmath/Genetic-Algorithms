import pygame
from pygame.locals import *
import numpy as np
import random
from math import sqrt
# from travelingSalesperson.pyde

class City:
    def __init__(self, x, y, num):
        self.x = x
        self.y = y
        self.number = num  # identifying number

    def display(self):
        pygame.draw.circle(screen, CYAN, [self.x, self.y], 5)
        text = myfont.render(str(self.number),True,WHITE)
        text_rect=text.get_rect()
        text_rect.center=(self.x - 10, self.y - 10)
        screen.blit(text, text_rect)

class Route:
    def __init__(self):
        self.distance = 0
        # put cities in a list in random order:
        self.cityNums = np.arange(N_CITIES)
        np.random.shuffle(self.cityNums)

    def display(self):
        for i,n in enumerate(self.cityNums):
            if i == len(self.cityNums)-1:
                pygame.draw.line(screen, VIOLET, [cities[n].x, cities[n].y],
                                                [cities[self.cityNums[0]].x, cities[self.cityNums[0]].y],2)
            else:
                pygame.draw.line(screen,VIOLET,[cities[n].x, cities[n].y],
                                 [cities[self.cityNums[i+1]].x,cities[self.cityNums[i+1]].y],2)
            # then display the cities and their numbers
            cities[i].display()

    def calcLength(self):
        self.distance = 0
        for i, num in enumerate(self.cityNums):
            # find the distance to the previous city
            self.distance += dist(cities[num].x,
                                  cities[num].y,
                                  cities[self.cityNums[i - 1]].x,
                                  cities[self.cityNums[i - 1]].y)
        return self.distance

    def mutateN(self, num):
        indices=np.random.choice(N_CITIES, num,replace = False)
        #print("indices:",indices)
        child = Route()
        child.cityNums = np.copy(self.cityNums)
        #print("child:",child.cityNums)
        for i in range(num - 1):
            child.cityNums[indices[i]], child.cityNums[indices[(i + 1) % num]] = \
                child.cityNums[indices[(i + 1) % num]], child.cityNums[indices[i]]
        #print("mutated child:",child.cityNums)
        return child

    def crossover(self, partner):
        '''Splice together genes with partner's genes'''
        child = Route()
        # randomly choose slice point
        index = np.random.randint(1, N_CITIES - 2)
        # add numbers up to slice point
        child.cityNums = self.cityNums[:index]
        #print("child:",child.cityNums)
        # half the time reverse them
        if random.random() < 0.5:
            np.flip(child.cityNums)
        # list of numbers not in the slice
        notinslice = np.array([x for x in partner.cityNums if x not in child.cityNums])
        # add the numbers not in the slice
        child.cityNums = np.concatenate([child.cityNums,notinslice])
        #print("crossed:",child.cityNums)
        return child

def dist(a,b,c,d):
    return np.sqrt((a-c)**2+(b-d)**2)

# define constants
N_CITIES = 100
cities = []
random_improvements = 0
mutated_improvements = 0
population = []
POP_N = 1000  # number of routes

#define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
VIOLET = (148, 0, 211)

width,height = 800,800

# set up display
pygame.init()

#in case you use fonts:
pygame.font.init()
myfont = pygame.font.SysFont('Consolas', 24)
scorefont = pygame.font.SysFont('Consolas', 36)

screen = pygame.display.set_mode([width,height])
pygame.display.set_caption('Pygame Window') #add your own caption!
FPS = 60  # frames per second
clock = pygame.time.Clock()

counter = 0 #frame count

# loop until user clicks the close button
done = False

#"setup" sketch
for i in range(N_CITIES):
    cities.append(City(random.randint(50, width - 50),
                       random.randint(50, height - 50), i))
# put organisms in population list
for i in range(POP_N):
    population.append(Route())
best = random.choice(population)
record_distance = best.calcLength()
first = record_distance

while not done:
    for event in pygame.event.get():
        if event.type == QUIT:  # if pygame window is closed by user
            done = True
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if FPS == 60:
                    FPS = 300  #faster display
                else:
                    FPS = 60

    # fill the screen with background color
    screen.fill(BLACK)
    counter += 1
    best.display()
    #print(best.cityNums)
    #print(record_distance)
    first_record = scorefont.render("First: "+str(int(first)), True, RED)
    best_now = scorefont.render("Best: "+str(int(best.distance)),True,BLUE)
    screen.blit(first_record,[10,10])
    screen.blit(best_now,[500,10])

    population.sort(key=Route.calcLength)
    population = population[:POP_N]  # limit size of population
    length1 = population[0].calcLength()
    if length1 < record_distance:
        record_distance = length1
        best = population[0]

        # do crossover on population
    for i in range(POP_N):
        parentA, parentB = random.sample(population, 2)
        # reproduce:
        child = parentA.crossover(parentB)
        population.append(child)

    #mutateN the best in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = best.mutateN(i)
            population.append(new)

    # mutateN random Routes in the population
    for i in range(3,25):
        if i < N_CITIES:
            new = random.choice(population)
            new = new.mutateN(i)
            population.append(new)

    pygame.display.update()


    # for saving screenshots:
    # if counter %5 == 0:
    # Capture(screen, 'Capture{}.png'.format(counter), (0, 0), (600, 600))
    clock.tick(FPS)
pygame.quit()



