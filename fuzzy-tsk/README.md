# Tarefa 1 - Aproximação de Funções com Modelos Fuzzy TSK

**Disciplina**: Inteligência Computacional

**Professor**: Rogério Martins Gomes

**Alunos**:
Marcelo Lopes de Macedo Ferreira Cândido
Milena Delarete Drummond Marques

## Objetivo

O objetivo desta atividade é, utilizando o Método do gradiente mostrados nos slides e vídeos do tópico 3, aproximar a saída para f(x)=x^2


## Execução do algoritmo

### 1. Configuração:
Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```
pip3 install -r "./requirements.txt"
```

### 2. Funcionamento:
O comando `python3 fuzzy-tsk -h` mostra como usar o pacote, como visto na seguinte saída:
```bash
Perceptron usage:

python3 fuzzy-tsk 
```

## Exemplo

Para determinar o custo para `<pop-size>` = 20 e `<mutation-rate>` = 0.005, use o comando:
```bash
python3 minimization-genetic-algorithm -p 50 -m 0.005
```

O resultado a ser impresso na tela será:
```
Generation: 0
Generation: 50
Generation: 100
Generation: 150
Generation: 200
Generation: 250
Generation: 267
Best individual and fitness: [-1.58214947 -3.13022245], -106.76453666013647
```

**OBS.:** O resultado pode variar pois, ao executar o programa, a populacao inicial é gerada aleatoriamente. 



## Versões do Python recomendadas

Dois computadores foram usados para rodar esse algoritmo e as versão utlizadas foram `3.7.4` e `3.9.1`.

