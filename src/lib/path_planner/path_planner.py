import numpy as np
import heapq


class PathPlanner:
    def __init__(self, occupancy_grid, start, goal):
        self.grid = occupancy_grid
        self.start = start
        self.goal = goal

    class Node:
        def __init__(self, y, x, parent=None):
            self.x = x
            self.y = y
            self.parent = parent
            self.g = 0  # Cost from start node to current node
            self.h = 0  # Heuristic (estimated cost from current node to goal)
            self.f = 0  # Total cost (g + h)

        def __lt__(self, other):
            return self.f < other.f

    def plan_path(self):
        rows, cols = self.grid.shape
        open_set = []
        closed_set = set()

        start_node = self.Node(*self.start)
        goal_node = self.Node(*self.goal)

        heapq.heappush(open_set, (start_node.f, start_node))

        while open_set:
            _, current_node = heapq.heappop(open_set)

            if current_node.x == goal_node.x and current_node.y == goal_node.y:
                return self.reconstruct_path(current_node)

            closed_set.add((current_node.x, current_node.y))

            for neighbor in self.get_neighbors(current_node, rows, cols):
                if neighbor in closed_set or self.grid[neighbor.x, neighbor.y]:
                    continue

                tentative_g = current_node.g + 1
                if tentative_g < neighbor.g or neighbor not in open_set:
                    neighbor.g = tentative_g
                    neighbor.h = self.manhattan_distance(neighbor, goal_node)
                    neighbor.f = neighbor.g + neighbor.h
                    neighbor.parent = current_node

                    if neighbor not in open_set:
                        heapq.heappush(open_set, (neighbor.f, neighbor))

        return None  # No path found

    def manhattan_distance(self, node1, node2):
        return abs(node1.x - node2.x) + abs(node1.y - node2.y)

    def get_neighbors(self, node, rows, cols):
        neighbors = []
        if node.x > 0:
            neighbors.append(self.Node(node.x - 1, node.y, node))
        if node.x < rows - 1:
            neighbors.append(self.Node(node.x + 1, node.y, node))
        if node.y > 0:
            neighbors.append(self.Node(node.x, node.y - 1, node))
        if node.y < cols - 1:
            neighbors.append(self.Node(node.x, node.y + 1, node))
        return neighbors

    def reconstruct_path(self, node):
        path = []
        while node is not None:
            path.append((node.x, node.y))
            node = node.parent
        return list(reversed(path))


if __name__ == "__main__":
    grid = np.array([[False, False, False, True, False],
                     [True, True, False, True, False],
                     [False, False, False, False, False],
                     [False, True, True, True, False],
                     [False, False, False, False, False]])

    start = (0, 0)
    goal = (4, 4)

    astar = PathPlanner(grid, start, goal)
    path = astar.plan_path()
    if path:
        print("Path found:", path)
    else:
        print("No path found")
