class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        s = ['RO']
        vals = preorder.split(',')
        for v in vals:
            if not s:
                return False
            s.pop()
            if v != '#':
                s.append(v + 'R')
                s.append(v + 'L')
        return True if not s else False


if __name__ == '__main__':
    s = Solution()
    preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    r = s.isValidSerialization(preorder)
    print(r)
    preorder = "1,#,#"
    r = s.isValidSerialization(preorder)
    print(r)
