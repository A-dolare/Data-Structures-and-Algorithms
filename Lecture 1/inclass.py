# def factors(): ------------------------------incorrect
#     n=int(input('plz enter a number'))
#     i=1
#     count=0
#     while i*i<=n: 
#         if n%i==0:
#             count+=2
#             print(i)
#         elif i==n/i:
#             count+=1
#             print(i)
#         i+=1
#     return count

# print(factors())

def factors():
    n = int(input('plz enter a number: '))
    i = 1
    count = 0
    while i * i <= n:
        if n % i == 0:
            print(i)
            if i == n // i:  # Perfect square case
                count += 1
            else:
                print(n // i)  # Print the other factor
                count += 2
        i += 1
    return count

print(factors())   
        
# hi i am 