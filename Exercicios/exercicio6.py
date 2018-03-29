#Exercício 1
"""
Escreva um programa calculadora (que faz apenas uma operação, por enquanto).
O programa deve receber 3 valores de entrada separadamente, em ordem:
- primeiro valor (numérico, podendo ser int ou float)
- operador (string, que pode ser *asterisco*, *-*, *+* ou */*)
- segundo valor (numérico, podendo ser int ou float)

Em posse dos valores de entrada, o programa deve realizar a operação adequada e escrever o resultado na tela
Exemplo de execução:
> python calculadora.py
> Digite o primeiro valor: 2
> Digite o operador: +
> Digite o segundo valor: 5
> Resultado: 7
"""
question = 'Qual número você deseja inserir?'
value1 = float(input(question))

op = input('Qual operação vocês deseja fazer?')

value2 = float(input(question))
result = 0 


if op == '+':
    result = value1 + value2 
elif op == '-':
    result = value1 - value2
elif op == '*':
    result = value1 * value2
elif op == '/':
    if value2 == 0.0:
        print ('É impossível dividir por 0, krido')
    else:
        result = value1 / value2
else: 
    print('Operador inválido')

print('resultado: ', result )