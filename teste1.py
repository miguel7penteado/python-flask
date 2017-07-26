''' teste '''

import matplotlib.pyplot as plt
from collections import Counter

def grafico_linha_simples(parametro_plotagem):
    plotagem = None
    plotagem = parametro_plotagem
    anos_eixo_x = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp_eixo_y  = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]
    # Criar um grafico de linha simples, anos no eixo X, gdp no eixo Y
    plotagem.plot(anos_eixo_x, gdp_eixo_y, color='green', marker='o', linestyle='solid')
    # Adicionar um titulo
    plotagem.title(" Valor de GDP Nominal")
    # adiciona um rotulo no eixo y
    plotagem.ylabel("Bilhoes de Reais R$")
    plotagem.xlabel("Tempo em anos")
    plotagem.show()

def grafico_barras_simples(parametro_plotagem):
    plotagem = None
    plotagem = parametro_plotagem
    vetor_valores_eixo_x = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
    vetor_valores_eixo_y = [5, 11, 3, 8, 10]
    # barras tem largura padrao 0.8, entao nos iremos adicionar 0.1 para as coordenadas a esquerda
    # para que cada barra fique centrada
    xs = [contador + 0.1 for contador, _ in enumerate(vetor_valores_eixo_x)]
    # plota barras com coordenadas esquerdas x-coordinates [xs], altura [vetor_valores_eixo_y]
    plotagem.bar(xs, vetor_valores_eixo_y)
    plotagem.ylabel("Numero de estatuetas")
    plotagem.title("Meus filmes favoritos - estatuetas")
    # Rotulo do eixo x com o nome dos filmes no centro da barra
    plotagem.xticks([contador + 0.5 for contador, _ in enumerate(vetor_valores_eixo_x)], vetor_valores_eixo_x)
    plotagem.show()

def grafico_histograma(parametro_plotagem):
    plotagem      = None
    plotagem      = parametro_plotagem
    notas         = [83,95,91,87,70,0,85,82,100,67,73,77,0]
    casa_decimal  = lambda nota: nota // 10 * 10 
    histograma    = Counter(casa_decimal(nota) for nota in notas)
    plotagem.bar([x - 4 for x in histograma.keys()],           # shift each bar to the left by 4
            histograma.values(),                               # da para cada barra sua altura correta
            8)                                                 # da para cada barra a largura de 8
    plotagem.axis([-5, 105, 0, 5])                             # eixo x vai de -5 a 105,
                                                               # eixo y vai de  0 a 5
    plotagem.xticks([10 * contador for contador in range(11)]) # rotulos do eixo x em 0, 10, ..., 100
    plotagem.xlabel("Casa decimal das notas")
    plotagem.ylabel("Numero de estudantes")
    plotagem.title("Distribuicao dos alunos nas casas decimais das notas")
    plotagem.show()
	
def grafico_eixo_y_ilusorio(plt, mislead=True):
    mentions = [500, 505]
    years = [2013, 2014]
    plt.bar([2012.6, 2013.6], mentions, 0.8)
    plt.xticks(years)
    plt.ylabel("# of times I heard someone say 'data science'")
    # if you don't do this, matplotlib will label the x-axis 0, 1
    # and then add a +2.013e3 off in the corner (bad matplotlib!)
    plt.ticklabel_format(useOffset=False)
    if mislead:
        # misleading y-axis only shows the part above 500
        plt.axis([2012.5,2014.5,499,506])
        plt.title("Look at the 'Huge' Increase!")
    else:
        plt.axis([2012.5,2014.5,0,550])
        plt.title("Not So Huge Anymore.")       
    plt.show()

def grafico_muitas_linhas(plt):
    variance     = [1,2,4,8,16,32,64,128,256]
    bias_squared = [256,128,64,32,16,8,4,2,1]
    total_error  = [x + y for x, y in zip(variance, bias_squared)]
    xs = range(len(variance))
    # we can make multiple calls to plt.plot 
    # to show multiple series on the same chart
    plt.plot(xs, variance,     'g-',  label='variance')    # green solid line
    plt.plot(xs, bias_squared, 'r-.', label='bias^2')      # red dot-dashed line
    plt.plot(xs, total_error,  'b:',  label='total error') # blue dotted line
    # because we've assigned labels to each series
    # we can get a legend for free
    # loc=9 means "top center"
    plt.legend(loc=9)
    plt.xlabel("model complexity")
    plt.title("The Bias-Variance Tradeoff")
    plt.show()

def grafico_pontos_de_dispersao(plt):
    friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    plt.scatter(friends, minutes)
    # label each point
    for label, friend_count, minute_count in zip(labels, friends, minutes):
        plt.annotate(label,
                     xy=(friend_count, minute_count), # put the label with its point
                     xytext=(5, -5), # but slightly offset
                     textcoords='offset points')

    plt.title("Daily Minutes vs. Number of Friends")
    plt.xlabel("# of friends")
    plt.ylabel("daily minutes spent on the site")
    plt.show()

def make_chart_scatterplot_axes(plt, equal_axes=False):
    test_1_grades = [ 99, 90, 85, 97, 80]
    test_2_grades = [100, 85, 60, 90, 70]
    plt.scatter(test_1_grades, test_2_grades)
    plt.xlabel("test 1 grade")
    plt.ylabel("test 2 grade")
    if equal_axes:
        plt.title("Axes Are Comparable")
        plt.axis("equal")
    else:
        plt.title("Axes Aren't Comparable")
    plt.show()

def make_chart_pie_chart(plt):
    plt.pie([0.95, 0.05], labels=["Uses pie charts", "Knows better"])
    # make sure pie is a circle and not an oval
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    #grafico_linha_simples(plt)
    #grafico_barras_simples(plt)
    grafico_histograma(plt)
    #grafico_eixo_y_ilusorio(plt, mislead=True)
    #grafico_eixo_y_ilusorio(plt, mislead=False)
    #grafico_muitas_linhas(plt)
    #grafico_pontos_de_dispersao(plt)
    #make_chart_scatterplot_axes(plt, equal_axes=False)
    #make_chart_scatterplot_axes(plt, equal_axes=True)
    #make_chart_pie_chart(plt)
	