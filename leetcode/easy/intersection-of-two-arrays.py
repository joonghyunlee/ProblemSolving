class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1, s2 = set(nums1), set(nums2)
        return [n for n in s1 if n in s2]


if __name__ == '__main__':
    s = Solution()
    r = s.intersection([1, 2, 2, 1], [2, 2])
    print r
    r = s.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    print r
