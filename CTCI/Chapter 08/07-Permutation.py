# abcd O
# aabc X

# Result = []
# abcd => 'a', 'b', 'c', 'd'
# 'a' / 'b', 'c', 'd'


def permutation(message):
    result = []
    cset = set(c for c in message)

    def helper(prefix, length):
        if length == 0:
            result.append(prefix)
            return

        for c in list(cset):
            cset.remove(c)
            helper(prefix + c, length - 1)
            cset.add(c)

    helper('', len(message))
    return result


def permutation2(message):
    from itertools import permutations
    return [''.join(perm) for perm in permutations(list(message), 3)]


def permutation3(message):
    def helper(items):
        if len(items) == 0:
            return []
        elif len(items) == 1:
            return [items]
        perms = []
        for i, item in enumerate(items):
            for p in helper(items[:i] + items[i + 1:]):
                perms.append([item] + p)
        return perms
    
    return [''.join(perm) for perm in helper(list(message))]


def permutation4(message, r):
    def helper(items, r):
        if len(items) == 0:
            return []
        elif len(items) == 1:
            return [items]
        if r == 0:
            return []
        elif r == 1:
            return [[item] for item in items]
        perms = []
        for i, item in enumerate(items):
            for p in helper(items[:i] + items[i + 1:], r - 1):
                perms.append([item] + p)
        return perms
    
    return [''.join(perm) for perm in helper(list(message), r)]


if __name__ == '__main__':
    print permutation('abc')
    print permutation2('abc')
    print permutation3('abc')
    print permutation4('abc', 2)
