

# class Solution:
#     def sieve(self):
#         n = int(input())
#         mx = 100005
#         self.spf = [True] * (mx)
#         self.spf[0] = False
#         self.spf[1] = False

#         i = 2
#         while i * i < mx:
#             if self.spf[i]:
#                 j = i * i
#                 # print(i)
#                 while j < mx:
#                     self.spf[j] = False
#                     j += i
#                     # print(j)
#             i += 1
#         self.solve(n)
        

#     def solve(self, n):

#         if n == 1:
#             print(1)
#             print(1)
#         elif n == 2:
#             print(1)
#             print(1, 1, sep = ' ')
#         else:
#             print(2)
#             for i in range(2, n + 2):
#                 if self.spf[i]:
#                     print(2, end = ' ')
#                 else:
#                     print(1, end = ' ')

# soln = Solution()
# soln.sieve()

class Solution:
    mx = 1000000000005
    spf = [i for i in range(mx)]

    for i in range(2, int(mx ** 0.5) + 1):
        for j in range(i * i, mx, i):
            if spf[j] == j:
                spf[j] = i
    

    def t_prime(self):

        n = int(input())
        arr = list(map(int, input().split()))

        for i in range(n):
            p = self.spf[arr[i]]
            if p * p == arr[i] and arr[i] != 1:
                print('YES')
            else:
                print('NO')

soln = Solution()
soln.t_prime()
    

