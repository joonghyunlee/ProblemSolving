def parentheses(n):
    def helper(n):
        if n == 1:
            return {"()"}

        items = set()
        for case in helper(n - 1):
            items.add("(" + case + ")")
            items.add("()" + case)
            items.add(case + "()")

        return items
    return list(helper(n))


def parentheses2(n):
    def helper(items, item, left, right, i):
        if left < 0 or right < left:
            return
        elif left == 0 and right == 0:
            items.append(item[:])
        else:
            item[i] = "("
            helper(items, item, left - 1, right, i + 1)
            item[i] = ")"
            helper(items, item, left, right - 1, i + 1)

    items, item = [], [None] * (2 * n)
    helper(items, item, n, n, 0)
    return [''.join(item) for item in items]


if __name__ == '__main__':
    print parentheses(3)
    print parentheses2(3)