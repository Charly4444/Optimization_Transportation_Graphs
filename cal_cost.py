"""
calculate the total cost
"""
def cal_cost(transportation_matrix,unit_cost_matrix):
    total_cost = 0
    for i in range(len(transportation_matrix)):
        for j in range(len(transportation_matrix[0])):
            total_cost += transportation_matrix[i][j] * unit_cost_matrix[i][j]
    return total_cost
