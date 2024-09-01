# Importado o modulo json para poder importar arquivo json
import json

# Tratamento do arquivo json transformando em dict e armazenando em variavel
with open("faturamento_agosto.json", 'r', encoding='utf8') as file:
        daily_earnings = json.load(file)

# Usando a função min() para verificar o menor valor das chaves do dict daily_earnings
lowest_day = min(daily_earnings, key=daily_earnings.get)
lowest_earning = daily_earnings[lowest_day]
print(f"O menor faturamento do mês foi: {lowest_earning}")

# Usando a função max() para verificar o maior valor das chaves do dict daily_earnings
highest_day = max(daily_earnings, key=daily_earnings.get)
highest_earning = daily_earnings[highest_day]
print(f"O maior faturamento do mês foi: {highest_earning}")

# Usando a função sum() para calcular a soma de todos os valores de daily_earnings, e len() para
# saber o tamanho, e dividindo os dois para chegar na média
total_earning = sum(daily_earnings.values())
total_days = len(daily_earnings)
average_earning = total_earning / total_days

# Rodando um loop for para verificar todos os valores e contar os dias que estão acima da média
count = 0
for days, earning in daily_earnings.items():
    if earning > average_earning:
          count += 1
    days_above_avg = count

print(f"O numero de dias onde o faturamento foi acima da média mensal foi: {days_above_avg}")