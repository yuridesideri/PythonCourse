#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.




exp = input('Digite uma expressão matemática qualquer que use parênteses: ')

result = 'corretos'
parent = 0

for count, n in enumerate(exp):
    if n == '(':
        parent += 1
    
    if n == ')':
        parent -= 1
    
    if parent < 0:
        result = 'errados'
        break

print(f'A sua expressão está com os parênteses {result}')

