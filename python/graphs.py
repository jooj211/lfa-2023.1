import matplotlib.pyplot as plt

# Dados
dados1 = [11.619, 11.039, 9.516, 11.373, 11.352, 9.491, 12.127, 9.425, 11.548, 9.189, 9.544, 12.111, 10.231, 9.612, 13.009]
dados2 = [8.432735681533813, 9.161964893341064, 10.449620485305786, 10.96143627166748, 11.022583723068237, 10.60813021659851, 9.910183906555176, 9.91233491897583, 9.830678462982178, 9.830116271972656, 10.260095357894897, 10.532334566116333, 9.912833213806152, 10.345981121063232, 11.338716983795166]

# Criando os valores do eixo x (índices dos dados)
indices1 = range(len(dados1))
indices2 = range(len(dados2))

# Criando o gráfico de linhas para o primeiro conjunto de dados
plt.plot(indices1, dados1, marker='o', linestyle='-', color='blue', label='Java')

# Criando o gráfico de linhas para o segundo conjunto de dados
plt.plot(indices2, dados2, marker='o', linestyle='-', color='green', label='Python')

# Configurando os rótulos dos eixos
plt.xlabel('Índice')
plt.ylabel('Valores')

# Configurando o título do gráfico
plt.title('Tempos para 100000 execuções')

# Adicionando uma legenda
plt.legend()

# Exibindo o gráfico
plt.show()