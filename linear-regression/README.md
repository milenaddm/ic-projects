# Tarefa 3 - Regressão Linear

**Disciplina**: Inteligência Computacional

**Professor**: Rogério Martins Gomes

**Alunos**:
Marcelo Lopes de Macedo Ferreira Cândido
Milena Delarete Drummond Marques

## Configuração:
Na raiz do projeto, execute o seguinte comando para instalar as dependências necessárias:
```
pip3 install -r "./requirements.txt"
```

## 1. Com uma variável
### Funcionamento:
O comando `python3 linear-regression-one-variable -h` mostra como usar o pacote, como visto na seguinte saída:
```bash
linear-regression-one-variable usage:

python3 linear-regression-one-variable -m <maxepocas>
```

### Exemplo

Para aproximar a saída com `<maxepocas> ` = 100, use o comando:
```bash
python3 linear-regression-one-variable -m 100
```

### Principais resultados
![Lucro por população x Lucro em $10.000s](./linear-regression-one-variable/images/Graph1.png)
![Custo em relação ao múmero de operações](./linear-regression-one-variable/images/Graph2.png)
![Lucro por população x Lucro em $10.000s](./linear-regression-one-variable/images/Graph3.png)

## 2. Com múltiplas variáveis
### Funcionamento:
O comando `python3 linear-regression-multi-variables -h` mostra como usar o pacote, como visto na seguinte saída:
```bash
Perceptron usage:

python3 linear-regression-multi-variables -m <maxepocas> -l <learning-rate>
```

## Exemplo

Para aproximar a saída com `<maxepocas> ` = 100 e `<learning-rate>` = 0.01, use o comando:
```bash
python3 linear-regression-multi-variables -m 100 -l 0.01
```

## Gráficos
Os gráfico plotados durante a execução e de acordo com o pedido na atividade são:
![Gráfico 1](./images/Graph1.png)
![Gráfico 2](./images/Graph2.png)
![Gráfico 3](./images/Graph3.png)
![Gráfico 4](./images/Graph4.png)
![Gráfico 5](./images/Graph5.png)

### 2.3
Veja que agora não é possível traçar o ajuste linear como no exercício anterior. Por quê?

## 3. Equação Normal



