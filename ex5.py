"""
5) Escreva um programa que inverta os caracteres de um string. 

IMPORTANTE: 
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
b) Evite usar funções prontas, como, por exemplo, reverse; 

"""


def main():
    # leitura da string
    str = input("Digite uma string: ")
    # variável da string invertida
    str_inv = ""
    # tamanho da string
    size = len(str)
    # inversão da string, pegando o último caractere e concatenando na variável da string invertida
    while size > 0:
        str_inv += str[size - 1]
        size -= 1
    print(f"\n\nstring original: {str}")
    print(f"string invertida: {str_inv}")


if __name__ == "__main__":
    main()
