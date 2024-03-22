"""
# WE SOLVE THE CYCLE FINDING PROBLEM AS A GRAPH PROBLEM

This module aims to: use a built graph of the matrix to find at least
one cycle in the matrix (cost matrix).
we broke the problem down into two parts: first find all possible paths
from the start node, next find the paths that actually terminate in the 
start node neighbor while completes the cycle

# not as a certainty but supported with the claim: that a cycle always exists in 
this matrix, and that the DFS search algorith will find all possible paths 
we dare to moderately assert that this module will always find at least one cycle
from teh start node
"""

def get_mycycle(my_graph, start):

    # TRAVERSE GRAPH ....
    # we'll do a depth first traversal and find routes that end in the neighbors, these are the loops
    def traverse_graph(graph, start):
        routes = []  #to return
        stack = []
        visited = []
        path = []

        current_node = start
        visited.append(current_node)
        path.append(current_node)

        neighbors = graph[current_node]
        stack.extend(neighbors)

        while stack:
            current_node = stack.pop()
            
            visited.append(current_node)
            path.append(current_node)

            neighbors = graph[current_node]
            neighborchecked = []
            if (neighbors):
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in stack and neighbor!=start:
                        stack.append(neighbor)
                        neighborchecked.append(neighbor)
                        
                
            if(neighborchecked == [] or neighbors == []):
                print('path_found: ', path); routes.append(path[:])

                path.pop()  #pop of the defame one
                velid = False
                while velid==False:
                    if path !=[]:

                        b = path.pop()
                        for br in graph[b]:
                            if br not in visited: 
                                velid = True
                        if velid: path.append(b)

                    # thats exit condition
                    else: velid=True


        return routes        


    # cycle to return
    cycles = []
    # FINDCYCLE
    # find the cycles
    def find_cycles(routes, graph):
        for route in routes:
            for neighbor in graph[route[0]]:
                if neighbor in graph[route[-1]] and neighbor not in route:
                    cycles.append(route + [neighbor])
                    print(route + [neighbor])
                if neighbor == route[-1]:
                    cycles.append(route)
                    print(route)
        return cycles


    # ===============
    # PERFORM THESE THREE EVALUATIONS

    # routes = traverse_graph_with_cycle_detection(my_graph, start) 
    routes = traverse_graph(my_graph, start) 

    find_cycles(routes, my_graph)

    
    # print('cycles: ',cycles)

    return cycles
