
import heapq
import math

# 1. Define the 20 healthcare facilities
facilities = {
    "A": "Queen Elizabeth Central Hospital",
    "B": "Bangwe Health Centre",
    "C": "Limbe Health Centre",
    "D": "Ndirande",
    "E": "Chilomoni",
    "F": "Zingwangwa",
    "G": "Chitimba",
    "H": "South Lunzu",
    "I": "Mbatani",
    "J": "Kadidi",
    "K": "Makhetha",
    "L": "Malabada",
    "M": "Blantyre Adventist",
    "N": "Mwaiwathu",
    "O": "Beit Cure International Hospital",
    "P": "Shifa Hospital",
    "Q": "LMJ",
    "R": "Bean Medical Centre",
    "S": "Masm Medical Clinic",
    "T": "Atlas Medical Centre"
}

# 2. Create an empty adjacency list
graph = {node: [] for node in facilities}

# 3. Define the weighted edges
edges = [
    ("A", "D", 4),
    ("A", "E", 6),
    ("A", "M", 3),
    ("A", "N", 4),
    ("A", "O", 2),
    ("A", "P", 3),
    ("A", "S", 5),
    ("A", "T", 4),

    ("B", "C", 7),
    ("B", "D", 3),
    ("B", "R", 4),

    ("C", "G", 5),
    ("C", "Q", 2),

    ("D", "E", 4),
    ("D", "R", 3),

    ("E", "F", 5),

    ("F", "G", 4),
    ("F", "H", 6),

    ("G", "H", 5),

    ("H", "I", 3),
    ("H", "J", 4),

    ("I", "J", 2),
    ("I", "K", 5),

    ("J", "K", 3),
    ("J", "L", 4),

    ("K", "L", 2),

    ("M", "N", 2),
    ("N", "S", 3),
    ("S", "T", 2),
    ("S", "P", 7)
]

# 4. Build the undirected weighted graph
for u, v, weight in edges:
    graph[u].append((v, weight))
    graph[v].append((u, weight))


# 5. Implement Dijkstra's algorithm
def dijkstra(graph, start):

    distance = {node: math.inf for node in graph}
    predecessor = {node: None for node in graph}

    distance[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:

        current_distance, current_node = heapq.heappop(
            priority_queue
        )

        if current_distance > distance[current_node]:
            continue

        for neighbour, weight in graph[current_node]:

            new_distance = current_distance + weight

            if new_distance < distance[neighbour]:

                distance[neighbour] = new_distance
                predecessor[neighbour] = current_node

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbour)
                )

    return distance, predecessor


# 6. Reconstruct the shortest route
def get_path(predecessor, start, destination):

    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = predecessor[current]

    path.reverse()

    if not path or path[0] != start:
        return []

    return path


# 7. Get user input
print("HOSPITAL REFERRAL NETWORK")
print("-------------------------")

start = input("Enter starting facility (A-T): ").upper()
destination = input("Enter destination facility (A-T): ").upper()

if start not in graph or destination not in graph:
    print("Invalid facility selected.")

else:
    # Run Dijkstra
    distances, predecessors = dijkstra(graph, start)

    # Display shortest distances
    print("\nSHORTEST DISTANCES")
    print("------------------")

    for node in facilities:
        print(
            node, "-", facilities[node],
            "| Distance:", distances[node],
            "| Predecessor:", predecessors[node]
        )

    # Display selected route
    path = get_path(predecessors, start, destination)

    print("\nSHORTEST REFERRAL ROUTE")
    print("----------------------")

    if path:
        print(" -> ".join(path))

        print("\nFacilities visited:")
        for node in path:
            print(node, "-", facilities[node])

        print("\nTotal distance:",
              distances[destination], "km")
    else:
        print("No route exists between these facilities.")
