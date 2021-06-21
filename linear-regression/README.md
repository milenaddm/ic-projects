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
linear-regression-multi-variables usage:

python3 linear-regression-multi-variables -m <maxepocas> -l <learning-rate>
```

### Exemplo

Para aproximar a saída com `<maxepocas> ` = 100 e `<learning-rate>` = 0.01, use o comando:
```bash
python3 linear-regression-multi-variables -m 100 -l 0.01
```

### Principais resultados
![Data](./linear-regression-multi-variables/images/Graph1.png)
![Data](./linear-regression-multi-variables/images/Graph2.png)
![Cost x number of iteractions with alpha=0.01](./linear-regression-multi-variables/images/Graph3.png)
![Cost x number of iteractions with alpha=0.05](./linear-regression-multi-variables/images/Graph4.png)
![Cost x number of iteractions with alpha=0.1](./linear-regression-multi-variables/images/Graph5.png)

### 2.3
Veja que agora não é possível traçar o ajuste linear como no exercício anterior. Por quê?
Não é possível traçar o ajudses linear pois a combinação linear das duas variáveis não é suficiente para representar o comportamento dos dados. Seria necessário fazer a adição de características polinomiais, por exemplo interações entre as variáveis, para fazer a represnetação correta.



## Equação Normal
### Funcionamento:
Basta digitar o comando
```bash
python normal-equation
```

### Resultado
Equação nominal: 140.86 + 16978.19x

## Conclusão
Pode-se observar que implementar a equação nominal é mais simples que implmentar o gradiente decrescente, além de se ter um resultado exato.
