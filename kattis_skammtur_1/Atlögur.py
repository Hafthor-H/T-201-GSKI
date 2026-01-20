number_of_knights = int(input())
knights = {}
winner = False

for i in range(number_of_knights):
    health, streangth = input().split()
    knights[i+1] = (health, streangth)

while not winner:
    knight = 