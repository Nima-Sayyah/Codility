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
# def logarithmic(n): 
#     result = 0
#     while n > 1: 
#         n //= 2
#         result += 1 
#     return result
# print(logarithmic(9))

# Linear time — O(n)
# def linear(n, A):
#     for i in range(n):
#         if A[i] == 0: 
#             return 0
#     return 1
# print(linear(8,A=[1,2,3,4,5,6,7,7]))

# Quadratic time — O(n2)
# def quadratic(n): 
#     result = 0
#     for i in range(n):
#         for j in range(i, n):
#             result += 1 
#     return result
# print(quadratic(3))

# Linear time — O(n + m)
# def linear2(n, m): 
#     result = 0
#     for i in range(n):
#         result += i
#     for j in range(m): 
#         result += j
#     return result
# print(linear2(2,3))

# Problem: You are given an integer n. Count the total of 1+2+...+n

# Slow solution — time complexity O(n2)
# def slow_solution(n): 
#     result = 0
#     for i in range(n):
#         for j in range(i + 1): 
#             result += 1
#     return result
# print(slow_solution(7))

# Fast solution — time complexity O(n)
# def fast_solution(n): 
#     result = 0
#     for i in range(n):
#         result += (i + 1) 
#     return result
# print(fast_solution(7))

# import pdb; pdb.set_trace()
