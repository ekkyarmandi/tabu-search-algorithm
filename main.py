from func import cluster_by_vehicle, remove_zero
from algo import tabu_search, nearest_neighbourhood
from vehicle import Vehicle
import pandas as pd
import time
import os


def main():
    s1 = time.time()
    s2 = time.time()

    # generate initial route nearest neightbourhood
    initial_route = nearest_neighbourhood()

    # define vehicles
    k1 = Vehicle(name="Pick Up", cost_per_km=1111, capacity=1500)
    k2 = Vehicle(name="Single Truck", cost_per_km=850, capacity=2500)

    # cluster the route into two and validate solution
    solution = cluster_by_vehicle(k1, k2, initial_route)
    output = construct_output(
        iteration=0,
        route=initial_route,
        solution=solution,
        time_leapsed=time.time() - s1,
    )
    save(output, "result_nn.xlsx")

    # fix the previous solution using tabu search
    max_it = 10000
    new_solution, new_route = tabu_search(
        iteration=max_it, route=initial_route, solution=solution
    )
    output = construct_output(
        iteration=max_it,
        route=new_route,
        solution=new_solution,
        time_leapsed=time.time() - s2,
    )

    save(output, "result_ts.xlsx")

    # print the solution
    # print("----")
    # print(new_solution["vehicle"][0])
    # print("----")
    # print(new_solution["vehicle"][1])
    # print("----")
    # print("total_cost: Rp{:,.0f}".format(new_solution["total_cost"]))
    # print("----")


def join_str(route: list) -> str:
    route = list(map(str, route))
    return "-".join(route)


def construct_output(route, solution, time_leapsed, iteration):
    v1, v2 = solution["vehicle"]
    return {
        "iteration": iteration,
        "cost": solution["total_cost"],
        "solution": join_str(remove_zero(route)),
        "total_distance": sum([k.total_distance for k in [v1, v2]]),
        "v1_route": join_str(v1.route),
        "v1_loads": v1.loads,
        "v1_total_distance": v1.total_distance,
        "v2_route": join_str(v2.route),
        "v2_loads": v2.loads,
        "v2_total_distance": v2.total_distance,
        "time_leapsed": time_leapsed,
    }


def save(output, filename):
    if not os.path.exists(filename):
        df = pd.DataFrame(output, index=[0])
    else:
        df = pd.read_excel(filename)
        new_row = pd.DataFrame(output, index=[0])
        df = pd.concat([df, new_row], ignore_index=True)
    df.to_excel(filename, index=False)


def run():
    repeat = 10
    for _ in range(repeat):
        main()


if __name__ == "__main__":
    # main()
    run()
