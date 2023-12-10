
### Cabeçalhos e Definições

- Inclui cabeçalhos padrão de C++ para manipulação de entrada/saída, estruturas de dados, matemática e tempo.
- Define constantes e abreviações para facilitar o acesso e a manipulação de dados.

### Estrutura do Grafo (`graph`)

- Define um grafo com um número especificado de vértices (`n`).
- Contém uma estrutura interna `edge` para representar uma aresta com origem (`src`), destino (`dst`) e peso (`weight`).
- Possui um método `add_edge` para adicionar arestas ao grafo.

### Algoritmo Chu-Liu/Edmonds (`arborescence`)

O algoritmo Chu-Liu/Edmonds é um método para encontrar uma arborescência mínima (ou uma árvore geradora mínima direcionada) em um grafo direcionado ponderado. O algoritmo pode ser dividido em várias etapas principais:

1. **Encontrando Arestas de Entrada Mínimas**:
   - Para cada vértice no grafo (exceto a raiz `r`), o algoritmo encontra a aresta de entrada com o menor peso. Essas são as arestas que conectam o vértice a seu predecessor mais barato.
   - Isso é feito para tentar construir uma arborescência - uma árvore que alcança todos os vértices a partir da raiz.

2. **Verificação de Arborescência**:
   - Após selecionar as arestas de entrada mais baratas para cada vértice, o algoritmo verifica se essas arestas formam uma arborescência.
   - Uma arborescência é válida se não houver ciclos, ou seja, se puder ser formada uma árvore onde cada vértice (exceto a raiz) tem exatamente uma aresta de entrada.

3. **Contração de Ciclos**:
   - Se forem encontrados ciclos com as arestas de entrada mínimas, o algoritmo passa a contrair esses ciclos. A contração de um ciclo significa tratar todos os vértices no ciclo como um único vértice super.
   - Durante a contração, as arestas internas do ciclo são removidas e as arestas de entrada e saída do ciclo são ajustadas para refletir a nova configuração.

4. **Recursão ou Iteração**:
   - Após contrair todos os ciclos detectados, o algoritmo repete o processo para o novo grafo (com ciclos contraídos). Isso é feito até que não sejam mais encontrados ciclos.
   - Em cada repetição, o grafo fica progressivamente menor (devido à contração dos ciclos), facilitando a detecção da arborescência mínima.

5. **Finalização**:
   - O processo termina quando uma arborescência é encontrada (ou seja, um conjunto de arestas que alcança todos os vértices a partir da raiz sem formar ciclos).
   - O peso da arborescência mínima é a soma dos pesos das arestas selecionadas.

6. **Complexidade**:
   - A complexidade do algoritmo é O(mn), onde `m` é o número de arestas e `n` é o número de vértices do grafo. Esta complexidade é derivada da necessidade de examinar e contrair ciclos em várias iterações.

### Exemplo de Uso no Código

No código fornecido, a função `arborescence` implementa este algoritmo. Ela usa estruturas de dados como vetores para armazenar as melhores arestas de entrada (`in`) e para controlar a contração dos ciclos (`C` e `mark`). A cada iteração, o algoritmo atualiza essas estruturas até encontrar uma arborescência ou determinar que uma arborescência não pode ser formada.

## Conclusão da Execução do Algoritmo com Análise Estatística dos Resultados

Após a execução do algoritmo Chu-Liu/Edmonds em uma série de grafos aleatórios, podemos chegar a algumas conclusões importantes, tanto qualitativas quanto quantitativas:

### Conclusões Qualitativas

- O algoritmo demonstra capacidade de lidar com uma ampla gama de estruturas de grafos, como indicado pela variabilidade nos pesos das arborescências mínimas.
- O desempenho do algoritmo varia significativamente, o que pode ser atribuído à natureza aleatória dos grafos e à complexidade de suas estruturas.
- A eficiência do algoritmo em diferentes condições oferece insights valiosos sobre sua aplicabilidade prática e áreas potenciais para otimização.

### Análise Estatística dos Resultados

- **Peso Médio da Arborescência Mínima**: A média dos pesos das arborescências mínimas encontradas foi de aproximadamente 20.223,27.
- **Maior e Menor Peso da Arborescência Mínima**: Os pesos variaram de um mínimo de 17.862 a um máximo de 22.619, indicando a diversidade nas estruturas dos grafos testados.
- **Tempo Médio de Execução**: O tempo médio de execução foi de cerca de 0,341 segundos, demonstrando uma eficiência geral satisfatória.
- **Variação no Tempo de Execução**: A variação no tempo de execução (de 0,001 a 0,838 segundos) reflete a influência da complexidade do grafo no desempenho do algoritmo.

### Considerações Finais

Estas observações, juntamente com a análise estatística, fornecem uma visão detalhada do comportamento e eficiência do algoritmo Chu-Liu/Edmonds. Os resultados destacam a habilidade do algoritmo em encontrar arborescências mínimas em variadas instâncias de grafos e apontam para as variações de desempenho que podem ser atribuídas às características específicas de cada grafo. Esses insights são fundamentais para avaliar onde o algoritmo se destaca e onde melhorias ou otimizações podem ser necessárias para lidar com casos mais complexos de forma eficiente.~

### Referências

- O código é baseado nos trabalhos de Y. J. Chu e T. H. Liu (1965) e J. Edmonds (1967) sobre arborescências mínimas em grafos direcionados.
- [Alteração no código escrito por Takanori MAEHARA](https://github.com/spaghetti-source/algorithm/blob/master/graph)

### Notas Adicionais

- O programa é uma implementação prática do algoritmo Chu-Liu/Edmonds com um foco em testar e medir seu desempenho em diferentes instâncias de grafos aleatórios.
- O uso de arquivos CSV para registrar os resultados permite uma análise posterior dos dados coletados, útil para avaliar a eficiência do algoritmo.
