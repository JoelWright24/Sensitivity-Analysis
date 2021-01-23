# One Factor at a Time

One Factor at a time is a local method of Sensitivity Analysis. It takes on board a function and, as the name suggests, shows the effect of ultering one perameter at a time.

In this file, a system has been simplified down to an exquation with four variables:

$$ x_{0}^{2} + 10x_{1} + 2 x_{2} \sqrt{x_{3}}$$

The script takes in an asrray for the default value of each variable and the percentage that each value is subject to change (the uncertainty of the value).
The script outputs a Tornado graph which is an easy-to-read graph of the relative affect each variable has on the fuction.

## Limitations of local sensitivity analysis methods

While Latin Hypercube Sampling is a global method, “One Factor at a Time” is only a local method of sensitivity analysis.

Local methods of sensitivity analysis compare one change to the default state, but do not compare changes to a system when it is away from its default state.

Therefore, local methods are good for understanding a basic affect of a system. But when a system is complex, global systems give a better overview and provide better information to make informed design decisions.
