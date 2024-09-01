# Atribuindo os valores a um dict
values = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(values.values())

# Utilizando dict comprehension para calcular a percentagem de cada valor
percentage = {state: (amount / total) * 100 for state, amount in values.items()}

# Mostrando os valores da dict de porcentagens
for state, percentage in percentage.items():
    print(f"{state}: {percentage:.2f}%")