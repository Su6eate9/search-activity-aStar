import networkx as nx
import heapq
from typing import Tuple, List, Callable, Optional, Dict
import math


class AStarSolver:
    
    def __init__(self, graph: nx.Graph, heuristic: Optional[Callable] = None):
        self.graph = graph
        self.heuristic = heuristic or self._euclidean
        self.nodes_expanded = 0
        self.nodes_evaluated = 0
        
    @staticmethod
    def _euclidean(n1: Tuple[int, int], n2: Tuple[int, int]) -> float:
        return math.sqrt((n1[0] - n2[0])**2 + (n1[1] - n2[1])**2)
    
    @staticmethod
    def _manhattan(n1: Tuple[int, int], n2: Tuple[int, int]) -> float:
        return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])
    
    def solve(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], Dict]:
        self.nodes_expanded = 0
        self.nodes_evaluated = 0
        
        if start not in self.graph or goal not in self.graph:
            return None, {'success': False, 'error': 'Invalid nodes', 'path_cost': float('inf')}
        
        if start == goal:
            return [start], {'success': True, 'nodes_expanded': 0, 'nodes_evaluated': 1, 
                            'path_length': 1, 'path_cost': 0.0}
        
        open_set = []
        open_dict = {start}
        closed_set = set()
        g_score = {start: 0.0}
        f_score = {start: self.heuristic(start, goal)}
        came_from = {}
        
        heapq.heappush(open_set, (f_score[start], id(start), start))
        
        while open_set:
            _, _, current = heapq.heappop(open_set)
            
            if current in open_dict:
                open_dict.remove(current)
            
            if current == goal:
                path = self._reconstruct_path(came_from, current)
                return path, {
                    'success': True,
                    'nodes_expanded': self.nodes_expanded,
                    'nodes_evaluated': self.nodes_evaluated,
                    'path_length': len(path),
                    'path_cost': g_score[goal]
                }
            
            closed_set.add(current)
            self.nodes_expanded += 1
            
            for neighbor in self.graph.neighbors(current):
                if neighbor in closed_set:
                    continue
                
                self.nodes_evaluated += 1
                weight = self.graph[current][neighbor].get('weight', 1.0)
                tentative_g = g_score[current] + weight
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(neighbor, goal)
                    
                    if neighbor not in open_dict:
                        heapq.heappush(open_set, (f_score[neighbor], id(neighbor), neighbor))
                        open_dict.add(neighbor)
        
        return None, {
            'success': False,
            'error': 'No path found',
            'nodes_expanded': self.nodes_expanded,
            'nodes_evaluated': self.nodes_evaluated,
            'path_cost': float('inf')
        }
    
    @staticmethod
    def _reconstruct_path(came_from: Dict, current: Tuple[int, int]) -> List:
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path
    
    def solve_with_networkx(self, start: Tuple[int, int], goal: Tuple[int, int]) -> Tuple[Optional[List], Dict]:
        try:
            path = nx.astar_path(self.graph, start, goal, 
                                heuristic=self.heuristic, weight='weight')
            cost = nx.astar_path_length(self.graph, start, goal,
                                       heuristic=self.heuristic, weight='weight')
            return path, {
                'success': True,
                'path_length': len(path),
                'path_cost': cost,
                'library': 'NetworkX'
            }
        except (nx.NetworkXNoPath, nx.NodeNotFound):
            return None, {'success': False, 'error': 'No path or invalid nodes', 'library': 'NetworkX'}
