import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import GridGraphBuilder, AStarSolver, GridVisualizer
from src.a_star_solver import AStarSolver as AS


def main():
    print("=" * 70)
    print("ALGORITMO A* - BUSCA EM GRID COM OBSTACULOS")
    print("=" * 70)
    print()
    
    print("[1] Criando grid...")
    builder = GridGraphBuilder.create_sample_grid(width=10, height=10)
    graph = builder.build()
    
    info = builder.get_graph_info()
    print(f"  Dimensoes: {info['grid_dimensions']}")
    print(f"  Nos: {info['num_nodes']}")
    print(f"  Arestas: {info['num_edges']}")
    print(f"  Obstaculos: {info['num_obstacles']}")
    print(f"  Conectado: {info['is_connected']}")
    print()
    
    print("[2] Definindo pontos...")
    start = (0, 0)
    goal = (9, 9)
    print(f"  Inicio: {start}")
    print(f"  Objetivo: {goal}")
    print()
    
    print("[3] Executando A* (Euclidiana)...")
    solver = AStarSolver(graph)
    path, stats = solver.solve(start, goal)
    
    if stats['success']:
        print(f"  [OK] Caminho encontrado!")
        print(f"  Comprimento: {stats['path_length']}")
        print(f"  Custo: {stats['path_cost']:.4f}")
        print(f"  Expandidos: {stats['nodes_expanded']}")
        print(f"  Avaliados: {stats['nodes_evaluated']}")
    else:
        print(f"  [ERRO] {stats['error']}")
    print()
    
    print("[4] Executando A* (Manhattan)...")
    solver_manhattan = AStarSolver(graph, heuristic=AS._manhattan)
    path_manhattan, stats_manhattan = solver_manhattan.solve(start, goal)
    
    if stats_manhattan['success']:
        print(f"  [OK] Caminho encontrado!")
        print(f"  Comprimento: {stats_manhattan['path_length']}")
        print(f"  Custo: {stats_manhattan['path_cost']:.4f}")
        print(f"  Expandidos: {stats_manhattan['nodes_expanded']}")
        print(f"  Avaliados: {stats_manhattan['nodes_evaluated']}")
    else:
        print(f"  [ERRO] {stats_manhattan['error']}")
    print()
    
    print("[5] Comparando com NetworkX...")
    path_nx, stats_nx = solver.solve_with_networkx(start, goal)
    
    if stats_nx['success']:
        print(f"  [OK] Caminho encontrado!")
        print(f"  Comprimento: {stats_nx['path_length']}")
        print(f"  Custo: {stats_nx['path_cost']:.4f}")
        print(f"  Mesmos resultados? {path == path_nx and stats['path_cost'] == stats_nx['path_cost']}")
    else:
        print(f"  [ERRO] {stats_nx['error']}")
    print()
    
    print("[6] Gerando visualizacoes...")
    visualizer = GridVisualizer(10, 10, builder.obstacles)
    
    if path:
        try:
            import matplotlib
            matplotlib.use('Agg')
            visualizer.save_figure(path, start, goal, 
                                  filename="grid_pathfinding_result.png")
            print("  Figura salva com sucesso!")
        except Exception as e:
            print(f"  [AVISO] Nao foi possivel salvar: {e}")
    print()
    
    print("[7] Testando casos especiais...")
    print("  Teste 1: Inicio = Objetivo")
    path_same, stats_same = solver.solve(start, start)
    print(f"  Resultado: {path_same}, Custo: {stats_same['path_cost']}")
    
    unreachable_goal = (5, 5)
    if unreachable_goal not in builder.obstacles:
        print(f"  Teste 2: No {unreachable_goal} nao eh obstaculo")
    print()
    
    print("=" * 70)
    print("RESUMO DA EXECUCAO")
    print("=" * 70)
    print(f"Grid: 10x10 com {info['num_obstacles']} obstaculos")
    print(f"Inicio: {start} | Objetivo: {goal}")
    print(f"Caminho encontrado: {stats['success']}")
    if stats['success']:
        print(f"Comprimento: {stats['path_length']} | Custo: {stats['path_cost']:.4f}")
        print(f"Expandidos: {stats['nodes_expanded']} | Avaliados: {stats['nodes_evaluated']}")
    print()
    print("Execucao concluida!")
    print("=" * 70)


if __name__ == "__main__":
    main()
