import pandas as pd  # utilizando Pandas

faturamento_mensal = pd.read_json('dados.json')

menor_valor = faturamento_mensal[faturamento_mensal['valor'] > 0]['valor'].min()
maior_valor = faturamento_mensal['valor'].max()
dados_limpo = faturamento_mensal[faturamento_mensal['valor'] > 0]
dias = len(dados_limpo[dados_limpo['valor'] > dados_limpo['valor'].mean()])

print(f'O menor valor de faturamento foi: {menor_valor:.2f}')
print(f'O maior valor de faturamento foi: {maior_valor:.2f}')
print(f'O número de dias com o de faturamento acima da média foram: {dias}')
