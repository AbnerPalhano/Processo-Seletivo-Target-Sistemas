"""
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: 
• O menor valor de faturamento ocorrido em um dia do mês; 
• O maior valor de faturamento ocorrido em um dia do mês; 
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal. 

IMPORTANTE: 
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; 
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média; 
"""


def main():
    import os
    import json

    # inicialização de variáveis
    min = 0
    max = 0
    dias_acima_media = 0
    faturamento = {}
    # leitura do arquivo json e armazenamento dos dados em um dicionário
    # uso de os.path garante que o script rode em qualquer sistema operacional
    with open(os.path.join(os.getcwd(), "dados.json"), "r") as file:
        jsonfile = json.load(file)

        for line in jsonfile:
            faturamento[line["dia"]] = line["valor"]
    # cálculo do valor total e da média de faturamento
    total = sum(faturamento.values())
    media = total / len(faturamento)
    # cálculo do menor valor, maior valor e dias com faturamento acima da média
    for dia, valor in faturamento.items():
        if valor < min or min == 0:
            min = valor
        if valor > max:
            max = valor
        if valor > media:
            dias_acima_media += 1

    print(
        f"Menor valor de faturamento: R${min:.2f}\nMaior valor de faturamento: R${max:.2f}\nDias com faturamento acima da média: {dias_acima_media}"
    )


if __name__ == "__main__":
    main()
