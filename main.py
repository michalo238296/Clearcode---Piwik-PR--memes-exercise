def calculate(usb_size, memes):
    n = len(memes)
    max_size = usb_size * 1024
    titles = [k[0] for k in memes]
    w = [k[1] for k in memes]
    v = [k[2] for k in memes]
    backpack = set()
    table = [[0 for weights in range(max_size + 1)] for memes in range(n)]
    for i in range(max_size + 1):
        if w[0] > i:
            table[0][i] = 0
        else:
            table[0][i] = v[0]
    for i in range(1, n):
        for j in range(max_size + 1):
            if w[i] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - w[i]] + v[i])
    x = n - 1
    y = max_size
    max_price = table[x][y]
    temp = table[x][y]
    while temp != 0:
        if x == 0:
            backpack.add(titles[x])
            temp = 0
        if temp == table[x - 1][y]:
            x -= 1
        else:
            backpack.add(titles[x])
            y = y - w[x]
            x = x - 1
            temp = table[x][y]
    return (max_price, backpack)


def main():
    memes = [('rollsafe.jpg', 202, 6),
             ('rollsafe1.jpg', 102, 16),
             ('rollsafe2.jpg', 700, 56),
             ('sad_pepe_compilation.gif', 410, 10),
             ('sad_pepe_compilation1.gif', 410, 30),
             ('sad_pepe_compilation2.gif', 110, 2),
             ('yodeling_kid.avi', 605, 12),
             ('yodeling_kid1.avi', 150, 40)
             ]
    print(calculate(1, memes))


main()
