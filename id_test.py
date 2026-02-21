ranged=lambda x: list(map(int,x.split('-')))
with open('ids.txt','r') as f:
    ranges=map(ranged,f.read().split(','))
    answer=0
    for r in ranges:
        r[1]+=1
        for i in range(*r):
            val=str(i)
            pattern=val[0]
            for j in range(1,int(len(val)/2)):
                reps=len(val)/len(pattern)
                if reps%1==0:
                    if val[j:] == pattern*int(reps-1):
                        answer+=int(val)
                        break
                pattern=pattern+val[j]
    print(answer)