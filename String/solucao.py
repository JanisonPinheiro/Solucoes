palavra = input('Digite uma palavra: ')
nova_palavra = ''

for i in range(len(palavra)-1, -1, -1):
    nova_palavra += palavra[i]

print(f'String original: {palavra}')
print(f'String invertida: {nova_palavra}')
