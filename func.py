import pandas as pd
import numpy as np
import math


def read_data():
    data = pd.read_excel("data.xlsx", sheet_name="distribution")
    data = data.set_index("ID")
    return data


def read_matrix():
    data = pd.read_excel("data.xlsx", sheet_name="matrix", header=None)
    data = data.fillna(0)
    data = data.to_numpy()
    return data


def generate_solution(n):
    if isinstance(n, int):
        p = np.array(range(n)) + 1
        np.random.shuffle(p)
        return p
    else:
        raise ValueError("n harus nilai bulat")


def cluster_by_vehicle(k1, k2, route, p=0.5):
    # declare initial solution
    solution = {
        "vehicle": [],
        "total_cost": 0,
        "loads_balance": math.inf,  # loads delta
    }
    # run the clustering
    route = route[1:-1]
    i = math.floor(len(route) * p)
    r1 = route[0:i]
    r2 = route[i:]
    k1.validate_solution([0, *r1, 0])
    k2.validate_solution([0, *r2, 0])
    solution["vehicle"] = [k1, k2]
    solution["total_cost"] = k1.total_cost + k2.total_cost
    solution["loads_balance"] = abs(k1.loads - k2.loads)
    return solution
