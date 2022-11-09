# FILENAME gol.py in the main,py
# First Last: Jerusha Theobald
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: 


import copy
import random
import sys
import time

# The WIDTH and HEIGHT of cell grid.
WIDTH = 4  
HEIGHT = 4  
 
# The character representing a living cell and dead cell respectively.
ALIVE = 'O'  
DEAD = 'X'   
 
# Note: nextCells and cell  dictionaries 
# The indexes of the list are (x, y) with DEAD 'X' or ALIVE 'O' randomvalues
nextCells = {}

# Loop over columns and rows 
for x in range(WIDTH):  
     for y in range(HEIGHT): 

# Randomize starting cells as ALIVE or DEAD
         if random.randint(0, 1) == 0:
             nextCells[(x, y)] = ALIVE  
         else:
             nextCells[(x, y)] = DEAD  

# Iteration of loop
while True:  
     print('\n' * 1)  
     cells = copy.deepcopy(nextCells)
 
     for y in range(HEIGHT):
         for x in range(WIDTH):

# New line printed at end of the row
             print(cells[(x, y)], end='')  
         print()    
 
# Get neighboring coordinates for next cells from current cells
     for x in range(WIDTH):
         for y in range(HEIGHT):
             left  = (x - 1) % WIDTH
             right = (x + 1) % WIDTH
             above = (y - 1) % HEIGHT
             below = (y + 1) % HEIGHT
 
# Number of living neighbors 
             numNeighbors = 0

# Check if top-left, top, top-right, left, right, 
# bottom-left, bottom, bottom-right neighbor's alive.

             if cells[(left, above)] == ALIVE:
                 numNeighbors += 1  

             if cells[(x, above)] == ALIVE:
                 numNeighbors += 1  
           
             if cells[(right, above)] == ALIVE:
                 numNeighbors += 1  
                
             if cells[(left, y)] == ALIVE:
                 numNeighbors += 1  
             
             if cells[(right, y)] == ALIVE:
                 numNeighbors += 1  
               
             if cells[(left, below)] == ALIVE:
                 numNeighbors += 1  
                 
             if cells[(x, below)] == ALIVE:
                 numNeighbors += 1  

             if cells[(right, below)] == ALIVE:
                 numNeighbors += 1  
 
# Game rules: living cells with 2 or 3 neighbors remain ALIVE and
# dead cells with 3 neighbors become ALIVE

             if cells[(x, y)] == ALIVE and (numNeighbors == 2
                 or numNeighbors == 3):
                     nextCells[(x, y)] = ALIVE

             elif cells[(x, y)] == DEAD and numNeighbors == 3:
                 nextCells[(x, y)] = ALIVE
                 
# Remainang cells die or stay DEAD
             else:
                 nextCells[(x, y)] = DEAD
