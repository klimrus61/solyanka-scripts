class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        cheacked = set()
        res = 0
        for i in range(len(mat)):
            if sum(mat[i]) == 1:
                inx = mat[i].index(1)
                if inx not in cheacked and sum(mat[j][inx] for j in range(len(mat))) == 1:
                    res += 1
                cheacked.add(inx)
        return res
