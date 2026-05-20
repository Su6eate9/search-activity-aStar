import networkx as nx
from typing import Tuple, Set, Dict
import numpy as np


class GridGraphBuilder:
    
    def __init__(self, width: int, height: int, obstacles: Set[Tuple[int, int]] = None):
        self.width = width
        self.height = height
        self.obstacles = obstacles or set()
        self.graph = nx.Graph()
        
    def build(self) -> nx.Graph:
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) not in self.obstacles:
                    self.graph.add_node((y, x))
        
        for y in range(self.height):
            for x in range(self.width):
                if (y, x) in self.obstacles:
                    continue
                
                for ny, nx_c in [(y, x + 1), (y + 1, x), (y, x - 1), (y - 1, x)]:
                    if (0 <= ny < self.height and 
                        0 <= nx_c < self.width and 
                        (ny, nx_c) not in self.obstacles):
                        
                        weight = np.sqrt((ny - y)**2 + (nx_c - x)**2)
                        if not self.graph.has_edge((y, x), (ny, nx_c)):
                            self.graph.add_edge((y, x), (ny, nx_c), weight=weight)
        
        return self.graph
    
    def get_graph(self) -> nx.Graph:
        return self.graph
    
    def get_graph_info(self) -> Dict:
        return {
            'num_nodes': self.graph.number_of_nodes(),
            'num_edges': self.graph.number_of_edges(),
            'grid_dimensions': (self.height, self.width),
            'num_obstacles': len(self.obstacles),
            'is_connected': nx.is_connected(self.graph) if self.graph.number_of_nodes() > 0 else False
        }
    
    @staticmethod
    def create_sample_grid(width: int = 10, height: int = 10) -> 'GridGraphBuilder':
        obstacles = {
            (2, 3), (2, 4), (2, 5),
            (3, 5), (4, 5), (5, 5), (5, 4), (5, 3),
            (6, 3), (7, 3), (7, 4), (7, 5), (7, 6),
        }
        return GridGraphBuilder(width, height, obstacles)
