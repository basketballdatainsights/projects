# Simulated Annealing
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
#Date:         4/22/2017

#need some python libraries
#import copy
from random import Random   #need this for the ranACdom number generation -- do not change
import numpy as np
import math           # for exponential function


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
          
#  set the intial temperature
def initial_temperature():
        
    x = np.random.choice([0,1], size=100, p=[1./3, 2./3])  # randomly set initial temperature
       
    return x
#begin Simulated Annealing overall logic ----------------

def coolingRatio(T,k):
    return(T - 0.01*k)

def probSelect(choice1, choice2, T):

    randChoice = myPRNG.randint(1,10)
    if randChoice <= math.exp((choice1[0] - choice2[0]) / T ):
        return(choice1)
    else:
        return(choice2)
        
    
def simulatedAnnealing():
    #variable to record the number of solutions evaluated
    solutionsChecked = 0
    Kt = 100             # number of iterations ()
    T = 100000              # set initial temperature
    Vc = initial_temperature()  #T, tempmarature, initialize at random 
    
    x_best = Vc[:]           #x_best will hold the best solution 
    f_curr = evaluate(Vc)   #f_curr will hold the evaluation of the current soluton
    f_best = f_curr[:]    

    while T > 0.01:    
        for k in list( range(1,Kt) ):
            solutionsChecked = solutionsChecked + 1
            # Choose random neighbor, Vn, of Vc
            Neighborhood = neighborhood(x_best)   # create a list of all neighbors in the neighborhood of x_curr
            randInt = myPRNG.randint(0,99)  # choose random integer for Neighborhood selection
            
            Vn = Neighborhood[ randInt ]                # choose random Neighborhood of Vc, call Vn
            #print(Vn[:])
            eval_of_Vn = evaluate(Vn)               # evaluate the random neighbor
            if eval_of_Vn[0] > f_best[0]:
                x_best = Vn[:]
                f_best = eval_of_Vn[:]
            else:
                x_best = probSelect(x_best[:], Vn[:], T)  # select new point with 30% probability
            #print( evaluate(x_best[:])[0] )
            T = coolingRatio(T,k)
            #print( "Temp:",T )
            k += 1  # increment to go to next loop
        #return(f_best, x_best)
        print ("\nTotal number of solutions checked: ", solutionsChecked)
        print ("Best values found so far: ", f_best)        
        
    print ("\nFinal number of solutions checked: ", solutionsChecked)
    print ("Best values found: ", f_best[0])
    print ("Weight is: ", f_best[1])
    print ("Total number of items selected: ", np.sum(x_best))
    print ("Best solution: ", x_best)    
    
# run Simulated Annealing on random problem instance
simulatedAnnealing()




