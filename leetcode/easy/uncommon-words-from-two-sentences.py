class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        mapA, mapB = {}, {}
        for w in A.split():
            mapA[w] = mapA.get(w, 0) + 1
        for w in B.split():
            mapB[w] = mapB.get(w, 0) + 1

        uncommons = []
        for w, freq in mapA.iteritems():
            if mapB.get(w) is None and freq == 1:
                uncommons.append(w)

        for w, freq in mapB.iteritems():
             if mapA.get(w) is None and freq == 1:
                uncommons.append(w)

        return uncommons


if __name__ == '__main__':
    s = Solution()
    r = s.uncommonFromSentences("this apple is sweet", "this apple is sour")
    print r
    r = s.uncommonFromSentences("apple apple", "banana")
    print r