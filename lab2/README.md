## LAB 2
## Quicksort

Teste: vetores de tamanhos de potências de 10
Formato: mesmo do Lab1

- Passar o particionador para o primeiro elemento

- Escolha do particionador
1. Mediana de 3: primeiro, meio, último - fazer a mediana
2. Aleatório: gera um índice aleatório entre o primeiro e o último índice

- Particionamento (grupos)
1. Lomuto
2. Hoare: direita-esquerda, esquerda-direita, etc
* Exemplo dos particionamentos: https://moodle.inf.ufrgs.br/pluginfile.php/182227/mod_resource/content/1/exemplo-particionamento.cpp

-> Testar as 4 combinações com 5 vetores de tamanhos diferentes

- Estatísticas da execução (4 arquivos)
    * Tamanho da entrada
    * Número de trocas
    * Número de recursões
    * Tempo em segundos