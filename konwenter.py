celsjusz = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
fahrenheit = []

print("Tabela Celsjusz")
print(celsjusz)

for x in celsjusz:
  fahrenheit.append(32 + (1.8 * x))

print()
print("Tabela Fahrenheit")
print(fahrenheit)