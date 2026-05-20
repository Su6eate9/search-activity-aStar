import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from typing import List, Tuple, Optional, Set


class GridVisualizer:
    def __init__(self, width: int, height: int, 
                 obstacles: Optional[Set[Tuple[int, int]]] = None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles is not None else set()
    
    def visualize_grid_and_path(self, path: List[Tuple[int, int]],
                               start: Tuple[int, int],
                               goal: Tuple[int, int],
                               title: str = "A* Grid Pathfinding",
                               show_grid: bool = True,
                               figsize: Tuple[int, int] = (10, 10)) -> None:
        fig, ax = plt.subplots(figsize=figsize)
        
        if show_grid:
            ax.set_xlim(-0.5, self.width - 0.5)
            ax.set_ylim(self.height - 0.5, -0.5)
            ax.set_xticks(np.arange(-0.5, self.width, 1), minor=True)
            ax.set_yticks(np.arange(-0.5, self.height, 1), minor=True)
            ax.grid(True, which='minor', color='gray', linestyle='-', linewidth=0.5, alpha=0.3)
        
        for obs in self.obstacles:
            y, x = obs
            rect = patches.Rectangle((x - 0.5, y - 0.5), 1, 1, 
                                     linewidth=2, edgecolor='black', 
                                     facecolor='black', alpha=0.7)
            ax.add_patch(rect)
        
        if path and len(path) > 1:
            path_array = np.array(path)
            ax.plot(path_array[:, 1], path_array[:, 0], 
                   color='blue', linewidth=2, marker='o', 
                   markersize=4, label='Caminho', zorder=3)
            
            for y, x in path:
                if (y, x) != start and (y, x) != goal:
                    rect = patches.Rectangle((x - 0.5, y - 0.5), 1, 1,
                                            linewidth=1, edgecolor='blue',
                                            facecolor='lightblue', alpha=0.5)
                    ax.add_patch(rect)
        
        start_y, start_x = start
        rect = patches.Rectangle((start_x - 0.5, start_y - 0.5), 1, 1,
                                linewidth=2, edgecolor='green',
                                facecolor='lightgreen', alpha=0.8)
        ax.add_patch(rect)
        ax.plot(start_x, start_y, marker='s', color='green', 
               markersize=10, label='Inicio', zorder=4)
        
        goal_y, goal_x = goal
        rect = patches.Rectangle((goal_x - 0.5, goal_y - 0.5), 1, 1,
                                linewidth=2, edgecolor='red',
                                facecolor='lightcoral', alpha=0.8)
        ax.add_patch(rect)
        ax.plot(goal_x, goal_y, marker='*', color='red',
               markersize=15, label='Objetivo', zorder=4)
        
        ax.set_xlabel('X', fontsize=12)
        ax.set_ylabel('Y', fontsize=12)
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(loc='upper right', fontsize=10)
        ax.set_aspect('equal')
        
        plt.tight_layout()
        plt.show()
    
    def visualize_graph_network(self, graph: nx.Graph,
                               path: Optional[List[Tuple[int, int]]] = None,
                               title: str = "Grid Graph",
                               figsize: Tuple[int, int] = (12, 10)) -> None:
        fig, ax = plt.subplots(figsize=figsize)
        
        pos = {node: (node[1], -node[0]) for node in graph.nodes()}
        
        nx.draw_networkx_nodes(graph, pos, node_color='lightblue',
                              node_size=300, ax=ax)
        
        if path:
            nx.draw_networkx_nodes(graph, pos, nodelist=path,
                                  node_color='yellow', node_size=500,
                                  ax=ax, label='Caminho')
        
        nx.draw_networkx_edges(graph, pos, width=0.5, alpha=0.5, ax=ax)
        nx.draw_networkx_labels(graph, pos, font_size=8, ax=ax)
        
        ax.set_title(title, fontsize=14, fontweight='bold')
        ax.legend(fontsize=10)
        plt.axis('off')
        plt.tight_layout()
        plt.show()
    
    def save_figure(self, path: List[Tuple[int, int]],
                   start: Tuple[int, int],
                   goal: Tuple[int, int],
                   filename: str = "grid_pathfinding.png") -> None:
        fig, ax = plt.subplots(figsize=(10, 10))
        
        ax.set_xlim(-0.5, self.width - 0.5)
        ax.set_ylim(self.height - 0.5, -0.5)
        ax.grid(True, which='major', color='gray', linestyle='-', 
               linewidth=0.5, alpha=0.3)
        
        for obs in self.obstacles:
            y, x = obs
            rect = patches.Rectangle((x - 0.5, y - 0.5), 1, 1,
                                    linewidth=2, edgecolor='black',
                                    facecolor='black', alpha=0.7)
            ax.add_patch(rect)
        
        if path and len(path) > 1:
            path_array = np.array(path)
            ax.plot(path_array[:, 1], path_array[:, 0],
                   color='blue', linewidth=2, marker='o',
                   markersize=5, label='Caminho')
        
        start_y, start_x = start
        ax.plot(start_x, start_y, marker='s', color='green',
               markersize=12, label='Inicio')
        
        goal_y, goal_x = goal
        ax.plot(goal_x, goal_y, marker='*', color='red',
               markersize=15, label='Objetivo')
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('A* Pathfinding Result')
        ax.legend()
        ax.set_aspect('equal')
        
        plt.savefig(filename, dpi=150, bbox_inches='tight')
        print(f"Figure saved as {filename}")
        plt.close()
