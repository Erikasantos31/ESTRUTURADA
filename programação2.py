'''
FAÇA UM PROGRAMA, COM UMA FUNÇÃO QUE NECESSITA DE ARGUMENTO. A FUNÇÃO RETORNA O VALOR DE CARACTERE 'P', SE SEU ARGUMENTO FOR POSITIVO, 
e 'N', se seu argumento for zero ou negativo
'''
def positivo_ou_negativo(numero):
    if numero > 0:
        return 'P'
      
    else:
        return 'N'

def main():
    print(positivo_ou_negativo(10))
    print(positivo_ou_negativo(0))
    print(positivo_ou_negativo(-99))

main()
