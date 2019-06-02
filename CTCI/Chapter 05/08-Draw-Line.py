def drawLine(screen, width, x1, x2, y):
    height = len(screen) // (width // 8)
    iy = (width // 8) * (height - y - 1)

    ix1, ix2 = x1 // 8, x2 // 8
    bx1 = (1 << (8 - (x1 % 8))) - 1
    bx2 = 0b11111111 ^ ((1 << (7 - (x2 % 8))) - 1)

    for i in range(ix2 - ix1 - 1):
        screen[iy + ix1 + 1 + i] = 0b11111111

    if x1 != x2:
        screen[iy + ix1] = bx1
        screen[iy + ix2] = bx2
    else:
        screen[iy + ix1] = bx1 & bx2


def show(screen, width):
    height = len(screen) // (width // 8)
    for y in range(height):
        print 'y: {}'.format(height - y - 1),
        for x in range(width // 8):
            print '{:08b}'.format(screen[y * (width // 8) + x]),
        print


if __name__ == '__main__':
    screen = [0b0] * (160 // 8 * 120)
    drawLine(screen, 160, 34, 87, 110)
    show(screen, 160)
    drawLine(screen, 160, 45, 45, 109)
    show(screen, 160)
