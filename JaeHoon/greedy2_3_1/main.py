n = 1760
coin = [500, 100, 50, 10]
result = 0
for coin in coin:
    count = n // coin
    n -= count * coin
    result += count
    count = 0
print(result)
#############################
n = 1760
coin = [500, 100, 50, 10]
for coin in coin:
    count += n // coin
    n %= coin
print(count)
