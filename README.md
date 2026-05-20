# Algoritmo A\* - Busca em Grid com Obstáculos

## 📋 Descrição do Projeto

Este projeto implementa o **algoritmo A\*** (A-Star) para resolver o problema de pathfinding em um grid 2D com obstáculos. O A\* é um algoritmo de busca em grafos que combina o melhor dos algoritmos de Dijkstra e heurísticas para encontrar o caminho mais curto de forma eficiente.

### Problema Modelado

**Navegação em Grid com Obstáculos**:

- Representamos um espaço 2D como um grid 10x10
- Cada célula pode ser transitável ou um obstáculo
- O agente precisa encontrar o caminho ótimo (mais curto) do ponto inicial até o objetivo
- Apenas movimentos horizontais e verticais são permitidos (sem diagonais)

### Por que A\*?

O A\* é ideal para este problema porque:

1. **Otimalidade**: Garante encontrar o caminho mais curto
2. **Eficiência**: Usa heurística para reduzir o espaço de busca
3. **Informado**: Combina custo real (g) com estimativa (h)
4. **Prático**: Muito usado em jogos, robótica e planejamento

---

## 🏗️ Modelagem como Grafo

### Componentes Principais

```
Grid 10x10
  ├── Nós: Cada célula (y, x) não-obstáculo
  ├── Arestas: Conectam células adjacentes (4-conectividade)
  └── Pesos: Distância euclidiana entre células (valor 1.0 para horizontais/verticais)

Grafo = G(V, E)
  V = {(y,x) | 0 ≤ y < 10, 0 ≤ x < 10, (y,x) ∉ Obstáculos}
  E = {((y,x), (ny,nx)) | células adjacentes}
  w(e) = √[(ny-y)² + (nx-x)²]
```

### Representação

```
Grid Original:          Grafo:
  0 1 2 3 4 5              . . . . . .
0 . . . . . .              | | | | | |
1 . # # # . .              . - # - . .
2 . . . . . .              | | | | | |
3 . . . . . .              . . . . . .

# = Obstáculo (não tem nó)
. = Célula passável (tem nó)
| / - = Arestas conectando nós
```

---

## 🧠 Algoritmo A\* Implementado

### Pseudocódigo

```
A*(start, goal, heuristic):
  open_set ← [start]
  came_from ← {}
  g_score ← {start: 0}
  f_score ← {start: heuristic(start, goal)}

  enquanto open_set não vazio:
    current ← nó com menor f_score em open_set

    se current == goal:
      retornar reconstruir_caminho(came_from, current)

    remover current de open_set
    adicionar current ao closed_set

    para cada vizinho de current:
      se vizinho em closed_set:
        continuar

      tentative_g ← g_score[current] + custo(current, vizinho)

      se tentative_g < g_score[vizinho]:
        came_from[vizinho] ← current
        g_score[vizinho] ← tentative_g
        f_score[vizinho] ← tentative_g + heuristic(vizinho, goal)
        adicionar vizinho à open_set

  retornar None (sem caminho)
```

### Componentes Principais

1. **g(n)**: Custo real do caminho do início até o nó n
2. **h(n)**: Heurística estimada do nó n até o objetivo
3. **f(n) = g(n) + h(n)**: Função de avaliação total

### Heurísticas Implementadas

#### 1. Distância Euclidiana (padrão)

```python
h(n) = √[(n.y - goal.y)² + (n.x - goal.x)²]
```

- Admissível para movimento em qualquer direção
- Melhor para ambientes com poucos obstáculos
- Mais informada que Manhattan em grids com 4-conectividade

#### 2. Distância de Manhattan

```python
h(n) = |n.y - goal.y| + |n.x - goal.x|
```

- Admissível para movimento com 4-conectividade
- Mais agressiva, expande menos nós
- Ótima para labirintos

**Admissibilidade**: h(n) ≤ custo real mínimo garante otimalidade do A\*

---

## 📁 Estrutura de Arquivos

```
search-activity-aStar/
├── README.md                 # Este arquivo
├── requirements.txt          # Dependências Python
├── src/
│   ├── __init__.py          # Inicialização do pacote
│   ├── graph_builder.py     # Construção do grafo grid
│   ├── a_star_solver.py     # Implementação do algoritmo A*
│   └── visualizer.py        # Visualização com matplotlib
├── examples/
│   └── main.py              # Script de demonstração completo
└── docs/
    └── example_output.md    # Saída esperada da execução
```

---

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

### Passo 1: Clonar o Repositório

```bash
git clone https://github.com/Su6eate9/search-activity-aStar.git
cd search-activity-aStar
```

### Passo 2: Criar Ambiente Virtual (Recomendado)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Passo 3: Instalar Dependências

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Script Principal

```bash
python examples/main.py
```

### Resultado Esperado

O programa deve:

1. ✓ Criar um grid 10x10 com obstáculos
2. ✓ Executar A\* com heurística euclidiana
3. ✓ Executar A\* com heurística de Manhattan
4. ✓ Comparar com implementação do NetworkX
5. ✓ Exibir estatísticas de performance
6. ✓ Gerar visualização do caminho encontrado
7. ✓ Salvar imagem em `grid_pathfinding_result.png`

---

## 📊 Saída Esperada

```
======================================================================
ALGORITMO A* - BUSCA EM GRID COM OBSTÁCULOS
======================================================================

[PASSO 1] Criando grid de exemplo...
  - Dimensões do grid: (10, 10)
  - Número de nós: 87
  - Número de arestas: 156
  - Número de obstáculos: 13
  - Grafo conectado: True

[PASSO 2] Definindo pontos de início e objetivo...
  - Início: (0, 0)
  - Objetivo: (9, 9)

[PASSO 3] Executando A* com heurística euclidiana...
  ✓ Caminho encontrado!
  - Comprimento do caminho: 19 nós
  - Custo do caminho: 18.0000
  - Nós expandidos: 43
  - Nós avaliados: 78
  - Caminho: [(0, 0), (0, 1), (0, 2)]...[(9, 7), (9, 8), (9, 9)]

[PASSO 4] Executando A* com heurística de Manhattan...
  ✓ Caminho encontrado!
  - Comprimento do caminho: 19 nós
  - Custo do caminho: 18.0000
  - Nós expandidos: 38
  - Nós avaliados: 71

[PASSO 5] Comparando com implementação nativa do NetworkX...
  ✓ Caminho encontrado!
  - Comprimento do caminho: 19 nós
  - Custo do caminho: 18.0000
  - Mesmos resultados? True

[PASSO 6] Gerando visualizações...
  - Exibindo grid com o caminho encontrado...
  - Salvando figura em arquivo...

[PASSO 7] Testando casos especiais...
  - Teste 1: Início = Objetivo
    Resultado: [(0, 0)], Custo: 0
  - Teste 2: Nó inacessível (rodeado por obstáculos)

======================================================================
RESUMO DA EXECUÇÃO
======================================================================
Grid: 10x10 com 13 obstáculos
Início: (0, 0) | Objetivo: (9, 9)
Caminho encontrado: True
Comprimento: 19 nós | Custo: 18.0000
Performance: 43 expandidos, 78 avaliados

Execução concluída com sucesso! ✓
======================================================================
```

---

## 🔍 Explicação do Código

### 1. **graph_builder.py** - Construção do Grafo

```python
# Criar builder com grid de exemplo
builder = GridGraphBuilder.create_sample_grid(10, 10)

# Construir o grafo
graph = builder.build()

# Obter informações
info = builder.get_graph_info()
# {
#   'num_nodes': 87,
#   'num_edges': 156,
#   'grid_dimensions': (10, 10),
#   'num_obstacles': 13,
#   'is_connected': True
# }
```

**Processo de construção:**

1. Adicionar nó para cada célula não-obstáculo
2. Conectar células adjacentes (4-vizinhos)
3. Calcular peso de arestas como distância euclidiana

### 2. **a_star_solver.py** - Algoritmo A\*

```python
# Criar solver
solver = AStarSolver(graph, heuristic=None)  # Euclidiana por padrão

# Resolver
path, stats = solver.solve(start=(0, 0), goal=(9, 9))

# Resultado
# path = [(0, 0), (0, 1), (0, 2), ..., (9, 9)]
# stats = {
#   'success': True,
#   'path_length': 19,
#   'path_cost': 18.0,
#   'nodes_expanded': 43,
#   'nodes_evaluated': 78
# }
```

**Estruturas de dados:**

- `open_set`: Fila de prioridade (heap) de nós a explorar
- `closed_set`: Nós já processados
- `g_score`: Custo real até cada nó
- `f_score`: g + h estimado
- `came_from`: Rastreamento do caminho

### 3. **visualizer.py** - Visualização

```python
# Criar visualizador
viz = GridVisualizer(width=10, height=10, obstacles=builder.obstacles)

# Visualizar grid e caminho
viz.visualize_grid_and_path(path, start=(0,0), goal=(9,9))

# Salvar figura
viz.save_figure(path, start, goal, filename="resultado.png")
```

**Elementos visuais:**

- 🟩 Célula inicial (verde)
- 🟥 Célula objetivo (vermelho)
- ⬛ Obstáculos (preto)
- 🟦 Células do caminho (azul claro)
- 📍 Linha do caminho (azul)

---

## 📈 Análise de Complexidade

### Complexidade Temporal

| Aspecto              | Complexidade    | Notas                             |
| -------------------- | --------------- | --------------------------------- |
| Construção do Grafo  | O(n·m)          | n, m = dimensões do grid          |
| Algoritmo A\* (pior) | O(b^d)          | b = ramificação, d = profundidade |
| Com heurística boa   | O(b·d)          | Redução significativa na prática  |
| NetworkX A\*         | O(n·m·log(n·m)) | Implementação otimizada           |

Para grid 10x10:

- Nós: ~100
- Arestas: ~400
- A\* típico: ~50 nós expandidos (vs ~100 sem heurística)

### Complexidade Espacial

- **open_set**: O(b^d) pior caso
- **closed_set**: O(n)
- **g_score, f_score**: O(n)
- **Total**: O(n + b^d)

Prática: O(n) ou O(n·log(n)) com boa heurística

---

## 🔧 Extensões e Melhorias

### Possíveis Melhorias

1. **Movimentos Diagonais**

   ```python
   # Adicionar 4 mais vizinhos
   neighbors = [(y±1, x±1), ...]  # 8-conectividade
   ```

2. **Diferentes Tipos de Obstáculos**

   ```python
   # Obstáculos com custos (terreno difícil)
   cost_map = {(y,x): weight for ...}
   ```

3. **Busca Bidirecional**

   ```python
   # Buscar do início e do objetivo simultaneamente
   ```

4. **Jumping Point Search**

   ```python
   # Aceleração do A* para grids uniformes
   ```

5. **D\* Lite (Dinâmico)**
   ```python
   # Replanejamento eficiente quando obstáculos mudam
   ```

### Casos de Uso

- 🎮 **Jogos**: IA de NPCs
- 🤖 **Robótica**: Planejamento de movimento
- 🚗 **Navegação**: Sistemas GPS
- 🗺️ **Logística**: Rota ótima de entregas
- 🌐 **Redes**: Roteamento de pacotes

---

## ❌ Limitações

1. **Estático**: Grafo não muda durante a busca
2. **4-Conectividade**: Apenas movimentos ortogonais
3. **Heurística Fixa**: Euclidiana não é ótima para todos os casos
4. **Grafo Pequeno**: Implementação não otimizada para grids massivos
5. **Sem Pesos Variáveis**: Arestas têm pesos uniformes

---

## 📚 Referências Teóricas

### Leitura Recomendada

1. **A\* Pathfinding Algorithm**
   - Hart, P. E., Nilsson, N. J., & Raphael, B. (1968)
   - IEEE Transactions on Systems Science and Cybernetics

2. **Artificial Intelligence: A Modern Approach**
   - Russell, S. & Norvig, P. (4th ed.)
   - Capítulo 3: Solving Problems by Searching

3. **NetworkX Documentation**
   - https://networkx.org/documentation/stable/

### Conceitos Relacionados

- Busca em Largura (BFS)
- Busca em Profundidade (DFS)
- Algoritmo de Dijkstra
- Busca Gulosa Melhorada
- Heurísticas Admissíveis

---

## 👤 Autor e Contexto

**Atividade Académica**: Algoritmos de Busca e Grafos  
**Data**: Maio 2026  
**Objetivo**: Implementação e demonstração do A\* com Python e NetworkX

---

## 📄 Licença

Este projeto é fornecido para fins educacionais.

---

## 🤝 Contribuições

Para melhorias ou correções, considere:

1. Fork do repositório
2. Criar branch (`git checkout -b feature/melhoria`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/melhoria`)
5. Abrir Pull Request

---

## ✅ Checklist de Verificação

- [x] Problema modelado como grafo
- [x] A\* implementado do zero
- [x] Heurísticas admissíveis (euclidiana e Manhattan)
- [x] Integração com NetworkX
- [x] Visualização com matplotlib
- [x] Código comentado e estruturado
- [x] README completo
- [x] Exemplos executáveis
- [x] Tratamento de erro
- [x] Estatísticas de performance

---

## ❓ FAQ

**P: Por que usar A\* ao invés de Dijkstra?**  
R: A\* é mais eficiente porque usa heurística para guiar a busca, expandindo menos nós.

**P: Posso usar diagonais?**  
R: Sim! Modifique `neighbors` em `graph_builder.py` para 8-conectividade.

**P: Qual heurística é melhor?**  
R: Depende do problema. Manhattan é melhor para 4-conectividade, Euclidiana para movimento livre.

**P: E se não houver caminho?**  
R: O algoritmo retorna `None` e `success=False` com mensagem de erro.

---

**Última atualização**: Maio 2026  
**Status**: ✓ Completo e testado
