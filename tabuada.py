# TABUADA 

numero = int(input('Digite um número entre 1 e 10: '))

if 1 <= numero <= 10:
    
    print(f'Tabuada de {numero}:')
    
    for num in range(1, 11):
        
        print(f'{numero} X {num} = {numero * num}')
else:
    print('Número inválido. Por favor, digite um número entre 1 e 10.')