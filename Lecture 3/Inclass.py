# ARRAY LEADERS
# A. Brute Force:
# arr=[1,2,48,6,4,1,2,1,2,45,31]
# def leaders(arr):
#     for i in range(len(arr)):
#         lead=True
#         for j in range(i+1,len(arr)):
#             if arr[j]>arr[i]:
#                 lead=False
#                 break
#         if lead:
#             print(arr[i])
        
# leaders(arr)

# B. Optimal Solution

# arr=[100,48,6,4,1,2,1,2,45,31]
# def leaders(arr):
#     maxi=arr[len(arr)-1]
#     ans=[]
#     ans.append(maxi)
#     for i in range(0,len(arr)-1):
#         # print(arr[i],end=' ')
#         if (arr[len(arr)-i-2])>maxi:
#             maxi=(arr[len(arr)-i-2])
#             ans.append(maxi)
#         print(i)
#     return ans
# print(leaders(arr))


# SEGREGATE 0s and 1s:
# A. Brute Force:

# array=[0,1,0,1,1,1,0,0,0,0,0,1]
# def seg(arr):
#     zeros= arr.count(0)
#     for i in range(0,zeros):
#         arr[i]=0
#     for i in range(zeros,len(arr)):
#         arr[i]=1
#     return arr
# print(seg(array))

# B. Optimal Solution
# B1

# array=[0,1,0,1,0,1,1,1,0,0,1,0]
# def seg(arr):
#     arr.sort()
#     return arr
# print(seg(array))

# B2.

# array=[0,1,0,1,0,1,0,1,1,1,1,1,0,0,1]
# def seg(arr):
#     i=0
#     j=len(arr)-1
#     while i<j:
#         # print(i,j)
#         while i<j and arr[i]==0:
#             i+=1
#         while i<j and arr[j]==1:
#             j-=1
#         if arr[i]==1 or arr[j]==0:
#             temp=arr[i]
#             arr[i]=arr[j]
#             arr[j]=temp
#         # print(arr)
#         # print(i,j)
#         if i>j:
#             break
#         # print(i,j)
#     return arr


# print(seg(array))

# Segregating 0s, 1s and 2s
    
# class Solution:
#     def sort012(self, arr):
        
#         l=0
#         m=0
#         h=len(arr)-1
        
#         while m<=h:
#             if arr[m]==0:
#                 temp=arr[m]
#                 arr[m]=arr[l]
#                 arr[l]=temp
#                 l+=1
#                 m+=1
#                 print(m)
#             elif arr[m]==1:
#                 m+=1
#             elif arr[m]==2:
#                 temp=arr[m]
#                 arr[m]=arr[h]
#                 arr[h]=temp
#                 h-=1
#         return arr

# soln=Solution()
# print(soln.sort012([0,1,2,1,0]))


