import random

august_earnings = {day: random.uniform(1000, 5000) for day in range(1, 32)}

for day, earning in august_earnings.items():
    print(f'"{day}": {earning:.2f},')