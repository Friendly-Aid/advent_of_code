timelines={}
def timeline(grid,pos):
    global timelines
    
    x,y=pos
    height=len(grid)
    total=0
    for temp_y in range(y+1,height):
        if grid[temp_y][x]=='^':
            if (x,temp_y) in timelines:
                return timelines[(x,temp_y)]
            total+=timeline(grid,(x-1,temp_y))
            total+=timeline(grid,(x+1,temp_y))
            timelines[(x,temp_y)]=total
            return total
    return 1

with open('tachyon_grid.txt', 'r') as f:
    grid=f.read().split('\n')

start=(grid[0].index('S'),0)
print(timeline(grid,start))