def calculate(usb_size, memes):
    n = len(memes)  # n-number of all memes
    max_size = usb_size * 1024  # max_size - capacity of pendrive
    titles = [k[0] for k in memes]  # list of meme names
    w = [k[1] for k in memes]  # list of memes weights
    v = [k[2] for k in memes]  # list of memes values
    backpack = set()
    table = [[0 for weights in range(max_size + 1)] for memes in range(n)]  # creating table for value storage

    for i in range(max_size + 1):  # fill fisrt row of array separately
        if w[0] > i:
            table[0][i] = 0
        else:
            table[0][i] = v[0]
    for i in range(1, n):  # fill table with values
        for j in range(max_size + 1):
            if w[i] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = max(table[i - 1][j], table[i - 1][j - w[i]] + v[i])
    x = n - 1
    y = max_size
    max_price = table[x][y]  # maximum sum of values
    temp = table[x][y]
    while temp != 0:  # reading from table which memes are part of solution
        if x == 0:  # if we re on the top of table, take value and break the loop
            backpack.add(titles[x])
            break
        if temp == table[x - 1][y]:
            x -= 1
        else:
            backpack.add(titles[x])
            y = y - w[x]
            x = x - 1
            temp = table[x][y]
    return (max_price, backpack)
