import random

results = []
while len(results) <5000:
    valor = random.randrange(1 , 20000)
    results.append(valor)

print(results)

print(len(results))#confirmação que existem 5000 valores
