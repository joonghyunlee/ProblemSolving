class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'

        st = []
        for n in num:
            while st and st[-1] > n and k > 0:
                st.pop()
                k -= 1
            st.append(n)

        while k > 0:
            st.pop()
            k -= 1

        for i in range(len(st)):
            if st[i] != '0':
                break
        return ''.join(st[i:]) if i < len(st) else '0'


if __name__ == '__main__':
    s = Solution()
    r = s.removeKdigits('9', 1)
    print r
