'''
FAÇA UM PROGRAMA QUE CONVERTA DA NOTAÇÃO DE 24 HORAS PARA A NOTAÇÃO DE 12HORAS. POR EXEMPLO, O PROGRAMA DEVE CONVERTER 14:25 EM 2:25PM.
A ENTRADA É DADA EM DOIS INTEIROS DEVe HAVER PELO MENOS DUAS FUNÇÕES: UMA PARA FAZER A CONVERSÃO E UMA PARA A SAIDA. REGISTRE A
INFORMAÇÃO A.M / PM. COMO UM VALOR 'A' PARA A.M E 'P' PARA P.M. ASSIM, A FUNÇÃO PARA EFETUAR AS CONVERSÕES TERÁ UM PARAMETRO 
FORMAL PARA REGISTRAR SE É A.M OU P.M. INCLUA UM LOOP QUE PERMITA QUE O UNITARIO REPITA ESSE CALCULO PARA NOVOS VALORES DE ENTRADA
TODAS AS VEZES QUE DESEJAR.

'''
#TODO IF ELIFE ELSE TEM QUE TEM QUE TER UM RETURN
#FUNÇÃO TEM QUE ESTAR DENTRO DA VARIAVEL
#VARIAVEL DENTRO DO PRINT
#convertendo a hora

# horas = int(input('diga a hora: '))
# minutos = int(input('e qual é os minutos: '))

# def converte_hora (horas):
#     return (horas - 12)
    
# def imprime_horas (horas,minutos):
#     if(horas <= 12):
#         print(horas,minutos,'am')
#     else:
#         print(converte_hora(horas), minutos, 'pm')
    
# # imprime_horas(horas,minutos)

# def main():
#     horas = int(input('diga a hora: '))
#     minutos = int(input('e qual é os minutos: '))

# main()
    
def converte (horario, minutos):
    if horario > 12:
        horario = horario - 12
        # periodo = 'PM'
        print(f' {horario} : {minutos} pm')
    elif horario == 0:
        horario = 12
        print(f'{horario} : {minutos} AM')

    else:
         print(f'{horario} : {minutos} AM')
    
def main():
   while True: 
        
        horario = int(input(' infome a horas : '))
        minutos = int(input('E infome os minutos: '))
        
        if minutos > 59:
            minutos = minutos - 59
            periodo2 = 'AM'
        
        if horario == 25 or horario > 24:
            print('hora invalida')
            print('programa finalizado')
            break
        
        converte(horario,minutos)
    
main()
     


