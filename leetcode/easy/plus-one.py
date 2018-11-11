class Solution(object):
	def plusOne(self, digits):
		i = len(digits) - 1
		r = 1
		while i >= 0:
			d = digits[i] + r
			if d >= 10:
				r = 1
				d = d - 10
			else:
				r = 0
			digits[i] = d
			i -= 1
		if r > 0:
			digits.insert(0, r)
		return digits
		
		
if __name__ == '__main__':
	s = Solution()
	r = s.plusOne([1, 2, 3, 4])
	print(r)
	r = s.plusOne([1])
	print(r)
	r= s.plusOne([1, 9])
	print(r)
	r = s.plusOne([9,9])
	print(r)