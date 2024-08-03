from func import read_matrix, read_data


class Vehicle:
    data = read_data()
    dom = read_matrix()
    dtype = [5.5, 12]  # demand type

    def __init__(
        self, cost_per_km: float | int, capacity: int, name: str = "Vehicle"
    ) -> None:
        self.name = name
        self.cost_per_km = cost_per_km
        self.capacity = capacity
        self.route = []
        self.loads = 0
        self.is_feasible = True
        self.total_cost = 0

    def evaluate_solution(self, route: list) -> None:
        """
        Validate the solution
        :param route: list of nodes
        :return: None
        """
        # reset result
        self.reset_result()
        # check route length
        self.route = route
        total_distance = 0
        for n, _ in enumerate(route):
            if n == len(route) - 1:
                break
            a, b = route[n], route[n + 1]
            d = self.dom[a][b]
            total_distance += d
        # calculate total cost
        self.total_cost = round(total_distance * self.cost_per_km)
        # calculate loads based on demand
        self.loads = self.calculate_loads()
        # check if the loads exceed the capacity
        if self.loads > self.capacity:
            self.is_feasible = False

    def calculate_loads(self) -> int:
        """
        Calculate the loads based on the demand
        :return: loads
        """
        demands = self.data[["Demand_1", "Demand_2"]].to_numpy()
        loads = 0
        nodes = self.route[1:-1]
        for n in nodes:
            loads += sum(
                [demands[n][i] * self.dtype[i] for i in range(len(self.dtype))]
            )
        return int(loads)

    def reset_result(self):
        self.loads = 0
        self.is_feasible = True
        self.total_cost = 0

    def __str__(self) -> str:
        return f"Vehicle(name='{self.name}',total_cost='Rp{self.total_cost:,.0f}',total_loads={self.loads:,d},route_length={len(self.route)})"
