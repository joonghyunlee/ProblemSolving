class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum() or s[i] == ' ':
                i += 1
                continue
            elif not s[j].isalnum() or s[j] == ' ':
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


if __name__ == '__main__':
    s = Solution()
    r = s.isPalindrome('A man, a plan, a canal: Panama')
    print r
    r = s.isPalindrome('race a car')
    print r
