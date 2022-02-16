n,m = map(int, input().split())
result = []
for i in range(n):
    data = list(map(int, input().split()))
    result.append(min(data))
result.sort()
print(result[-1])
