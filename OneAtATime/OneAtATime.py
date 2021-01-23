# Script that copletes onefactor at a time and outputs a tornado graph
import matplotlib.pyplot as plt
import numpy as np
#Define a basic function with four variables, one input and one output.
def basic_function(x):

    return(x[0]**2 + 10*x[1] + 2*x[2]*(x[3]**0.5))

#How much will the varables vary by?
# This is given by the funtion below with two inputs and three outputs
def limits_function(Default_Varable, Varation_Percentage):
    # output the lower limit, then value, then upper limit
    return ((Default_Varable*(1-(Varation_Percentage/100)), Default_Varable, Default_Varable*(1+(Varation_Percentage/100))))

#New function here 

def OneFactorAtATime(numbers, change_percentages):

    #initialze the limits 
    numbers_limits=[]
    for ii in range (len(numbers)):
        limits=limits_function(numbers[ii], change_percentages[ii])
        numbers_limits.append((limits))


    #The other returned values
    min_scinarios= np.zeros((len(numbers),len(numbers)))
    max_scinarios=np.zeros((len(numbers),len(numbers)))
    for jj in range (len(numbers)):
        number_at_hand=numbers[jj]
        for kk in range (len(numbers)):
            if (numbers[kk]==number_at_hand):
                #Then print min limit
                #Then run the loop again
                current_limit=numbers_limits[kk]
                min_scinarios[kk,jj]=current_limit[0]
                max_scinarios[kk,jj]=current_limit[2]
                     
            else:
                current_number=numbers[jj]
                min_scinarios[kk,jj]=current_number
                max_scinarios[kk,jj]=current_number
    
    
    # Initilize Lows and Highs lists
    lows=[]
    highs=[]    
    #Default output of the function
    Default=basic_function(numbers)
    # Relitivize the output of the function as a percentage of the Default output  
    for ii in range (len(numbers)):
        lows.append((basic_function(min_scinarios[ii,:])-Default)/Default)
        highs.append((basic_function(max_scinarios[ii,:])-Default)/Default)


    # Plot on The Tornado Graph
    ## Firstly the name of the variables
    variables =[ 'Variable A', 'Variable B', 'Variable C', 'Variable D' ]
    plt.figure(1)
    base=0 # where the tornado graph is centered. 
    ys = range(len(lows))[::-1]  # The little bit of code "[::-1]" is required so that the results are printed top to bottom

    for y, low, high in zip(ys, lows, highs):
        low_width = (base - low)
        high_width = (high - base)

        # Each bar is a "broken" horizontal bar chart
        plt.broken_barh(
            [(100*low, 100*low_width), (base, 100*high_width)], # Multipled by 100 because it is a percentage
            (y - 0.4, 0.8),
            facecolors=['white', 'white'],  # Try different colors if you like
            edgecolors=['black', 'black'],
            linewidth=1,
        )
    # Draw a vertical line at the base varaible and gridlines
    plt.axvline(base, color='black')
    plt.grid()
    # Make the y-axis display the variables and write a x-axis label
    plt.yticks(ys, variables)
    plt.xlabel("Percentage Differential from Default [%]")
    plt.show()    
    return ()
    

#Now need to create table where we plot the results of changing one at a time
#Example Default Vaules, all to vary by 10% for now:
A=15
B=20
C=10
D=36
numbers=(A, B, C, D)
change_percentages=(10, 10, 10, 10)

OneFactorAtATime(numbers, change_percentages)