'''

    终于搞明白一个问题， 矩阵和二维数组是不一样的。 矩阵是一个类，有构造函数。 数组是基本数据结构， 二维就是里面的元素是数组， 三维以此类推。

'''


def transpose(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    R, C = len(A), len(A[0])

    ns = [[None] * R for _ in range(C)]

    for i in range(C):
        for j in range(R):
            ns[i][j] = A[j][i]

    return ns



a = [[1,2],[3,4]]
print(transpose(a))



