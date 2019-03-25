class Solution(object):
    def nextGreaterElement1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = []
        for i, n in enumerate(nums1):
            for m in nums2:
                if n == m:
                    ret.append(-1)
                elif len(ret) == i + 1 and m > n:
                    ret[i] = m
                    break
        return ret

    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        mdict = {}
        s = []

        for n in nums2:
            while s and s[-1] < n:
                mdict[s.pop()] = n
            s.append(n)

        ret = []
        for m in nums1:
            ret.append(mdict.get(m, -1))

        return ret



if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    r = s.nextGreaterElement(nums1, nums2)
    print r
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    r = s.nextGreaterElement(nums1, nums2)
    print r
