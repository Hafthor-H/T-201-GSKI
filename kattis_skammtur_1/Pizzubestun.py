number_of_pizzas = int(input())
pizzas = []

for i in range(number_of_pizzas):
    pizza, price = input().split()
    pizzas.append(int(price))

pizzas.sort()
pizzas.reverse()

print(pizzas)

total = 0
for num in range(0, len(pizzas), 2):
    total += pizzas[num]
print(total)