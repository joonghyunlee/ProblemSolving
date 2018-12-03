class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d1 = {}
        for n in nums1:
            v = d1.get(n, None)
            if not v:
                d1[n] = 1
            else:
                d1[n] += 1

        d2 = {}
        for n in nums2:
            v = d2.get(n, None)
            if not v:
                d2[n] = 1
            else:
                d2[n] += 1

        ret = []
        for n in d1.keys():
            if n in d2.keys():
                for i in range(min(d1[n], d2[n])):
                    ret.append(n)

        return ret


if __name__ == '__main__':
    s = Solution()
    r = s.intersect([1, 2, 2, 1], [2, 2])
    print r
