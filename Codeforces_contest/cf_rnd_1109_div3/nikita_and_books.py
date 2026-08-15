import sys
input_data = sys.stdin.buffer.read()
tokens = input_data.split()
iter = iter(tokens)
t = int(next(iter))

while t > 0:
    n = int(next(iter))
    # arr = []
    sum = 0
    flag = True
    asc = -1
    for i in range(n):
        num = int(next(iter))
        if num >= asc:
            flag = False
        # arr.append(num)
        asc = num
        sum += num

    if sum >= ((n * (n + 1)) // 2) and flag:
        print('yes')
    else:
        print('no')

    t -= 1