#
# (4, 3) -> (3, 2), (3, 5), (5, 2), (5, 4)


def deployQueen():
    answer = []
    def helper(row, cols, lDiagonals, rDiagonals):
        if row == 8:
            return answer.append([(r, col) for r, col in enumerate(cols)])

        for i in range(8):
            if i in cols or i in lDiagonals or i in rDiagonals:
                continue
            helper(row + 1, cols + [i],
                   [ld-1 for ld in lDiagonals 
                        if ld - 1 >= 0 and ld - 1 < 8] + [i - 1],
                   [rd + 1 for rd in rDiagonals
                        if rd + 1 >= 0 and rd + 1 < 8] + [i + 1])
        return

    helper(0, [], [], [])
    return answer


if __name__ == '__main__':
    print deployQueen()