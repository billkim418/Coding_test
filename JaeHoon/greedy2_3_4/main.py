# n, k 값 따로 저장
n, k = map(int, input().split())
count = 0

while(n != 1): # 1이 되기 전까지 반복
    if n%k == 0: # n과 k 가 나누어 떨어지는 경우
        n/=k
        count+=1
    else: # 그렇지 않은경우 1빼기
        n-=1
        count +=1
print(count)
