friend_count = int(input())

ages = []
for i in range(friend_count):
    age = int(input())
    ages.append(age)
print(min(ages))