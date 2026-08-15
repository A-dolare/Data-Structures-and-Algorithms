
n, q = map(int, input().split())
# print(n, q)

arr = list(map(int, input().split()))
# print(arr)

presum = [0] * n
presum[0] = arr[0]
for i in range(n):
    presum[i] = presum[i - 1] + arr[i]
# print(presum)

for i in range(q):
    a, b = map(int, input().split())
    x = a - 1
    y = b - 1
    
    if x > 0:
        print(presum[y] - presum[x - 1])
    else:
        print(presum[y])
    
    q-=1