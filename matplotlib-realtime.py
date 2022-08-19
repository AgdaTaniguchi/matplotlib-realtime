import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def definirGraficoRAM(frame):
    valores.append(round(psutil.virtual_memory().used / psutil.virtual_memory().total * 100, 2)) # adicionando os valores capturados pelo psutil na lista valores
    valores.remove(valores[0]) # remove o primeiro valor da lista

    graficosRAM.cla() # limpa os eixos
    graficosRAM.plot(valores) # plota o gráfico
    graficosRAM.scatter(len(valores) - 1, valores[-1]) # marcador (bolinha) na posição atual do gráfico
    graficosRAM.title.set_text(f'Memória RAM - {valores[-1]}%') # título do gráfico
    graficosRAM.set_ylim(0, 100) # limite do eixo y

# cria uma lista com 50 zeros, esta lista será utilizada no eixo y gráfico
valores = [0] * 50 

# propriedades dos gráficos
janelaGeral = plt.figure(figsize=(3 * 3, 2 * 3), facecolor='#EEE') # cria a janela com o tamanho e a cor

# cria um gráfico dentro da janela
graficosRAM = plt.subplot(311)

graficosRAM.axes.get_xaxis().set_visible(False) # tira a visualização dos dados do eixo x
graficosRAM.set_facecolor('#DDD') # define a cor do gráfico

# função para chamar em loop a função definirGraficoRAM
animacaoGeral = FuncAnimation(janelaGeral, definirGraficoRAM, interval=500)

# abre a janela
plt.show()