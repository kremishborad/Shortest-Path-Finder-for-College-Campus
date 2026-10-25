
import heapq

# College campus map represented as a graph
campus = {
    "Main Gate": {
        "Library": 200,
        "Canteen": 150
    },
    "Library": {
        "Main Gate": 200,
        "Admin Block": 100,
        "Computer Lab": 120
    },
    "Canteen": {
        "Main Gate": 150,
        "Computer Lab": 180,
        "Parking": 100
    },
    "Admin Block": {
        "Library": 100,
        "Computer Lab": 80
    },
    "Computer Lab": {
        "Library": 120,
        "Canteen": 180,
        "Admin Block": 80,
        "Parking": 140
    },
    "Parking": {
        "Canteen": 100,
        "Computer Lab": 140
    }
}


def dijkstra(graph, start, destination):
    # Store distances and previous locations
    distances = {place: float("inf") for place in graph}
    previous = {place: None for place in graph}

    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_place = heapq.heappop(
            priority_queue
        )

        # Skip outdated queue entries
        if current_distance > distances[current_place]:
            continue

        # Destination reached
        if current_place == destination:
            break

        # Check all neighboring locations
        for neighbor, distance in graph[current_place].items():
            new_distance = current_distance + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_place

                heapq.heappush(
                    priority_queue,
                    (new_distance, neighbor)
                )

    # Check whether a path exists
    if distances[destination] == float("inf"):
        return None, float("inf")

    # Reconstruct the shortest path
    path = []
    current = destination

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()
    return path, distances[destination]


def display_locations():
    print("\nAvailable Campus Locations:")
    for place in campus:
        print("-", place)


def main():
    print("=" * 45)
    print("   COLLEGE CAMPUS SHORTEST PATH FINDER")
    print("        Using Dijkstra's Algorithm")
    print("=" * 45)

    display_locations()

    start = input("\nEnter starting location: ").strip()
    destination = input("Enter destination: ").strip()

    # Validate input
    if start not in campus or destination not in campus:
        print("\nInvalid location! Please select a listed location.")
        return

    if start == destination:
        print("\nYou are already at the destination!")
        print("Distance: 0 meters")
        return

    path, distance = dijkstra(campus, start, destination)

    if path is None:
        print("\nNo path exists between these locations.")
    else:
        print("\nShortest Path:")
        print(" -> ".join(path))
        print(f"Total Distance: {distance} meters")
        print(f"Number of locations in path: {len(path)}")


if __name__ == "__main__":
    main()
