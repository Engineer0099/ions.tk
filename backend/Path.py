import heapq


class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, name, x, y):
        self.nodes[name] = {"pos": (x, y), "edges": {}}
    
    def add_edge(self, node1, node2, cost=1):
        self.nodes[node1]["edges"][node2] = cost
        self.nodes[node2]["edges"][node1] = cost  # Bi-directional


# Initialize graph
building_graph = Graph()

# Add key nodes (example: walkable points in a floor)
building_graph.add_node("Entrance", 0, 0)
building_graph.add_node("Hallway1", 5, 0)
building_graph.add_node("Elevator", 10, 0)
building_graph.add_node("Stairs", 10, 5)
building_graph.add_node("Room1", 15, 0)
building_graph.add_node("Room2", 15, 5)

# Define connections between nodes
building_graph.add_edge("Entrance", "Hallway1", 5)
building_graph.add_edge("Hallway1", "Elevator", 5)
building_graph.add_edge("Hallway1", "Stairs", 6)
building_graph.add_edge("Elevator", "Room1", 5)
building_graph.add_edge("Stairs", "Room2", 5)


def a_star(graph, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))  # (cost, node)
    came_from = {}
    g_cost = {node: float('inf') for node in graph.nodes}
    g_cost[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor, cost in graph.nodes[current]["edges"].items():
            new_cost = g_cost[current] + cost
            if new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                priority = new_cost
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return None  # No path found


# Example pathfinding
start_node = "Entrance"
goal_node = "Room1"
path = a_star(building_graph, start_node, goal_node)
print("Optimal Path:", path)


def navigate_floors(graph, start, goal, start_floor, goal_floor):
    if start_floor == goal_floor:
        return a_star(graph, start, goal)

    # First move to the elevator or stairs
    elevator_node = "Elevator"
    stairs_node = "Stairs"
    
    print("Floor change required!")
    choice = input("Choose movement method (1: Elevator, 2: Stairs): ")

    if choice == "2":
        vertical_path = a_star(graph, start, stairs_node) + ["Go Upstairs"] + a_star(graph, stairs_node, goal)
    else:
        vertical_path = a_star(graph, start, elevator_node) + ["Use Elevator"] + a_star(graph, elevator_node, goal)

    return vertical_path


# Example: Moving between floors
final_path = navigate_floors(building_graph, "Entrance", "Room2", 1, 2)
print("Final Navigation Path:", final_path)