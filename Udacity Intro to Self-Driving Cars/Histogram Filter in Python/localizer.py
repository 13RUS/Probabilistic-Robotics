import pdb
from helpers import normalize, blur


def initialize_beliefs(grid):
    height = len(grid)
    width = len(grid[0])
    area = height * width
    belief_per_cell = 1.0 / area
    beliefs = []
    
    #print ('Initial beliefs:')  
    for i in range(height):
        row = []
        for j in range(width):
            row.append(belief_per_cell)
        #print (row)
        beliefs.append(row)
    return beliefs

def sense(color, grid, beliefs, p_hit, p_miss):
    new_beliefs = []
    beliefround = []
    
    print "We see color:", color
   
    height = len(beliefs)
    width = len(beliefs[0])
    
    for i in range (height):
        row = []
        for j in range (width):
            hit = (color == grid[i][j])
            row.append(beliefs[i][j]*(hit*p_hit + (1-hit)*p_miss))
        new_beliefs.append(row)
    
    s = 0
        
    for i in range (height):
        for j in range (width):
            s = s + new_beliefs[i][j]
    
    #this is my print
    #print '\nNew beliefs after sense:' 
    
    for i in range (height):
        row = []
        for j in range (width):
            new_beliefs[i][j] =  new_beliefs[i][j] / s
            #print("{:0.3f}".format(new_beliefs[i][j]))
            row.append (round (new_beliefs[i][j],10))
        beliefround.append(row) 
 
    
    for i in range (height):
        print beliefround[i]
    
    return new_beliefs

def move(dy, dx, beliefs, blurring): 
    height = len(beliefs)
    width = len(beliefs[0])
    new_G = [[0.0 for i in range(width)] for j in range(height)]
    
    print "Robot moves:", dy, dx
    for i, row in enumerate(beliefs):
        for j, cell in enumerate(row):
            new_i = (i + dy) % height
            new_j = (j + dx) % width
            #pdb.set_trace()
            new_G[int(new_i)][int(new_j)] = cell
     
    for i in range(height):
        row = []
        for j in range(width):
            row.append (round(new_G[i][j],10))
        print row
    
    return blur(new_G, blurring)
