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


if __name__ == '__main__':
    print permutation('abc')
