class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        memo = {word: 1 for word in words}

        for word in sorted(words, key=len):
            for i in range(len(word)):
                if word[:i] + word[i + 1:] in memo:
                    memo[word] = max(memo[word[:i] + word[i + 1:]] + 1,
                                     memo[word])
        return max(memo.values())


if __name__ == '__main__':
    s = Solution()
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    r = s.longestStrChain(words)
    print r
    words = ["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", 
             "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj", "ksqvsq",
             "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"]
    r = s.longestStrChain(words)
    print r
