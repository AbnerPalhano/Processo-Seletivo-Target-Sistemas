"""
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: 
•	SP – R$67.836,43 
•	RJ – R$36.678,66 
•	MG – R$29.229,88 
•	ES – R$27.165,48 
•	Outros – R$19.849,53 

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  
"""


def main():
    # inicialização de variáveis
    faturamentos = {
        "SP": 67836.43,
        "RJ": 36678.66,
        "MG": 29229.88,
        "ES": 27165.48,
        "Outros": 19849.53,
    }
    # cálculo do valor total de faturamento
    total = sum(faturamentos.values())
    # cálculo da porcentagem de representação de cada estado
    sp = faturamentos["SP"] / total * 100
    rj = faturamentos["RJ"] / total * 100
    mg = faturamentos["MG"] / total * 100
    es = faturamentos["ES"] / total * 100
    outros = faturamentos["Outros"] / total * 100
    print(
        f"Faturamentos (%):\nSP: {sp:.2f}%\nRJ: {rj:.2f}%\nMG: {mg:.2f}%\nES: {es:.2f}%\nOUTROS: {outros:.2f}%"
    )


if __name__ == "__main__":
    main()
