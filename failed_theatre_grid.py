"""def print_grid(safe_points):
    width = 1
    height = 1
    grid = [['.']]
    for point in safe_points:
        while height < (point[1] + 1):
            grid.append(['.'] * width)
            height += 1
        while width < (point[0] + 1):
            for i in range(height):
                grid[i].append('.')
            width += 1
        grid[point[1]][point[0]] = 'X'

    for line in grid:
        print(''.join(line))
    print()


def right_turn(Point_A,Point_B,Point_C):
    if Point_A[0] == Point_B[0]:
        if Point_A[1] > Point_B[1]:
            Y = '>'
            result='up'
        else:
            Y = '<'
            result='down'
        if Point_B[0] > Point_C[0]:
            X = '>'
        else:
            X = '<'
    else:
        if Point_A[0] > Point_B[0]:
            X = '>'
            result='left'
        else:
            X = '<'
            result='right'
        if Point_C[1] > Point_B[1]:
            Y = '>'
        else:
            Y = '<'
    if X!=Y:
        return result
    else:
        return False


with (open('theatre_floor.txt','r') as f):
    points = [tuple(map(int,point.split(','))) for point in f.read().strip().split('\n')]

n=len(points)
unsafe=set()
edge=set()
safe=set()
fill=None
fill_point=points[0]

for i in range(1,len(points)):
    Point_A=points[i-1]
    Point_B=points[i%n]
    Point_C=points[(i+1)%n]
    if Point_A[0] != Point_B[0]:
        y=Point_A[1]
        X_num = 1 if Point_A[0] < Point_B[0] else -1
        for x in range(Point_A[0],Point_B[0]+X_num,X_num):
            edge.add((x,y))
    else:
        x=Point_A[0]
        Y_num = 1 if Point_A[1] < Point_B[1] else -1
        for y in range(Point_A[1],Point_B[1]+Y_num,Y_num):
            edge.add((x,y))
    
    turn=right_turn(Point_A,Point_B,Point_C)
    
    if turn:
        if Point_B in safe:
            if turn=='up':
                X_num = 1 if Point_B[0] < Point_C[0] else -1
                for x in range(Point_B[0],Point_C[0],X_num):
                    y=Point_B[1]+1
                    while (x,y) in safe and (x,y) not in edge:
                        safe.remove((x,y))
                        unsafe.add((x, y))
                        y+=1
            elif turn=='down':
                X_num = 1 if Point_B[0] < Point_C[0] else -1
                for x in range(Point_B[0],Point_C[0],X_num):
                    y=Point_B[1]-1
                    while (x,y) in safe and (x,y) not in edge:
                        safe.remove((x,y))
                        unsafe.add((x, y))
                        y-=1
            elif turn=='left':
                Y_num = 1 if Point_B[1] < Point_C[1] else -1
                for y in range(Point_B[1],Point_C[1],Y_num):
                    x=Point_B[0]-1
                    while (x,y) in safe and (x,y) not in edge:
                        safe.remove((x,y))
                        unsafe.add((x, y))
                        x-=1
            else:
                Y_num = 1 if Point_B[1] < Point_C[1] else -1
                for y in range(Point_B[1],Point_C[1],Y_num):
                    x=Point_B[0]+1
                    while (x,y) in safe and (x,y) not in edge:
                        safe.remove((x,y))
                        unsafe.add((x, y))
                        x+=1
        else:
            X_num=1 if fill_point[0] < Point_B[0] else -1
            for x in range(fill_point[0],Point_B[0]+X_num,X_num):
                Y_num=1 if fill_point[1] < Point_B[1] else -1
                for y in range(fill_point[1],Point_B[1]+Y_num,Y_num):
                    if (x,y) not in unsafe:
                        safe.add((x,y))
    else:
        fill_point=Point_B

print_grid(safe)"""

def flood_fill(edge,height,width,point):
    filled=set()
    check=[point]
    while len(check)>0:
        current=check.pop()
        if current in filled or current in edge:
            continue
        
        filled.add(current)
        
        x,y=current
        if x+1 < width:
            check.append((x+1,y))
        if x-1>-1:
            check.append((x-1,y))
        if y+1 < height:
            check.append((x,y+1))
        if y-1>-1:
            check.append((x,y-1))
    
    return filled
    
def print_grid(points,height,width):
    grid = [['.']*width for i in range(height)]
    for point in points:
        grid[point[1]][point[0]] = 'X'

    for line in grid:
        print(''.join(line))
    print()


def edges(points,offset):
    edge = set()
    sizes = {}
    prev_points = {points[-1]}
    prev_point = points[-1]
    height = prev_point[1] + (offset * 2)
    width = prev_point[0] + (offset * 2)
    
    for point in points:
        if point not in prev_points:
            for prev in prev_points:
                size=(abs(point[1]-prev[1])+1)*(abs(point[0]-prev[0])+1)
                if size not in sizes:
                    sizes[size]=[(point,prev)]
                else:
                    sizes[size].append((point,prev))
    
        X_num=1
        Y_num=1
        if point[0] == prev_point[0]:
            if point[1] > prev_point[1]:
                if point[1]+(offset*2) > height:
                    height=point[1]+(offset*2)
                Y_num = 1
            else:
                if prev_point[1]+(offset*2) > height:
                    height=prev_point[1]+(offset*2)
                Y_num = -1
        else:
            if point[0] > prev_point[0]:
                if point[0]+(offset*2) > width:
                    width=prev_point[0]+(offset*2)
                X_num = 1
            else:
                if prev_point[0]+(offset*2) > width:
                    width=prev_point[0]+(offset*2)
                X_num = -1
        
        for x in range(prev_point[0]+offset,point[0]+offset+X_num,X_num):
            for y in range(prev_point[1]+offset,point[1]+offset+Y_num,Y_num):
                edge.add((x,y))
        
        prev_points.add(point)
        prev_point=point
    
    width+=offset
    height+=offset
    
    return height,width,edge,sizes


with (open('theatre_floor.txt','r') as f):
    points = [tuple(map(int,point.split(','))) for point in f.read().strip().split('\n')]

height,width,edge,sizes=edges(points,1)

print_grid(edge,height,width)

filled=flood_fill(edge,height,width,(0,0))

print_grid(filled,height,width)

def check(edges_1,edges_2):
    for point in edges_1:
        if point in edges_2:
            return False
    return True

for size in sorted(sizes.keys(),reverse=True):
    for points in sizes[size]:
        check_points=[points[0],(points[0][0],points[1][1]),points[1],(points[1][0],points[0][1])]
        _,_,rect,_=edges(check_points,1)
        if check(rect,filled):
            print(size,points)
            exit()