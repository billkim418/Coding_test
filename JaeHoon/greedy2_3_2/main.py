n,m,k = map(int, input().split())
data = list(map(int, input().split()))
result, count = 0, 0
data.sort()
print(data)

while count < m:
    if count%(k+1) == 0:
        result += data[-2]
        count += 1
    else:
        result += data[-1]
        count += 1
print(result)