import sys
input_buffer = sys.stdin.buffer.read()
tokens = iter(input_buffer)

for i in range(len(tokens)):
    print(next(tokens))