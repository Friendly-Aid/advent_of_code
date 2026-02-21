with open('safe_input.txt','r') as f:
    solution=f.read().strip().split('\n')
    answer=0
    pos=50
    for rot in solution:
        hits = 0
        past=pos
        if rot[0] == 'R':
            pos+=int(rot[1:])
        else:
            pos-=int(rot[1:])
            if pos==0:hits+=1
            elif pos<0 and past>0:hits+=1
        hits+=abs(pos)//100
        answer+=hits
        pos%=100
    print(answer)