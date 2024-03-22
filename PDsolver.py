from getgraph import build_graph
from getdeltancell import generate_delta_matrix
from getcycle import get_mycycle
from adjustthematrix import modify_matrix
from cal_cost import cal_cost
import copy

"""
So this will attempt to find a better solution based on the 
potential difference method
"""
def pdsolver(transport_matrix):
    # Create a copy of the original transportation matrix
    # this prevents it from modifying the previous, this can save us undesirable behaviour
    # incase you didnt know
    # ALWAYS REMEBER => Arrays are passed as POINTERS
    transportation_matrix = copy.deepcopy(transport_matrix)
    # ENTER HERE THE COST MATRIX FOR TESTING:
    unit_cost_mx = [[3,11,3,10],
                    [1,9,2,8],
                    [7,4,10,5]]
    

    print("unit_costs: "); print(unit_cost_mx)
    # # SINCE PROBLEM IS CLOSED WE ARE NOT CHECKING FOR IMBALABNCES AS WE COMPUTED DEMAND OURSELVES
    # # THE TRANSPORTATION MATRIX IS NOT A NECESSARY ARGUMENT BUT YOU CAN PASS
    # transportation_matrix = northwest_algo(demand, products, transportation_costs)

    
    def print_matrix(matrix):
        for row in matrix:
            print(row)
    
    # see transport_matrix
    print("Transportation Matrix:")
    print_matrix(transportation_matrix)

    # SEE COST
    cost_now = cal_cost(transportation_matrix,unit_cost_mx)
    print('cost_now',cost_now)

    
    # GET GRAPH(for reasons)
    my_graph = build_graph(transportation_matrix)

    # GET DELTAS, N START CELL n check
    potential_vars, sorted_cell_pts, is_optimal = generate_delta_matrix(transportation_matrix)
    print('potential_vars: ',potential_vars)
    print('is_optimal: ',is_optimal)

    valid_starts = []
    # Check if chosen start cell is in graph
    for start_cx in sorted_cell_pts:
        i, j, delta = start_cx  # Unpack the tuple
        if my_graph.get((i, j)):
            valid_starts.append((i, j))
    
    i=0
    start_cell = valid_starts[i]

    print('sorted_cells: ',sorted_cell_pts)
    print('start_cell: ',start_cell)

    cycle=[]
    # GET CYCLE
    cycles = get_mycycle(my_graph,start_cell)
    # when empty
    while cycles == [] and len(valid_starts)>0: 
        i+=1
        start_cell=valid_starts[i]
        cycles = get_mycycle(my_graph,start_cell)
        if cycles !=[]: cycle=cycles[0]
    
    # normal_
    if cycles: cycle=cycles[0]

    if cycle == []: return("NO IMPROVEMENT CYCLE FOUND")
        
    

    print('cycle: ', cycle)

    
    # ADJUST MATRIX
    adjusted_matrix = modify_matrix(transportation_matrix,cycle)
    print('adjusted_matrix',adjusted_matrix)

    # # Check if the adjusted matrix is the same as the original transport matrix
    # if adjusted_matrix == transportation_matrix:
    #     print("No improvement achieved with the current cycle.")
    #     # Move to the next valid start point if available
    #     if i + 1 < len(valid_starts):
    #         i += 1
    #         start_cell = valid_starts[i]
    #         cycle = get_mycycle(my_graph,start_cell)
    #         if cycle !=[]: cycle=cycle[0]
    #         # RECALC ADJUST MATRIX
    #         adjusted_matrix = modify_matrix(transportation_matrix,cycle)
    #         print('adjusted_matrix-2: ',adjusted_matrix)
    #     else:
    #         return "No improvement cycles found with any valid start point."
        
    # CALC COST
    cost_now = cal_cost(adjusted_matrix,unit_cost_mx)
    print('cost_now: ',cost_now)


    return adjusted_matrix, cycle, cost_now
