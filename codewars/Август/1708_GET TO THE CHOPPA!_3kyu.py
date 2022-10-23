def chopa(grid, start, end):
    res = [start,]
    i = 0
    j = 0
    while True:
        way = []
        row = grid(i)
        if len(row) >= j:
            if row[j+1] == 0:
                j += 1
                way.append()
            else:
                
    wrong_way = []
    for i, val in enumerate(grid[])
    return





print(chopa(grid=[
    [0, 0, 1, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    ],
    start=(0,0),
    end=(0,3),
))
