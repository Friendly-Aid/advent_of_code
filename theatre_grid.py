from shapely.geometry import Polygon

with open('theatre_floor.txt','r') as f:
    points = [tuple(map(int,point.split(','))) for point in f.read().strip().split('\n')]

floor = Polygon(points)

best_size=0
for i in range(len(points)):
    for j in range(i+1,len(points)):
        size = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
        if size > best_size:
            rect=Polygon([points[i],(points[i][0],points[j][1]),points[j],(points[j][0],points[i][1])])
            if floor.contains(rect):
                best_size=size
                
print(best_size)