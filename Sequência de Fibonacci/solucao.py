num = int(input('Digite um número: '))

a = 0
b = 1
fibonacci = [a, b]
while b <= num:
    a, b = b, a + b
    fibonacci.append(b)

if num in fibonacci:
    print(f'O número {num} pertence à sequência de Fibonacci')
else:
    print(f'O número {num} não pertence à sequência de Fibonacci.')

