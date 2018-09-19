message = 'it was a cold day in april, clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] += 1

print(count)
