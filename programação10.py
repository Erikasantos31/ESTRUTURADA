''''
Calculadora. Construa uma função que efetue as 4 operações matemáticas, serão
passados 3 parâmetros, tipo de operação (+,-,* ou /), posteriormente dois valores para
efetuar o cálculo, o return será do resultado da operação.
'''
num = float(input('informe um número: '))
num2 = float(input('informe um outro número: '))
# print('escolha uma operação: {}'.format(operação))
def operação (adição, subtração, multiplicação, divisão):
    if  adição:
        soma = num + num2
        return soma
    
    elif subtração:
        subtração = num - num2
        return subtração
    
    elif multiplicação:
        multiplicação = num * num2
        return multiplicação
    
    elif divisão:
        divisão = num / num2
        return divisão
    
    else:
       #result = 0
        #return result
        print('operação inalidade')

def exibir_resultados(adição, subtração, multiplicação, divisão):
    print('a adição foi: '.fomat(adição))
    print('subtração: '.format(subtração))
    print('multiplicação: '.format(multiplicação))
    print('divisão: '.format(divisão))

def main():
   exibir_resultados == operação

main()