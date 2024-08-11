import numpy as np
from func import cluster_by_vehicle, read_matrix, remove_zero


def nearest_neighbourhood():
    """
    Nearest Neighbourhood algorithm for calculating the initial route
    :param: m -> distance of matrix
    :param: n -> number of nodes
    :return: r -> collection of nodes
    """
    dom = read_matrix()
    r = [0]
    n = len(dom)
    for _ in range(n):
        i = r[-1]
        d = dom[i]
        for x in r:
            d[x] = 0
        min_d = min(filter(lambda x: x != 0, d))
        b = d.tolist().index(min_d)
        r.append(b)
        if len(r) == n:
            r.append(0)
            break

    return r


def tabu_search(iteration, route, solution, print_result=True) -> dict:
    """
    Tabu Search algorithm for solving the VRP
    :param: iteration -> iteration of the algorithm
    :param: route -> list of nodes
    :param: solution -> previous solution
    :return: solution -> fixed solution
    """

    def swap(route):
        i, j = random_index(len(route))
        new_route = route.copy()
        new_route[i], new_route[j] = new_route[j], new_route[i]
        return new_route

    def random_index(route_length):
        i, j = np.random.randint(1, route_length, size=2)
        while i == j:
            i, j = np.random.randint(1, route_length, size=2)
        return i, j

    # define tabu list variable and TS parameters
    route = remove_zero(route)
    tabu_list = [route]
    # fix the route
    k1 = solution["vehicle"][0]
    k2 = solution["vehicle"][1]
    for _ in range(iteration):
        swapped_route = swap(route)
        v1, v2 = solution["vehicle"]
        total_cost = solution["total_cost"]
        if print_result:
            print(_, f"Rp{total_cost:,.0f}", v1, v2)
        if swapped_route not in tabu_list:
            tabu_list.append(swapped_route)
            # validate solution
            new_solution = cluster_by_vehicle(k1, k2, swapped_route)
            if new_solution["total_cost"] < solution["total_cost"]:
                solution = new_solution
                route = swapped_route
    return solution, remove_zero(route)


if __name__ == "__main__":
    solution = nearest_neighbourhood()
    print(solution)
