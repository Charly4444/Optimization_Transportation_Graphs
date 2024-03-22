### IMPLEMENTATION OF THE SOLUTION OF TRANSPORTATION PROBLEM BY NORTHWEST METHOD AND THE POTENTIAL DIFFERENCE (U-V) methods {USING GRAPHS}

##### This Project serves as an initila implementation of a CLOSED type transportation problem common in the filed of Optimization.
###### The PDsolver includes all the called functions and logic flow from the app (newapp.py)
The contents of the project are thus:
##### newapp -> this is the main app that runs and allows you try a 'new' problem
##### northwest -> this module implements the northwest algorithm for initial sols
##### getdeltancell -> getdeltancell computes the potentials of the cells and returns a prefeffered for the start of search of an improvement cycle
##### getgraph => gets the graph of the current problem, THE CYCLE SEARCH IS SOLVED AS A GRAPH PROBLEM
##### getcycle -> getcycle finds a possible improvement cycle to be explored at start, the result which is used to adjust the matrix
##### adjustthematrix -> this program does the required adjustment on the transport matrix to obtain the new look.

The app can serve to search feasible solution for optimization tasks that can be modeled as Tranportation problems
(Charles. 24)