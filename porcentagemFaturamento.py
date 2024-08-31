import matplotlib.pyplot as plt

def calcular_percentuais(faturamento):
    total = sum(faturamento.values())
    percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}
    return percentuais

def main():
    faturamento = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53
    }
    percentuais = calcular_percentuais(faturamento)
    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

    plot_percentuais(percentuais)

def plot_percentuais(percentuais):
    estados = list(percentuais.keys())
    valores = list(percentuais.values())
    plt.pie(valores, labels=estados, autopct='%.2f%%')
    plt.title("Percentual de representação por estado")
    plt.show()

if __name__ == "__main__":
    main()
