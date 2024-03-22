"""
This module will generate the delta matrix and on the basis of this select 
which cell will be the starting cell. it returns three values
potential_vars, start_cell, is_optimal
"""

def generate_delta_matrix(cost_matrix):
    m = len(cost_matrix)  
    n = len(cost_matrix[0])

    # Initialize potential variables
    potential_vars = {'u1':0}
    potential_vars.update({f'u{i + 1}': None for i in range(1,m)})
    potential_vars.update({f'v{j + 1}': None for j in range(n)})

    # Extract equations from non-zero cells
    equations = [(i, j, cost_matrix[i][j]) for i in range(m) for j in range(n) if cost_matrix[i][j] != 0]

    # Update potential variables using equations
    while any(val is None for val in potential_vars.values()):  #crazy but without this some will be none except if we have (n+m-1) equations
        for i, j, c_ij in equations:
            if potential_vars[f'u{i + 1}'] != None:
                potential_vars[f'v{j + 1}'] = c_ij - potential_vars[f'u{i + 1}']
            elif potential_vars[f'v{j + 1}'] != None:
                potential_vars[f'u{i + 1}'] = c_ij - potential_vars[f'v{j + 1}']

    is_optimal = True
    cell_pts = []  # [(index, index, value), ...]
    
    # Find cell with highest potential for cycle starting point
    for i in range(m):
        for j in range(n):
            if cost_matrix[i][j] == 0:
                delta = cost_matrix[i][j] - (potential_vars[f'u{i + 1}'] + potential_vars[f'v{j + 1}'])
                cell_pts.append((i, j, delta))
                if delta < 0:
                    is_optimal = False

    # Sort cell points based on the third value in the tuple (delta)
    sorted_cell_pts = sorted(cell_pts, key=lambda x: x[2])

    
    return potential_vars, sorted_cell_pts, is_optimal

# # Example cost matrix
# cost_matrix = [
#     [3, 4, 0, 0],
#     [0, 2, 2, 0],
#     [0, 0, 3, 6]
# ]
# # cost_matrix = [
# #     [3, 0, 4, 0],
# #     [0, 0, 1, 3],
# #     [0, 6, 0, 3]
# # ]
# potential_vars, start_cell, is_optimal = generate_delta_matrix(cost_matrix)

# print("Cost Matrix:")
# for row in cost_matrix:
#     print(row)

# print("\nPotential Variables:")
# print(potential_vars)

# print("\nStart Cell for Cycle:")
# print(start_cell)

# print("\nIs Optimal:", is_optimal)
