class Solution:
    def wordSubsets(self, A: 'List[str]', B: 'List[str]') -> 'List[str]':
        from collections import defaultdict
        bdict = defaultdict(lambda: 0)
        for word in B:
            temp = defaultdict(lambda: 0)
            for c in word:
                temp[c] += 1
            for c in temp.keys():
                bdict[c] = max(bdict[c], temp[c])

        universals = []
        for word in A:
            temp = defaultdict(lambda: 0)
            for c in word:
                temp[c] += 1
            find = True
            for c in bdict.keys():
                if bdict[c] > temp[c]:
                    find = False
                    break
            if find:
                universals.append(word)
        return universals

    def wordSubsets2(self, A: 'List[str]', B: 'List[str]') -> 'List[str]':
        from collections import Counter
        cnt = Counter
        bCnt = cnt()
        for b in B:
            bCnt |= cnt(b)
        return [a for a in A if not (bCnt - cnt(a))]


if __name__ == '__main__':
    s = Solution()
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]
    r = s.wordSubsets(A, B)
    print(r)
    r = s.wordSubsets2(A, B)
    print(r)
