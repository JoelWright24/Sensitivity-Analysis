import numpy as np
import random
import matplotlib.pyplot as plt
# Latin Hypercube Sampling 
# 1) Produce a range of inputs by deviding the range
# 2) Convert so that each input has a range
# 3) Choose a random number within that range
# 4) Shuffle one side x or y input to create random simulation parameters
# 5) Process the data

# Example

def simple_function(x,y):
    return(2*x - y**2 + 28)

def LatinHyperCubePerameters (limits_x, limits_y, data_points):
    range_x=np.linspace(limits_x[0],limits_x[1],data_points+1)
    range_y=np.linspace(limits_y[0],limits_y[1],data_points+1)
    # Now time to produce random numbers in this range
    # initialize the random lists
    x_randomized=[]
    y_randomized=[]

    for ii in range (data_points):
        x0=random.uniform(range_x[ii], range_x[ii+1])
        y0=random.uniform(range_y[ii], range_y[ii+1])
        x_randomized.append(x0)
        y_randomized.append(y0)

    #Next we need to shuffle one of them
    shuffled_x=random.sample(x_randomized, len(x_randomized))
    
    
    #Now we need to print the results when putting x and y in the function
    solution=np.zeros((2,data_points))
    for jj in range (data_points):
        solution[0,jj]=shuffled_x[jj]
        solution[1,jj]=y_randomized[jj]

    return(solution)

limits_x=((0,10))
limits_y=((0,5))
data_points= 1000
data=LatinHyperCubePerameters (limits_x, limits_y, data_points)
solution=simple_function(data[0],data[1])
plt.figure(1)
plt.xlabel("X-Data")
plt.ylabel("Function")
plt.scatter(data[0],solution)
plt.figure(2)
plt.xlabel("Y-Data")
plt.ylabel("Function")
plt.scatter(data[1],solution)
plt.show()

