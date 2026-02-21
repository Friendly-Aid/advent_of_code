nearby=lambda x,y:set((x2,y2) for y2 in range(y-(1 if y >= 1 else 0),y+(2 if y < height-1 else 1)) for x2 in range(max(0,x-1),min(width,x+2)) if grid[y2][x2]=='@') - {(x,y)}

with open('TP_data.txt', 'r') as f:
    rolls = 0
    grid = [list(line) for line in f.read().strip().split('\n')]
    height = len(grid)
    width = len(grid[0])
    check = set((x, y) for y in range(height) for x in range(width))

    while len(check) > 0:
        x,y=check.pop()
        if grid[y][x] == '@':
            near=nearby(x,y)
            if len(near) < 4:
                rolls += 1
                grid[y][x] = '.'
                check.update(near)

    print("\n".join([''.join(line) for line in grid]))
    print(rolls)