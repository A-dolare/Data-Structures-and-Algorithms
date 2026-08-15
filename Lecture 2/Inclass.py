# ARRAY QUESTIONS

# NOTE : You can and should use a tuple for a fixed-sized array. 

# In fact, tuple is often the preferred choice over 
# list for fixed-size collections because:
# Immutability: Its size and contents cannot be accidentally modified. 
# Memory Efficiency: Tuples use less memory than lists because they don't over-allocate for future growth. 
# Performance: Tuples are slightly faster to create and access due to their fixed size and direct storage of elements. 
    
# 1. REVERSING AN ARRAY

# METHOD : IF WE TAKE LIST AS INPUT INSTEAD OF TUPLE

# def reverse():
#     col=eval(input('plz enter an array'))
#     col=col[::-1]
#     # empty.reverse()
#     return col
# print(reverse())

# def reverse():
#     col=eval(input('plz enter an array'))
#     # col=col[::-1]
#     col.reverse()
#     return col
# print(reverse())

# A. BRUTE FORCE- 

# def reverse():
#     col=eval(input('plz enter an array'))
#     # print(type(col))
#     empty=list()
#     for ind in range(0,len(col)):
#         empty.append(col[len(col)-ind-1])
#     empty=tuple(empty)
#     # print(type(empty))
#     return empty
# print(reverse())


# def reverse():
#     col=eval(input('plz enter an array'))
#     # print(type(col))
#     empty=list()*len(col)
#     for ind in range(0,len(col)):
#         empty.append(col[len(col)-ind-1])
#     empty=tuple(empty)
#     # print(type(empty))
#     return empty
# print(reverse())

# B. OPTIMAL APPROACH

# def reverse():
#     col=tuple(input('plz enter an array'))
#     # print(col)
#     # print(type(col))
#     col=list(col)
#     # print(type(col))
#     for ind in range(0,len(col)//2):
#         temp=col[ind]
#         col[ind]=col[len(col)-ind-1]
#         col[len(col)-ind-1]=temp
#     col=tuple(col)
#     return col
# print(reverse())

# reverse()


# def reverse():
#     col=tuple(input('plz enter an array'))
#     # print(col)
#     # print(type(col))
#     col=list(col)
#     # print(type(col))
#     i=0
#     j=len(col)-1
#     while i<j:
#         temp=col[i]
#         col[i]=col[j]
#         col[j]=temp
#         i+=1
#         j-=1
#     col=tuple(col)
#     return col
# print(reverse())

# reverse()

# 2. REVERSING PART OF AN ARRAY


# def reverse():
#     col=tuple(input('plz enter an array'))
#     # print(col)
#     # print(type(col))
#     col=list(col)
#     # print(type(col))
#     i=(0)+3
#     j=(len(col)-1)-2 # we only wanna reverse a part of the array
#     while i<j:
#         temp=col[i]
#         col[i]=col[j]
#         col[j]=temp
#         i+=1
#         j-=1
#     col=tuple(col)
#     return col
# print(reverse())

# reverse()


# 3. ROTATING THE ARRAY K-TIMES (RIGHT ROTATION)

# A. Brute Force

# def rotate():
#     col=tuple(input('plz enter an array'))
#     k=int(input('plz enter the number of rotations'))
#     k=k%(len(col))
#     # if k==0:
#     #     return col
#     col=list(col)
#     for i in range(0,k):
#         last=col[len(col)-1]
#         for ind in range(0,len(col)-1):
#             col[len(col)-1-ind]=col[len(col)-2-ind]
#         col[0]=last
#     col=tuple(col)
#     return col
# print(rotate())

# B. OPTIMAL SOLUTION 

def reverse(col,lower,upper):
    # print(col)
    # print(type(col))
    # col=list(col)
    # print(type(col))
    while lower<upper:
        temp=col[lower]
        col[lower]=col[upper]
        col[upper]=temp
        lower+=1
        upper-=1
    # col=list(col)
    return col


def rotate():
    col=tuple(input('plz enter an array'))
    k=int(input('plz enter the number of rotations'))
    k=k%(len(col))
    if k==0:
        return col
    col=list(col)
    col=reverse(col,len(col)-k,len(col)-1)
    col=reverse(col,0,len(col)-k-1)
    col=reverse(col,0,len(col)-1)
    col=tuple(col)
    return col

print(rotate())
    