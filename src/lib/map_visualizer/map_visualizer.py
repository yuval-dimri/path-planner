import numpy as np
import matplotlib.pyplot as plt


class MapVisualizer:
    def __init__(self, map_array):
        self.map_array = map_array
        # Numeric values corresponding to colors (0: white, 1: black, 2: red)
        # self.colors = [0, 1, 2]

    def visualize_map(self):
        # color_map = np.vectorize(lambda x: self.colors[x])(self.map_array)
        plt.imshow(self.map_array, cmap='viridis', interpolation='nearest',
                   origin='lower')  # Use 'viridis' colormap for numeric data
        plt.axis('off')
        plt.show()

    def color_point(self, point):
        plt.annotate('X', xy=point, color='red',
                     fontsize=16, ha='center', va='center')

    @staticmethod
    def generate_random_map(rows, cols, num_chunks=5, max_chunk_size=(50, 50), min_chunk_size=(10, 10), corridor_width=3, min_chunk_spacing=20):
        """
        Generate a structured random indoor-like map with random-sized and spaced-apart chunks.

        Parameters:
            rows (int): Number of rows in the map.
            cols (int): Number of columns in the map.
            num_chunks (int): Number of structured chunks in the map.
            max_chunk_size (tuple): Maximum size (rows, cols) of each chunk.
            min_chunk_size (tuple): Minimum size (rows, cols) of each chunk.
            corridor_width (int): Width of corridors between chunks and walls.
            min_chunk_spacing (int): Minimum spacing between chunks.

        Returns:
            np.ndarray: A randomly generated indoor-like map (0 for empty, 1 for wall).
        """
        map_array = np.zeros((rows, cols), dtype=int)

        for _ in range(num_chunks):
            chunk_height = np.random.randint(
                min_chunk_size[0], max_chunk_size[0])
            chunk_width = np.random.randint(
                min_chunk_size[1], max_chunk_size[1])

            while True:
                chunk_row = np.random.randint(
                    corridor_width, rows - chunk_height - corridor_width)
                chunk_col = np.random.randint(
                    corridor_width, cols - chunk_width - corridor_width)
                if not np.any(map_array[chunk_row:chunk_row + chunk_height + 2 * corridor_width,
                                        chunk_col:chunk_col + chunk_width + 2 * corridor_width]):
                    break

            map_array[chunk_row:chunk_row + chunk_height,
                      chunk_col:chunk_col + chunk_width] = 1

        # Create outer walls
        map_array[:corridor_width, :] = 0
        map_array[-corridor_width:, :] = 0
        map_array[:, :corridor_width] = 0
        map_array[:, -corridor_width:] = 0

        return map_array
