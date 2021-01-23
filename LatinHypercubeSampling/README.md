# Sensitivity Analysis

 The folder, sensitivity analysis, is a toolbox for analysing the sensitivity of systems. In the script Latin_Hypercube_Sampling.py a simple function is included with only two variables. This is a proof of concept and the script can be edited for a more complex system.

## Latin Hypercube Sampling

Latin Hypercube Sampling is a memory intensive global sampling method to compare the effect of the varibles in a function.

Below are the steps to undertake Latin Hypercube Sampling for a known function with multiple varables:

1. Produce a range of inputs for each varable in the function.

2. Devide up the ranges into smaller ranges in each varbable.

3. Choose a random number within each small range for each varable.

4. Shuffle (n-1) of the varables input to create random simulation parameters.

5. Process the data by plotting it or looking at regression statistics.
