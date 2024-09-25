'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro
informado. Por exemplo: 127 -> 721.
'''

def reverso (numero):
    return str(numero [::-1 ])

numero = str(input('informe um numero: ')) #.strip()
print('-='*20)
print(f'o numero informado foi: {numero}')
print(f'inverso fica: {reverso(numero)}')
    
    
