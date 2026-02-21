with open('gigawatz.txt','r') as f:
    banks=f.read().strip().split('\n')
    answer=0
    for bank in banks:
        pos=0
        last=0
        highest=list(map(int,bank[:12]))
        for i in range(1,len(bank)):
            temp=i-(len(bank)-12)
            if temp>pos:
                pos=temp
            for j in range(pos,min(i-last,12)):
                if int(bank[i]) > highest[j]:
                    last=i-j
                    highest=highest[:j]+list(map(int,bank[i:i+(12-j)]))
                    if int(bank[i])==9 and j==pos:
                        pos+=1
                    break
        val=int(''.join(map(str,highest)))
        answer+=val

    print(answer)