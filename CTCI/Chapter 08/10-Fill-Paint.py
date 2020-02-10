def fillPaint(screen, x, y, color):
    if screen[y][x] == color:
        return False

    def helper(screen, x, y, oldColor, newColor):
        lx, ly = len(screen[0]), len(screen)
        if x < 0 or x >= lx or y < 0 or y >= ly:
            return False

        if screen[y][x] == oldColor:
            screen[y][x] = newColor
            helper(screen, x-1, y, oldColor, newColor)
            helper(screen, x, y-1, oldColor, newColor)
            helper(screen, x, y+1, oldColor, newColor)
            helper(screen, x+1, y, oldColor, newColor)

        return True

    return helper(screen, x, y, screen[y][x], color)
