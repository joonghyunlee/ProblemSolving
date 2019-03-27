class Solution(object):
    def simplifyPath(self, path):
        dirs = path.split('/')
        res = []
        for d in dirs:
            if d == '..':
                if res:
                    res.pop()
            elif d == '.':
                continue
            elif not d:
                continue
            else:
                res.append(d)
        if not res:
            res.append('')
            res.append('')
        else:
            res.insert(0, '')
        return '/'.join(res)


if __name__ == '__main__':
    s = Solution()
    r = s.simplifyPath('/a/b/c')
    print r
    r = s.simplifyPath('/../')
    print r
    r = s.simplifyPath('/home//foo/')
    print r
    r = s.simplifyPath('/home/./foo/')
    print r
    r = s.simplifyPath('/home/../foo/')
    print r
    r = s.simplifyPath('/a/../..b/../c//.//')
    print r
    r = s.simplifyPath('/a//b////c/d//././/..')
    print r
