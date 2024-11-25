import numpy as np

#9.7 - Gram Schmidt Procedure

vec1 = np.array([1,1,0])
vec2 = np.array([0,1,1])

def eInnerProduct(vec1, vec2):
    sum = 0
    for i in range(0, len(vec1)):
        sum += vec1[i] * vec2[i]
    return sum

def normFinder(vec1, vec2):
    return np.sqrt(eInnerProduct(vec1, vec2))

def GSProcedure(vecArr):
    e_1 = vecArr[0]/normFinder(vecArr[0], vecArr[0])
    newVecArr = [e_1]

    for j in range(1, len(vecArr)):
        sum = 0
        for i in range(0, j-1):
            sum += normFinder(vecArr[j], newVecArr[i]) * newVecArr[i]

        e_j = (vecArr[j] - sum) / (normFinder(vecArr[j] - sum, vecArr[j] - sum))
        newVecArr.append(e_j)
    
    return newVecArr

print(GSProcedure([vec1, vec2]))