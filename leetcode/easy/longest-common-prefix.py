class Solution(object):
    def longestCommonPrefix(self, strs):
        pointer = 0
        prefix = []

        if len(strs) == 0:
            shortest = ""
        else:
            shortest = min(strs, key=len)

        pointer = 0
        while pointer < len(shortest):
            for s in strs:
                if len(prefix) == pointer:
                    prefix.append(s[pointer])

                if prefix[pointer] != s[pointer]:
                    del prefix[pointer]
                    pointer = len(shortest)
                    break

            pointer = pointer + 1

        return "".join(prefix)


if __name__ == '__main__':
    s = Solution()
    r = s.longestCommonPrefix(['flower', 'flow', 'flight'])
    print("'%s'" % r)
    r = s.longestCommonPrefix([])
    print("'%s'" % r)
    r = s.longestCommonPrefix([''])
    print("'%s'" % r)
    r = s.longestCommonPrefix(['a'])
    print("'%s'" % r)
    r = s.longestCommonPrefix(['c', 'c'])
    print("'%s'" % r)
