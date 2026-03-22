from shapely.geometry import Polygon

with open('theatre_floor.txt', 'r') as f:
    points = [tuple(map(int, point.split(','))) for point in f.read().strip().split('\n')]

floor = Polygon(points)
sizes={}
prev_points={points[-1]}
edges=set()
x_sizes=[0,float('inf')]
y_sizes=[0,float('inf')]
for i in range(len(points)):
    if points[i][0]<x_sizes[0]:
        x_sizes[0]=points[i][0]
    elif points[i][0]>x_sizes[1]:
        x_sizes[1]=points[i][1]
    if points[i][1]<y_sizes[0]:
        y_sizes[0]=points[i][1]
    elif points[i][1]>y_sizes[1]:
        y_sizes[1]=points[i][1]
    
    for point in prev_points:
        size=(abs(point[0]-points[i][0])+1)*(abs(point[1]-points[i][1])+1)
        if size not in sizes:
            sizes[size]=[]
        sizes[size].append((point,points[i]))
    prev_points.add(points[i])
    x_iter=1 if points[i-1][0] < points[i][0] else -1
    y_iter=1 if points[i-1][1] < points[i][1] else -1
    for x in range(points[i-1][0],points[i][0]+x_iter,x_iter):
        for y in range(points[i-1][1],points[i][1]+y_iter,y_iter):
            edges.add((x,y))

def box_in_polygon(points,edges):
    check=set()
    point_1,point_2=points
    x_points = sorted([point_1[0], point_2[0]])
    y_points = sorted([point_1[1], point_2[1]])
    if x_points[0]==x_points[1] or y_points[0]==y_points[1]:
        return True, set()
    
    for x in range(x_points[0]+1, x_points[1]):
        if (x, y_points[0]+1) in edges or (x, y_points[1]-1) in edges:
            return False, set()
        if (x, y_points[0]) not in edges:
            check.add((x,y_points[0]))
        if (x, y_points[1]) not in edges:
            check.add((x,y_points[1]))      
    for y in range(y_points[0]+1, y_points[1]):
        if (x_points[0]+1, y) in edges or (x_points[1]-1, y) in edges:
            return False, set()
        if (x_points[0], y) not in edges:
            check.add((x_points[0], y))
        if (x_points[1], y) not in edges:
            check.add((x_points[1], y))
    
    return True, check

for key in sorted(sizes.keys(),reverse=True):
    print(f'checking size {key}')
    for box_points in sizes[key]:
        been=set()
        inside,check=box_in_polygon(box_points,edges)
        while len(check)>0 and inside:
            point=check.pop()
            been.add(point)
            for point in [(point[0]-1,point[1]),(point[0]+1,point[1]),(point[0],point[1]-1),(point[0],point[1]+1)]:
                if point[0] < x_sizes[0]:
                    inside=False
                    break
                elif point[0] > x_sizes[1]:
                    inside=False
                    break
                if points[i][1] < y_sizes[0]:
                    inside=False
                    break
                elif points[i][1] > y_sizes[1]:
                    inside=False
                    break
                if point in edges or point in been:
                    continue
                else:
                    check.add(point)
        
        if inside:
            print(key)
            exit()