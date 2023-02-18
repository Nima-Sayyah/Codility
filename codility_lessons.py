# def dominant(n):
#     result = 0
#     for i in range(n):
#         result = i + 1
#     return result
# print(dominant(7))

# #Constant time — O(1).
# def constant(n): 
#     result = n * n
#     return result

#Logarithmic time — O(log n).
def logarithmic(n): 
    result = 0
    while n > 1: 
        n //= 2
        result += 1 
    return result
print(logarithmic(7))

# import pdb; pdb.set_trace()