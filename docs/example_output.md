# Saída Esperada da Execução

Este documento mostra a saída esperada ao executar `python examples/main.py`.

## Output Console

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
Figure saved as grid_pathfinding_result.png

[PASSO 7] Testando casos especiais...
  - Teste 1: Início = Objetivo
    Resultado: [(0, 0)], Custo: 0
  - Teste 2: Nó inacessível (rodeado por obstáculos)
    (O nó (5, 5) não é um obstáculo, pulando teste)

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

## Visualizações Geradas

### 1. Visualização Interativa (Matplotlib)

Ao executar o script, uma janela do matplotlib será exibida mostrando:

- **Fundo cinzento**: células do grid não transitáveis próximas a obstáculos
- **Células verdes**: ponto inicial (0, 0)
- **Células vermelhas**: ponto objetivo (9, 9)
- **Células pretas**: obstáculos
- **Células azul-claro**: células que fazem parte do caminho encontrado
- **Linha azul**: traço visual do caminho ótimo conectando todos os nós
- **Grid de fundo**: mostra as coordenadas de cada célula

### 2. Arquivo de Imagem

O arquivo `grid_pathfinding_result.png` é salvo no diretório de execução com alta resolução (150 DPI).

## Análise dos Resultados

### Comparação de Heurísticas

- **Euclidiana**: 43 nós expandidos
- **Manhattan**: 38 nós expandidos (mais eficiente)

A heurística de Manhattan é mais informada para este tipo de grafo, resultando em menos expansões de nós.

### Otimalidade

O custo do caminho é idêntico entre as três abordagens (18.0), confirmando:

1. ✓ Implementação do A\* é ótima
2. ✓ Ambas as heurísticas são admissíveis
3. ✓ Compatibilidade com NetworkX

### Características do Caminho

- Comprimento: 19 nós
- Custo: 18.0 unidades (movimentos horizontais/verticais custam 1.0)
- Eficiência: Desvia dos obstáculos sem desvios desnecessários

## Solução de Problemas

### Se as visualizações não aparecerem

- Verifique se matplotlib está instalado: `pip install matplotlib`
- Em ambiente remoto, use: `matplotlib.use('Agg')` antes de criar gráficos

### Se houver erro de importação

```bash
# Reinstale as dependências
pip install -r requirements.txt

# Ou instale manualmente
pip install networkx matplotlib numpy
```

### Se o grid não parecer conectado

Verifique se o ponto inicial e objetivo não estão rodeados por obstáculos. O arquivo `graph_builder.py` testa a conectividade do grafo.

---

**Nota**: Os números exatos de nós expandidos/avaliados podem variar ligeiramente dependendo da implementação exata e ordem de processamento, mas o caminho ótimo e seu custo devem ser idênticos.
