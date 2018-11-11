class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        h_idx = 0
        while h_idx <= len(haystack) - len(needle):
            n_idx = 0
            for n in needle:
                if haystack[h_idx + n_idx] == needle[n_idx]:
                    n_idx = n_idx + 1
                else:
                    break

                if n_idx == len(needle):
                    return h_idx

            h_idx = h_idx + 1

        return -1


if __name__ == '__main__':
    s = Solution()
    r = s.strStr('hello', 'll')
    print r
    r = s.strStr('aaaaa', 'bba')
    print r
    r = s.strStr('a', '')
    print r
    r = s.strStr('mississippi', 'issip')
    print r
    r = s.strStr('mississippi', 'issi')
    print r
    r = s.strStr('mississippi', 'pi')
    print r
