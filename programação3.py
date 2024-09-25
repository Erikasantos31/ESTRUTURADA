'''
faça um programa com uma função chamada somaImposto. A função possui dois parÂmetros formais: taxaImposto,
 que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
 A função 'Altera'o valor de custo para incluir o imposto sobre vendas
'''
#parametros vem antes da função 
def soma_imposto(taxa_imposto, custo):
    valor_imposto = (taxa_imposto / 100) * custo
    novo_valor_custo = valor_imposto + custo
    return novo_valor_custo

def main():
    taxa_imposto = int(input('qual a taxa de imposto? '))
    custo = int(input('qual seria o custo? '))
    
    result = soma_imposto(taxa_imposto, custo)
    print('O NOVO VALOR DA VENDA ', result)

main()    