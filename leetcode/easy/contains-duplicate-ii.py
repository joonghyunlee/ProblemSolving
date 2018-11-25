class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}
        for i, n in enumerate(nums):
            dis = dic.get(n, None)
            if not dis:
                dic[n] = [i]
            else:
                for d in dis:
                    if i - d <= k:
                        return True
                dis.append(i)
        return False


if __name__ == '__main__':
    s = Solution()
    r = s.containsNearby([1,2,3,1], 3)
    print(r)
    nums = [1,0,1,1]
    r = s.containsNearby(nums, 1)
    print(r)
    nums = [1,2,3,1,2,3]
    r = s.containsNearby(nums, 2)
    print(r)
    nums = [99,99]
    r = s.containsNearby(nums, 2)
    print(r)
