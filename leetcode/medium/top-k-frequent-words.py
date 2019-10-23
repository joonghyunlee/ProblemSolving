class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = {}
        for w in words:
            count[w] = count.get(w, 0) + 1

        def comparator(a, b):
            if a[1] > b[1]:
                return -1
            elif a[1] < b[1]:
                return 1
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            return 0

        return list(map(lambda x: x[0],
                        sorted(count.iteritems(), cmp=comparator)[:k]))


if __name__ == '__main__':
    s = Solution()
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    r = s.topKFrequent(words, 2)
    print r
    words = ["the", "day", "is", "sunny", "the",
             "the", "the", "sunny", "is", "is"]
    r = s.topKFrequent(words, 4)
    print r
    words = ["aaa", "aa", "a"]
    r = s.topKFrequent(words, 1)
    print r
    
