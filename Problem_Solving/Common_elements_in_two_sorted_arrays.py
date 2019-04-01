A = [1,2,3,4,5]
B = [1,3,5,6,7]

def common_elements(A, B) :
    p1 = 0
    p2 = 0
    result = []
    while p1<A.length and p2<B.length :
        if A[p1] == B[p2] :
            result.add(A[p1])
            p1 += 1
            p2 += 1
        else :
            if A[p1] > B[p2] :
                p2 += 1
            else :
                p1 += 1
    return result

'''By Ankush Chavan'''