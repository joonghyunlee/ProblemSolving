class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        for c in s:
            v = dic.get(c, 0)
            dic[c] = v + 1
        for c in t:
            v = dic.get(c, 0)
            dic[c] = v - 1

        for v in dic.values():
            if v != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isAnagram('anagram', 'naagram')
    print(r)
    r = s.isAnagram('wwww', 'vvvv')
    print(r)
    r = s.isAnagram('', '')
    print(r)
    r = s.isAnagram('', 'a')
    print(r)
