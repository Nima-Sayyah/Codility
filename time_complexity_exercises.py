# #OddOccurrencesInArray
# # Find value that occurs in odd number of elements (55%)(how about if they are 3 same numbers?)
# def unique_numbers(A):
#     result = []
#     for i in A:
#         if A.count(i) == 1:
#             result.append(i)
#     return result
# print(unique_numbers(A=[1,2,3,1,4,4,2,3,5,5,0]))

#TapeEquilibrium
#Minimize the value |(A[0] + ... + A[P-1]) - (A[P] + ... + A[N-1])| ()()
def minimum_difference(A):
    result=list()
    N = 0
    P = [i for i in range(1,len(A))]
    for i in range(len(A)):
        # index = i + i*(i+1)//2
        result.append(abs(result[i]-sum(A[i+1:])))
    return min(result)

print(minimum_difference(A=[3,1,2,4,3]))

# A=[3,1,2,4,3]
# # P = range(len(A))
# print(range(len(A)))
# P = [i for i in range(1,len(A))]
# print(P)
# i=range(len(A))
# print(abs(A[0]-sum(A[0+1:])))
