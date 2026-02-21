with open('food_stuffs.txt', 'r') as f:
    ranges,foods=f.read().strip().split('\n\n')
    ranges=sorted([list(map(int,r.split('-'))) for r in ranges.split('\n')])
    merged=[ranges[0]]
    for r in ranges[1:]:
        if r[0] <= merged[-1][1]+1:
            merged[-1][1]=max(r[1], merged[-1][1])
        else:
            merged.append(r)
    foods=map(int,foods.split('\n'))
    total=0
    for nums in merged:
        total+=nums[1]-(nums[0]-1)
    print(total)