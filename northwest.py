# THE NORTHWEST ALGO

# m = number of product constraints
# n = number of demand constrains
# demand = e.g =>  [3, 6, 5, 6]
# products = e.g => [7, 4, 9]
# transportation_costs = e.g => 
# [
# [3, 4, 0, 0], 
# [0, 2, 2, 0], 
# [0, 0, 3, 6]
# ]     THOUGH THIS IS NOT A NECESSARY ARGUMENT, YOU CAN PASS

def northwest_algo(demand, products, transportation_costs=[]):
    m = len(products)
    n = len(demand)

    # INITIALIZE empty transportation matrix
    transportation_matrix = [[0]*n for _ in range(m)]
    # # or initialize your own
    # transportation_matrix = transportation_costs

    # Initialize indices for product and demand constraints
    i = 0
    j = 0

    # Execute Northwest Corner Rule algorithm
    while i < m and j < n:
        if demand[j] < products[i]:     #basically asking if min(demand[j],product[i]) is demand[j] then we input this value and decrement product[i] by this value also shift to next demand[j]
            transportation_matrix[i][j] = demand[j]
            products[i] -= demand[j]
            demand[j] = 0
            j += 1
        elif demand[j] > products[i]:   #just the opposite case
            transportation_matrix[i][j] = products[i]
            demand[j] -= products[i]
            products[i] = 0
            i += 1
        else:
            transportation_matrix[i][j] = demand[j]
            demand[j] = 0
            products[i] = 0
            i += 1
            j += 1

    return transportation_matrix
