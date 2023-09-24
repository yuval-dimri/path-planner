import time
from src.lib.map_visualizer import MapVisualizer
from src.lib.path_planner import PathPlanner


def generate_random_map():
    rows, cols = 50, 50  # Adjust the map size as needed
    random_map = MapVisualizer.generate_random_map(rows, cols, num_chunks=4, max_chunk_size=(
        20, 20), min_chunk_size=(5, 5), corridor_width=4, min_chunk_spacing=20)
    return random_map


if __name__ == "__main__":
    random_map = generate_random_map()
    map_visualizer = MapVisualizer(random_map)
    # map_visualizer.color_point((0, 0), 2)
    # map_visualizer.map_array[200, 200] = 200
    print(map_visualizer.map_array)

    start_position = (1, 1)  # Replace with your desired start position
    # Replace with your desired goal position
    goal_position = (random_map.shape[0] - 1, random_map.shape[1] - 1)

# # Color the start and goal positions
#     # Use a different color (e.g., 2) for the start point
#     # Use a different color (e.g., 3) for the goal point
    map_visualizer.color_point(goal_position)
    # map_visualizer.visualize_map()
# # Plan and display the path
    planner = PathPlanner(random_map, start_position, goal_position)
    path = planner.plan_path()
    for point in path:
        map_visualizer.color_point(point)
    print("Planned Path:", path)

# # Display the map with colored points and the planned path
    map_visualizer.visualize_map()
