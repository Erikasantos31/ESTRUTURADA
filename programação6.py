'''
Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado.

'''
def inteiro (numero):
    return len(str(numero))

numero = str(input('digite um número: ')).strip()
print(f'esse numero tem {inteiro(numero)} inteiros digitados')