def modify_matrix(cost_matrix,cycle):
    # get theta from cycle evals
    def get_theta(cost_matrix,cycle):
        spot = []
        for i, val in enumerate(cycle):
            if i % 2 != 0:
                spot.append(cost_matrix[val[0]][val[1]])
        print(spot)
        return min(spot)

    # update the matrix at evals + - + -
    def update_cost_matrix(cost_matrix, cycle, theta):
        for i, pt in enumerate(cycle):
            if i % 2 == 0:
                x1, y1 = pt
                cost_matrix[x1][y1] += theta
            else:
                x2, y2 = pt
                cost_matrix[x2][y2] -= theta
        return cost_matrix


    # IMPL -> 
    theta = get_theta(cost_matrix,cycle); print('theta: ', theta)
    adjusted_matrix = update_cost_matrix(cost_matrix,cycle,theta)
    
    return adjusted_matrix
