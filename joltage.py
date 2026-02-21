with open('gigawatz.txt','r') as f:
    banks=f.read().strip().split('\n')
    answer=0
    for bank in banks:
        num1=0
        num2=0
        for i in bank[:-1]:
            if int(i) > num1:
                num1=int(i)
                num2=0
            elif int(i) > num2:
                num2=int(i)
        if int(bank[-1])>num2:
            num2=int(bank[-1])
        answer+=int(f"{num1}{num2}")
    print(answer)