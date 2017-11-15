#basic hill climbing search provided as base code for the DSA/ISE 5113 course
#author: Charles Nicholson
#date: 4/5/2017

#NOTE: YOU MAY CHANGE ALMOST ANYTHING YOU LIKE IN THIS CODE.  
#However, I would like all students to have the same problem instance, therefore please do not change anything relating to:
#   random number generation
#   number of items (should be 100)
#   random problem instance
#   weight limit of the knapsack

#------------------------------------------------------------------------------

#Student name: Alex Beene
#Date:          4/22/17

#need some python libraries
#import copy
from random import Random   #need this for the ranACdom number generation -- do not change
import numpy as np


#to setup a random number generator, we will specify a "seed" values
#need this for the random number generation -- do not change
seed = 5113
myPRNG = Random(seed)

# to get a random number between 0 and 1, use this:             myPRNG.random()
# to get a random number between lwrBnd and upprBnd, use this:  myPRNG.uniform(lwrBnd,upprBnd)
# to get a random integer between lwrBnd and upprBnd, use this: myPRNG.randint(lwrBnd,upprBnd)

#number of elements in a solution
n = 100

# create an "instance" for the knapsack problem
values = []
for i in range(0,n):
    values.append(myPRNG.uniform(10,100))  
    #append result to random number generator to list, values
    #randomly assign objects between 10 and 100 to my list
    
weights = []
for i in range(0,n):
    weights.append(myPRNG.uniform(5,20))
    #same for weights: randomly and uniformly distributed between 5 and 20
    
# Probability of hill climb versus random walk
probs = []
for i in range(0,n):
    probs.append(myPRNG.randint(0,1))
    
# define max weight for the knapsack
maxWeight = 5*n   #total values of 500 for instances

# change anything you like below this line ------------------------------------

# monitor the number of solutions evaluated
solutionsChecked = 0      #keep a running count of solutions evaluated so far



# function to evaluate a solution x
def evaluate(x):
          
    a=np.array(x)
    b=np.array(values)
    c=np.array(weights)
    
    totalvalues = np.dot(a,b)     #compute the values of the knapsack selection
    totalWeight = np.dot(a,c)    #compute the weight values of the knapsack selection
    
    if totalWeight > maxWeight: # This is infeasible so return zeros
        return [0.0, 0.0]
    
    return [totalvalues, totalWeight]   #returns a list of both total values and total weight
          
       
# here is a simple function to create a neighborhood
# 1-flip neighborhood of solution x         
def neighborhood(x):
        
    nbrhood = []     
    # in the 1-flip neighborhood, you have 100 neighbors
    
    # so, I'm saying: Let me set up my 100 neighbors:
    for i in range(0,n):
        nbrhood.append(x[:])
        # Now, the list is composed of 100 lists in it
        if nbrhood[i][i] == 1:   #ith element of list i
            nbrhood[i][i] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i] = 1
      
    return nbrhood
          
#create the initial solution
def initial_solution():
        
    # Init all 0s for initial list solution
    #x = [0]*n
    x = np.random.choice([0,1], size=100, p=[1./3, 2./3])

    # Sort the valuess and get the corresponding indeces of those valuess
#    indeces = sorted(range(len(values)), key=lambda k: values[k])
#    indeces = indeces[::-1] # now reverse the order so largest values indeces first
#    
#    # Init total weight to zero to begin
#    ttl = 0
#    # Loop thru the indeces from the front now since these are the highest vals
#    for i in indeces:
#        ttl += weights[i]     # add to ttl weight until we have reached 500 lbs
#        if ttl <= maxWeight:
#            x[i] = 1          # set this as a solution
#        else:
#            break             # we've reached the weight limit so break loop
            
    return x


def steepestAscent(first_improve=False):
    #variable to record the number of solutions evaluated
    solutionsChecked = 0
    
    x_curr = initial_solution()  #x_curr will hold the current solution     
    x_best = x_curr[:]           #x_best will hold the best solution 
    f_curr = evaluate(x_curr)   #f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]    
    
    done = 0           #boolean integer
    
    while done == 0:
      
        Neighborhood = neighborhood(x_curr)   # create a list of all neighbors in the neighborhood of x_curr
        
        for s in Neighborhood:                #evaluate every member in the neighborhood of x_curr
            solutionsChecked = solutionsChecked + 1
            #Everything here repeated for every element in my neighborhood
            eval_of_s = evaluate(s)
            if eval_of_s[0] > f_best[0]: # this is steepest ascent (#2)
                x_best = s[:]                 #find the best member and keep track of that solution         
                #Slicing operator: Make copy of list s, and assign to variable, x_best
                #Every variable is essentially like a pointer, points to a place in memory
                #Ensure x_best is a copy of solution
                f_best = eval_of_s[:]       #and store its evaluation
                if first_improve:
                    break # This is for first improvement (#3)
        
        if f_best == f_curr:               #if there were no improving solutions in the neighborhood
            done = 1
        else:
            
            x_curr = x_best[:]         #else: move to the neighbor solution and continue
            f_curr = f_best[:]         #evalute the current solution
            
            print ("\nTotal number of solutions checked: ", solutionsChecked)
            print ("Best values found so far: ", f_best)        
        
    print ("\nFinal number of solutions checked: ", solutionsChecked)
    print ("Best values found: ", f_best[0])
    print ("Weight is: ", f_best[1])
    print ("Total number of items selected: ", np.sum(x_best))
    print ("Best solution: ", x_best)    


def randomRestart():
    #variable to record the number of solutions evaluated
    solutionsChecked = 0
    
    x_curr = initial_solution()  #x_curr will hold the current solution     
    x_best = x_curr[:]           #x_best will hold the best solution 
    f_curr = evaluate(x_curr)   #f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]    
    
    done = 0           #boolean integers
    
    while done == 0:
      
        Neighborhood = neighborhood(x_curr)   # create a list of all neighbors in the neighborhood of x_curr
        
        random_nei_solutions = []
        for i in range(0,n):
            random_nei_solutions.append(myPRNG.randint(0,99))          
        
        for i in range(0,10):                #evaluate 10 members in the neighborhood of x_curr
            solution_index = random_nei_solutions[i]
            s = Neighborhood[solution_index]
            solutionsChecked = solutionsChecked + 1
            #Everything here repeated for every element in my neighborhood
            eval_of_s = evaluate(s)
            if eval_of_s[0] > f_best[0]: # this is steepest ascent (#2)
                x_best = s[:]                 #find the best member and keep track of that solution         
                #Slicing operator: Make copy of list s, and assign to variable, x_best
                #Every variable is essentially like a pointer, points to a place in memory
                #Ensure x_best is a copy of solution
                f_best = eval_of_s[:]       #and store its evaluation
        
        if f_best == f_curr:               #if there were no improving solutions in the neighborhood
            done = 1
        else:            
            x_curr = x_best[:]         #else: move to the neighbor solution and continue
            f_curr = f_best[:]         #evalute the current solution
            
            print ("\nTotal number of solutions checked: ", solutionsChecked)
            print ("Best values found so far: ", f_best)        
        
    print ("\nFinal number of solutions checked: ", solutionsChecked)
    print ("Best values found: ", f_best[0])
    print ("Weight is: ", f_best[1])
    print ("Total number of items selected: ", np.sum(x_best))
    print ("Best solution: ", x_best)    
    
def randomWalk():
    #variable to record the number of solutions evaluated
    solutionsChecked = 0
    
    x_curr = initial_solution()  #x_curr will hold the current solution     
    x_best = x_curr[:]           #x_best will hold the best solution 
    f_curr = evaluate(x_curr)   #f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]    
    
    done = 0           #boolean integer
    while done == 0:
      
        Neighborhood = neighborhood(x_curr)   # create a list of all neighbors in the neighborhood of x_curr      
        for p in probs:
            if p:
                for s in Neighborhood: 
                    solutionsChecked = solutionsChecked + 1
                    #Everything here repeated for every element in my neighborhood
                    eval_of_s = evaluate(s)
                    if eval_of_s[0] > f_best[0]: # this is steepest ascent (#2)
                        x_best = s[:]                 #find the best member and keep track of that solution         
                       #Ensure x_best is a copy of solution
                        f_best = eval_of_s[:]       #and store its evaluation
	    # random walk
            else: 
                i = myPRNG.randint(0,99)
                solutionsChecked += 1
                eval_of_s = evaluate(Neighborhood[i])
                if eval_of_s[0] > f_best[0]: # this is steepest ascent (#2)
                    x_best = Neighborhood[i][:]#find the best member and keep track of that solution         
                    f_best = eval_of_s[:] 	    
	    
        if f_best == f_curr:               #if there were no improving solutions in the neighborhood
            done = 1
        else:            
            x_curr = x_best[:]         #else: move to the neighbor solution and continue
            f_curr = f_best[:]         #evalute the current solution
            
            print ("\nTotal number of solutions checked: ", solutionsChecked)
            print ("Best values found so far: ", f_best)        
        
    print ("\nFinal number of solutions checked: ", solutionsChecked)
    print ("Best values found: ", f_best[0])
    print ("Weight is: ", f_best[1])
    print ("Total number of items selected: ", np.sum(x_best))
    print ("Best solution: ", x_best)    
    
#begin local search overall logic ----------------
#steepestAscent()
#steepestAscent(True)
#randomRestart()
randomWalk()




