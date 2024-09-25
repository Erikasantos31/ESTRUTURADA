'''
faça um programa, com um função que necessite de três argumento, e que forneça soma desse três argumento
'''

def soma_tres_numeros(n1, n2, n3):
   print(f'n1={n1}  n2={n2}  n3={3}')
   return n1 + n2 + n3

def main ():
    num1 = int(input('1° numero: '))
    num2 = int(input('2° numero: '))
    num3 = int(input('3° numero: '))

    result = soma_tres_numeros(num1, num2, num3)
    print('resultado = ', result)


main()