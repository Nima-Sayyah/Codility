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
    L_index = 0
    R_index = len(A)-1
    
    left_sum = A[L_index]
    right_sum = sum(A[R_index:])
    
    value = list()

    while R_index > 0:
        deduction = abs(left_sum - right_sum)
        if deduction !=0:
            value.append(deduction)
        L_index += 1
        left_sum += A[L_index]
        R_index -= 1

    return min(value)

print(minimum_difference(A=[3,1,2,4,3]))

# A=[3,1,2,4,3]
# # P = range(len(A))
# print(range(len(A)))
# P = [i for i in range(1,len(A))]
# print(P)
# i=range(len(A))
# print(abs(A[0]-sum(A[0+1:])))
