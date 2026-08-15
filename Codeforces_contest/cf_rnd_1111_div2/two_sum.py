q = int(input())

while q > 0:
    n = int(input())
    arr = list(map(int, input().split()))
    one_count = arr.count(1)
    neg_one_count = n - one_count
    sum = sum(arr)

    if abs(one_count - neg_one_count) & 1 == 0:
        print('yes')
    else:
        print('no')
    q -= 1