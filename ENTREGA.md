# Entrega: Algoritmo A\* - Busca em Grid com Obstáculos

## ✓ Checklist de Entrega

- [x] **Problema modelado como grafo**: Grid 2D com obstáculos, conexões 4-vizinhos
- [x] **Algoritmo A\* implementado**: Implementação do zero em `src/a_star_solver.py`
- [x] **Heurísticas admissíveis**: Euclidiana e Manhattan
- [x] **Integração com NetworkX**: Construção de grafo e validação com NetworkX
- [x] **Visualização com matplotlib**: Grid e caminho destacado
- [x] **Código comentado**: Todos os arquivos com docstrings e comentários
- [x] **README completo**: Documentação detalhada com exemplos
- [x] **Execução sem erros**: Todos os testes passam
- [x] **Estrutura de repositório**: Organização profissional de arquivos

---

## 📦 Arquivos Entregues

### Estrutura do Projeto

```
search-activity-aStar/
├── README.md                 # Documentação completa do projeto
├── requirements.txt          # Dependências Python
├── src/
│   ├── __init__.py          # Inicialização do pacote
│   ├── graph_builder.py     # Construção do grafo (240 linhas)
│   ├── a_star_solver.py     # Implementação A* (320 linhas)
│   └── visualizer.py        # Visualização matplotlib (210 linhas)
├── examples/
│   └── main.py              # Script de demonstração (142 linhas)
└── docs/
    └── example_output.md    # Saída esperada da execução
```

### Detalhes dos Arquivos Python

#### 1. **src/graph_builder.py** (240 linhas)

- Classe `GridGraphBuilder`
- Construção de grafo a partir de grid 2D
- Método `build()`: cria nós e arestas com pesos
- Método `get_graph_info()`: retorna estatísticas
- Método `create_sample_grid()`: cria grid de exemplo com obstáculos

#### 2. **src/a_star_solver.py** (320 linhas)

- Classe `AStarSolver`
- Implementação completa do algoritmo A\*
- Métodos heurísticas: euclidiana e Manhattan
- Método `solve()`: encontra caminho ótimo
- Método `solve_with_networkx()`: validação com NetworkX
- Estruturas de dados: open_set (heap), closed_set, g_score, f_score

#### 3. **src/visualizer.py** (210 linhas)

- Classe `GridVisualizer`
- Método `visualize_grid_and_path()`: visualização interativa
- Método `visualize_graph_network()`: grafo como rede
- Método `save_figure()`: salva PNG de alta resolução
- Elementos: obstáculos, células do caminho, início/objetivo

#### 4. **examples/main.py** (142 linhas)

- Script executável que demonstra:
  1. Criação do grid e grafo
  2. Execução com heurística euclidiana
  3. Execução com heurística de Manhattan
  4. Comparação com NetworkX
  5. Visualização e salvamento de figura
  6. Testes de casos especiais
  7. Resumo com estatísticas

---

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7+
- Pip

### Instalação (passo a passo)

```bash
# 1. Clonar ou abrir o repositório
cd search-activity-aStar

# 2. Criar ambiente virtual
python -m venv venv

# 3. Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 4. Instalar dependências
pip install -r requirements.txt

# 5. Executar o programa
python examples/main.py
```

### Saída Esperada

```
======================================================================
ALGORITMO A* - BUSCA EM GRID COM OBSTACULOS
======================================================================

[PASSO 1] Criando grid de exemplo...
  - Dimensoes do grid: (10, 10)
  - Numero de nos: 87
  - Numero de arestas: 140
  - Numero de obstaculos: 13
  - Grafo conectado: True

[PASSO 2] Definindo pontos de inicio e objetivo...
  - Inicio: (0, 0)
  - Objetivo: (9, 9)

[PASSO 3] Executando A* com heuristica euclidiana...
  [OK] Caminho encontrado!
  - Comprimento do caminho: 19 nos
  - Custo do caminho: 18.0000
  - Nos expandidos: 85
  - Nos avaliados: 140

[PASSO 4] Executando A* com heuristica de Manhattan...
  [OK] Caminho encontrado!
  - Comprimento do caminho: 19 nos
  - Custo do caminho: 18.0000
  - Nos expandidos: 82
  - Nos avaliados: 138

[PASSO 5] Comparando com implementacao nativa do NetworkX...
  [OK] Caminho encontrado!
  - Comprimento do caminho: 19 nos
  - Custo do caminho: 18.0000
  - Mesmos resultados? True

[PASSO 6] Gerando visualizacoes...
  - Salvando figura em arquivo...
  Figure saved as grid_pathfinding_result.png
  - Figura salva com sucesso!

[PASSO 7] Testando casos especiais...
  - Teste 1: Inicio = Objetivo
    Resultado: [(0, 0)], Custo: 0.0

======================================================================
RESUMO DA EXECUCAO
======================================================================
Grid: 10x10 com 13 obstaculos
Inicio: (0, 0) | Objetivo: (9, 9)
Caminho encontrado: True
Comprimento: 19 nos | Custo: 18.0000
Performance: 85 expandidos, 140 avaliados

Execucao concluida com sucesso!
======================================================================
```

---

## 📊 Resumo da Solução

### Problema

**Navegação em Grid com Obstáculos**: Encontrar o caminho mais curto de um ponto inicial a um objetivo em um grid 2D que contém obstáculos, usando apenas movimentos horizontais e verticais (4-conectividade).

### Modelagem como Grafo

```
G = (V, E)
V = {(y,x) | 0 ≤ y < 10, 0 ≤ x < 10, (y,x) não é obstáculo}
E = {((y,x), (ny,nx)) | células adjacentes horizontais/verticais}
w(e) = √[(Δy)² + (Δx)²] = 1.0 para adjacentes ortogonais
```

### Algoritmo A\*

**Fórmula**: f(n) = g(n) + h(n)

- **g(n)**: Custo real do início até o nó n
- **h(n)**: Heurística admissível (euclidiana ou Manhattan)
- **f(n)**: Custo estimado total

**Pseudocódigo**:

```
enquanto open_set não vazio:
  current ← nó com menor f_score
  se current == objetivo:
    retornar caminho
  para cada vizinho de current:
    se vizinho melhor que anterior:
      atualizar g_score, f_score
      adicionar à open_set
retornar None
```

### Heurísticas Implementadas

1. **Euclidiana** (padrão)
   - h(n) = √[(y_goal - y_n)² + (x_goal - x_n)²]
   - Admissível, mais informada

2. **Manhattan**
   - h(n) = |y_goal - y_n| + |x_goal - x_n|
   - Admissível para 4-conectividade, menos nós expandidos

### Resultados

**Grid 10×10 com 13 obstáculos**:

- Caminho encontrado: Sim
- Comprimento do caminho: 19 nós
- Custo: 18.0 unidades
- Performance (Euclidiana): 85 nós expandidos de 87 totais
- Performance (Manhattan): 82 nós expandidos de 87 totais
- Otimalidade: Confirmada (NetworkX valida)

---

## 💻 Código Destaque

### Inicialização do A\*

```python
solver = AStarSolver(graph, heuristic=None)  # Euclidiana padrão
path, stats = solver.solve(start=(0, 0), goal=(9, 9))

if stats['success']:
    print(f"Caminho: {path}")
    print(f"Comprimento: {stats['path_length']}")
    print(f"Custo: {stats['path_cost']}")
    print(f"Expandidos: {stats['nodes_expanded']}")
```

### Construção do Grafo

```python
builder = GridGraphBuilder(width=10, height=10, obstacles={...})
graph = builder.build()

# Resultado:
# - 87 nós (100 - 13 obstáculos)
# - 140 arestas (conexões entre vizinhos)
# - Grafo conectado
```

### Visualização

```python
visualizer = GridVisualizer(width=10, height=10, obstacles=builder.obstacles)
visualizer.save_figure(path, start=(0, 0), goal=(9, 9),
                      filename="resultado.png")

# Gera PNG 150 DPI com:
# - Obstáculos em preto
# - Células do caminho em azul
# - Início em verde, objetivo em vermelho
```

---

## 📚 Conceitos Teóricos

### Por que A\*?

| Algoritmo | Informado | Ótimo   | Eficiente     |
| --------- | --------- | ------- | ------------- |
| BFS       | Não       | Sim     | Razoável      |
| DFS       | Não       | Não     | Razoável      |
| Dijkstra  | Não       | Sim     | Bom           |
| **A\***   | **Sim**   | **Sim** | **Excelente** |
| Gulosa    | Sim       | Não     | Excelente     |

### Admissibilidade

Uma heurística h(n) é **admissível** se: `h(n) ≤ custo real mínimo`

**Prova de admissibilidade**:

- Euclidiana: distância direta ≤ caminho real ✓
- Manhattan: sem diagonal ≤ distância euclidiana ✓

### Completude e Otimalidade

- **Completo**: Sim, A\* com heurística admissível encontra solução se existir
- **Ótimo**: Sim, garante caminho de menor custo com heurística admissível
- **Complexidade**: O(b^d) pior caso, O(d) com heurística perfeita

---

## 🔧 Possíveis Extensões

1. **Movimentos Diagonais**: Adicionar 4 vizinhos diagonais (8-conectividade)
2. **Pesos Variáveis**: Diferentes custos por tipo de terreno
3. **Busca Bidirecional**: Buscar do início e objetivo simultaneamente
4. **D\* Lite**: Replanejamento dinâmico quando obstáculos mudam
5. **Jump Point Search**: Aceleração para grids uniformes

---

## 📋 Requisitos Atendidos

### ✓ Requisitos Técnicos

- Python 3.x: 3.12.10 utilizado
- NetworkX: Versão 3.6.1
- Matplotlib: Versão 3.10.9
- NumPy: Versão 2.4.6
- Código executável: Sem erros
- Visualização: PNG de 150 DPI gerado

### ✓ Requisitos Acadêmicos

- Modelagem de grafo: Explicada com notação formal
- Algoritmo A\*: Implementado do zero com detalhes
- Heurísticas: Duas heurísticas admissíveis implementadas
- Código comentado: 70+ linhas de comentários e docstrings
- README: Seções completas com teoria e prática
- Estrutura de projeto: Organização profissional

---

## 🎯 Conclusão

Este projeto implementa com sucesso o algoritmo A\* para pathfinding em grids com obstáculos. A solução é:

✓ **Teórica**: Fundamentação em algoritmos de busca informada  
✓ **Prática**: Código executável e bem organizado  
✓ **Educacional**: Bem documentado para aprendizado  
✓ **Reproduzível**: Fácil de executar e estender  
✓ **Profissional**: Estrutura de repositório GitHub-ready

---

## 👤 Informações

**Atividade**: Algoritmos de Busca e Grafos  
**Data de Entrega**: Maio 2026  
**Status**: ✓ Completo e Validado

---

## 📞 Suporte

Para questões sobre o código:

1. Consultar README.md para documentação teórica
2. Ver docstrings nos arquivos .py
3. Executar `python examples/main.py` para demonstração
4. Verificar comentários inline no código
