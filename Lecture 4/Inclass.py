# class Solution:
#     def prefSum(self, arr):
#         prefixSum=[]
#         sum=0
#         for i in range(len(arr)):
#             sum+=arr[i]
#             prefixSum.append(sum)
#         return prefixSum


# class Solution:
#     def prefSum(self, arr):
#         prefixSum=[]
#         prefixSum.append(arr[0])
#         sum=0
#         for i in range(1,len(arr)):
#             # sum+=arr[i]
#             prefixSum.append(prefixSum[i-1]+arr[i])
#         return prefixSum
# solution=Solution()
# print(solution.prefSum([0,1,2,3,4,5]))


# Euillibrium point 

# Brute Force

# class Solution:
#     def findEquilibrium(self, arr):
        
#         for i in range(1,len(arr)-1):
#             sum_l=0
#             sum_r=0
#             for j in range(0,i):
#                 sum_l+=arr[j]
#             for k in range(i+1,len(arr)):
#                 sum_r+=arr[k]
#             if sum_l==sum_r:
#                 return i
                
#         return -1

# Optimal Solution (Using prefix sum)

# class Solution:
#     def findEquilibrium(self, arr):
        
#         # Make Prefix Array

#         prefix=[]
#         prefix.append(arr[0])
#         for i in range(1,len(arr)):
#             prefix.append(prefix[i-1]+arr[i])
#         # print(prefix[0])
#         # return prefix

#         # Make Suffix Array

#         suffix=[0]*(len(arr))
#         # print(suffix)
#         suffix[len(suffix)-1]=arr[len(arr)-1]
#         # print(suffix)
#         for i in range(len(arr)-2,-1,-1):
#             suffix[i]=suffix[i+1]+arr[i]
#         # print(suffix[0])
#         # return suffix

#         lsum=0
#         rsum=0
        
#         for i in range(0,len(arr)-1):
#             # if i==0 and suffix[i]==0:
#             #     return i
#             lsum=prefix[i-1]
#             rsum=suffix[i+1]
#         # print(lsum)
#         # print(rsum)
#             if lsum==rsum:
#                 return i
        
#         return -1

# soln=Solution()
# print(soln.findEquilibrium([-7, 1, 5 ,2 ,-4, 3, 0]))

# Brute Force - computing all the subarray sums
arr = [1,-3,5,2]

all_sums = []

ending_here = []

for num in arr:

    new_ending = []

    for s in ending_here:
        new_ending.append(s + num)

    new_ending.append(num)

    ending_here = new_ending

    all_sums.extend(ending_here)

    print(new_ending)
    print(ending_here)
    print(all_sums)

print(all_sums)



# Optimized - using hashmap
from collections import defaultdict

class Solution:

    def subCount(self, arr, k):

        freq = defaultdict(int)

        freq[0] = 1

        pref = 0

        count = 0

        for num in arr:

            pref += num

            rem = pref % k

            # Important for languages where % can be negative
            rem = (rem + k) % k

            count += freq[rem]

            freq[rem] += 1

        return count