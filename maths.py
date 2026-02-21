with open('maths.txt', 'r') as f:
    grid=f.read().split('\n')
    new_grid=[]
    new = []
    skip=False
    for j in range(1, len(grid[0])+1):
        if skip:
            skip=False
            continue
        num=""
        for i in range(len(grid)):
            num+=grid[i][-j] if grid[i][-j] != ' ' else ''
        try:
            int(num)
            new.append(num)
        except:
            new+=[num[:-1],num[-1]]
            new_grid.append(new)
            skip=True
            new=[]
    total=0
    for math in new_grid:
        total+=eval(math[-1].join(math[:-1]))
    print(total)