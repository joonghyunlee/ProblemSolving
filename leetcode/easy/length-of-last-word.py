class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        count = 0
        last = 0
        for c in s:
            if c != ' ':
                count += 1
            else:
                if count != 0:
                    last = count
                count = 0
        if count != 0:
            last = count
        return last


if __name__ == '__main__':
    s = Solution()
    r = s.lengthOfLastWord('Hello World')
    print r
    r = s.lengthOfLastWord('b a ')
    print r
    r = s.lengthOfLastWord('b    a     ')
    print r
    r = s.lengthOfLastWord('a')
    print r
