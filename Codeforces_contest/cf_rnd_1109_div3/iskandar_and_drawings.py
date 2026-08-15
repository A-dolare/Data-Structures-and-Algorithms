import sys
import math
input_data = sys.stdin.buffer.read()
iter = iter(input_data)
t = int(next(iter))

while t > 0:
    n = int(next(iter))
    s = next(iter)

    if n == s.count('*'):
        print(0)
        t -= 1
        continue

    if n == s.count('#'):
        print(math.ceil(n))
        t -= 1
        continue
    
    left_ind = s.index('*')
    right_ind = s.rindex('*')

    secs = 0

    if left_ind > 2:
        secs += math.ceil(left_ind // 2)
    else:
        secs += 1

    if n - right_ind > 3:
        secs += math.ceil((n - right_ind) // 2)
    else:
        secs += 1

    print(math.ceil(secs // 2))

    t -= 1

    
    