class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        ans = 0
        import collections
        cmap = collections.Counter(chars)
        for word in words:
            wmap = collections.Counter(word)
            if all(k in cmap and cmap[k] >= v for k, v in wmap.iteritems()):
                ans += len(word)
        return ans

    def countCharacters2(self, words, chars):
        ans = 0
        cmap = {c: chars.count(c) for c in set(chars)}
        for word in words:
            ans += len(word)
            for w in set(word):
                if not (w in cmap and word.count(w) <= cmap[w]):
                    ans -= len(word)
                    break
        return ans


if __name__ == '__main__':
    s = Solution()
    words = ["cat","bt","hat","tree"]
    r = s.countCharacters(words, "atach")
    print r
    r = s.countCharacters2(words, "atach")
    print r
    words = ["hello","world","leetcode"]
    r = s.countCharacters(words, "welldonehoneyr")
    print r
    r = s.countCharacters2(words, "welldonehoneyr")
    print r