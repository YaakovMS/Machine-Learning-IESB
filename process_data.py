import pandas as pd
import statistics
import matplotlib.pyplot as plt

# Exercício 01 - Ajuste as idades que não são válidas ou estão vazias para a moda da amostra. Grave a saída no arquivo Resposta01.txt.
# Ler arquivo csv
df = pd.read_csv("dados.csv")

# Copiando para validData o arquivo com as idades válidas
validData = df['age'].dropna()

modeFile = statistics.mode(validData)

# Utilizando a variável modeFile que possui a moda das idades válidas e preenchendo o arquivo original
df['age'].fillna(modeFile, inplace=True)

# Criando arquivo e adicionando entradas do arquivo CSV com as idades válidas
with open("Resposta01.txt", "w") as f:
    f.write(df.to_string(index=False))

# Exercício 02 - Apresente no terminal o somatório de homens (male) e de mulheres (female)
count = df['sex'].value_counts()
print(f'O número de homens é: {count["male"]}\nO número de mulheres é: {count["female"]}')

# Exercício 03 -  Considerando a coluna "survived", sendo 0 como não sobrevivente e 1 como sobrevivente, apresente em um gráfico de pizza a porcentagem de sobreviventes e não sobreviventes.
alive = df['survived'].value_counts()
plt.figure(figsize=(5, 5))
plt.pie(alive, labels=['Dead', 'Alive'], autopct="%.2f%%")
plt.title('Dead and Alive')
plt.savefig("pieGraph.png")  # Salvar gráfico em um arquivo

# Exercício 04 - Apresente o gráfico de dispersão da Idade pela tarifa.
plt.figure(figsize=(5, 5))
plt.scatter(df['age'], df['fare'])
plt.xlabel('Age')
plt.ylabel('Fare')
plt.title('Age dispersion by fare')
plt.savefig("scatterGraph.png")  # Salvar gráfico em um arquivo

plt.show()  # Exibir os gráficos
