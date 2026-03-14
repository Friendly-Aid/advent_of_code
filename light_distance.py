def distance(point_1,point_2):
    if len(point_1) != len(point_2):
        raise ValueError('Points must have same dimensions')
    else:
        return sum((point_1[i]-point_2[i])**2 for i in range(len(point_1)))**0.5

class UnionFind:
    def __init__(self,boxes):
        n=len(boxes)
        self.boxes=boxes
        self.parents = [i for i in range(n)]
        self.size = [1]*n
    
    def find_root(self,x):
        if self.parents[x] != x:
            self.parents[x] = self.find_root(self.parents[x])
        return self.parents[x]
    
    def union(self,x,y):
        px,py = self.find_root(x),self.find_root(y)
        if px==py:
            return
        
        if self.size[px] < self.size[py]:
            px,py=py,px
        
        self.parents[py]=px
        
        self.size[px]+=self.size[py]
        if self.size[px]==len(self.boxes):
            print(self.boxes[x][0]*self.boxes[y][0])
            exit()

with open('boxes.txt','r') as f:
    boxes=[eval(f'({spot})') for spot in f.read().strip().split('\n')]

num_boxes=len(boxes)

distances=[]

for i in range(0,num_boxes):
    for j in range(i+1,num_boxes):
        dist=distance(boxes[i],boxes[j])
        distances.append((dist,i,j))

distances=sorted(distances,key=lambda x:x[0])
Union=UnionFind(boxes)

for dist,x,y in distances:
    Union.union(x,y)