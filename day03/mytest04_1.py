for i in range(2, 9 + 1):
    if not (i == 2 or i == 4 or i == 5 or i == 9):
        continue
    for j in range(1, 9 + 1):
        if j == 5:
            continue
        print("{} * {} = {}".format(i, j, i * j))
