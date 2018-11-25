class Solution(object):
	def containsDuplicate(self, nums):
		nd = {}
		for n in nums:
			v = nd.get(n, None)
			if not v:
				nd[n]=1
			else:
				return True
		return False

if __name__ == '__main__':
	s = Solution()
	r = s.containsDuplicate([1,2,3,1])
	print(r)
	r = s.containsDuplicate([1,2,3,4])
	print(r)
	r = s.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
	print(r)
