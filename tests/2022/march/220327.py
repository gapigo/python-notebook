# Making a random system based on time
import datetime
import random

# print(datetime.datetime.now().hour)
# minutes = [i for i in range(0 + 5, 61, 5)]
# print(minutes)

MAX = 0.05
random_chances = {}
minutes = [i for i in range(0 + 5, 61, 5)]
print(minutes)
max_chance = MAX * random.random()
min_chance = max_chance / 1000
len_m = len(minutes)
chances = []
i = 0
increasing_step = (max_chance - min_chance) / len_m
while i < len_m:
    chances.append(min_chance + increasing_step * i)
    i += 1
random.shuffle(chances)
for i, minute in enumerate(minutes):
    random_chances[minute] = chances[i]
print(random_chances)

count = 0

def set_last_minute(minute):
    global minutes, last_minute
    for min in minutes:
        if minute <= min:
            last_minute = min
            break

set_last_minute(datetime.datetime.now().minute)
print(last_minute)

for i in range(100):
    if random.random() < random_chances[last_minute]:
        count += 1
print(count)