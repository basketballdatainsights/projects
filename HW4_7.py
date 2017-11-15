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
#Date:         4/22/17

#need some python libraries
#import copy
from random import Random   #need this for the ranACdom number generation -- do not change
import numpy as np
import time                # time function


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
def oneFlip(x):
        
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

def doubleFlip(x):
        
    nbrhood = []     
    
    # so, I'm saying: Let me set up my 100 neighbors:
    for i in range(0,n-1):
        nbrhood.append(x[:])
        # Now, the list is composed of 100 lists in it
        if nbrhood[i][i] == 1:   #ith element of list i
            nbrhood[i][i] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i] = 1

        if nbrhood[i][i+1] == 1:   #ith element of list i
            nbrhood[i][i+1] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i+1] = 1
    return nbrhood
    
def tripleFlip(x):
   
    nbrhood = []     
    
    # so, I'm saying: Let me set up my 100 neighbors:
    for i in range(0,n-2):
        nbrhood.append(x[:])
        # Now, the list is composed of 100 lists in it
        if nbrhood[i][i] == 1:   #ith element of list i
            nbrhood[i][i] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i] = 1

        if nbrhood[i][i+1] == 1:   #second flip
            nbrhood[i][i+1] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i+1] = 1

        if nbrhood[i][i+2] == 1:   #third flip
            nbrhood[i][i+2] = 0
        else:                 #flip 0s to 1s and 1s to 0 for each 100 elements
            nbrhood[i][i+2] = 1
    return nbrhood
          
#create the initial solution
def starting_solution():
    
    x = np.random.choice([0,1], size=100, p=[1./3, 2./3]) 
        
    return x

def localSearch(x,first_improve=False):
    solutionsChecked = 0
    x_curr = x  #x_curr will hold the current solution     
    x_best = x_curr[:]           #x_best will hold the best solution 
    f_curr = evaluate(x_curr)   #f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]    
    
    done = 0           #boolean integer
    
    while done == 0:
      
        Neighborhood = oneFlip(x_curr)   # create a list of all neighbors in the neighborhood of x_curr
        
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
    return(x_best, f_best, solutionsChecked)
    #print(x_curr, f_curr, solutionsChecked)
    #return(x_best, solutionsChecked)

            
def VNS(): 
    timeOut = time.time() + 60    # make sure we are done within a minute
    while True:
    #variable to record the number of solutions evaluated
        solutionsChecked = 0      
        s0 = starting_solution()   
        x_best = s0[:]           #x_best will hold the best solution 
        f_curr = evaluate(s0)   #f_curr will hold the evaluation of the current soluton
        f_best = f_curr[:]    
        k = 1
        
        while k <= 3: 
            if k == 1:
                Neighborhood = tripleFlip(x_best)
            elif k == 2:
                Neighborhood = doubleFlip(x_best)
            elif k == 3: 
                Neighborhood = oneFlip(x_best)

            n = len(Neighborhood) - 1       # store upper bound on random number selection
            randInt = myPRNG.randint(0,n)   # choose random integer for Neighborhood selection
            s = Neighborhood[ randInt ]     # choose random neighbor in current Neighborhood
            
            s_star = localSearch(s)
            s_soln = s_star[0]
            eval_of_s = s_star[1]
            solutionsChecked = solutionsChecked + s_star[2]
                  # evaluate the random neighbor
            if eval_of_s[0] > f_best[0] :
                x_best = s_soln[:]
                f_best = eval_of_s[:]
                k = 1
            else:
                x_curr = x_best[:]         #else: move to the neighbor solution and continue
                f_curr = f_best[:]         #evalute the current solution
                k += 1
            print(x_best, solutionsChecked)
        t = time.time()
        if t > timeOut:
            break
    
      
    print ("\nFinal number of solutions checked: ", solutionsChecked)
    print ("Best values found: ", f_best[0])
    print ("Weight is: ", f_best[1])
    print ("Total number of items selected: ", np.sum(x_best))
    print ("Best solution: ", x_best)    
    
    
#begin local search overall logic ----------------
VNS()







