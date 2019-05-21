class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        st = []
        co = 0
        sub = []
        for c in s:
            if c in '0123456789':
                co *= 10
                co += ord(c) - ord('0')
            elif c == '[':
                st.append(sub)
                sub = []
                st.append(co)
                co = 0
            elif c == ']':
                n = st.pop()
                sub *= n
                prev = st.pop()
                sub = prev + sub
            else:
                sub.append(c)
        return ''.join(sub)


if __name__ == '__main__':
    so = Solution()
    s = '3[a]2[bc]'
    r = so.decodeString(s)
    print(r)
    s = '3[a2[c]]'
    r = so.decodeString(s)
    print(r)
    s = '2[abc]3[cd]ef'
    r = so.decodeString(s)
    print(r)
