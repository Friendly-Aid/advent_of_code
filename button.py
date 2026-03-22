import time
def shortest_path(presses,buttons):
    original=presses[frozenset()]
    while True:
        new_presses={}
        for path in presses.keys():
            for button in buttons:
                if button not in path:
                    for needed in presses[path]:
                        if needed in button:
                            new_needed=presses[path].symmetric_difference(button)
                            new_path=path.union({button})
                            if new_path == buttons:
                                return
                            if len(new_needed)==0:
                                return {new_path:original}
                            new_presses[new_path]=new_needed
                            break
        presses=new_presses

with open('buttons.txt','r') as f:
    data=f.read().strip().split('\n')

results={}
for button_data in data:
    button_data=button_data.replace(')',',)').split(' ')
    lights=button_data[0].strip('[]')
    lights = {i for i in range(len(lights)) if lights[i] == '#'}
    buttons={frozenset(eval(button)) for button in button_data[1:-1]}
    presses={frozenset():lights}
    answer = shortest_path(presses, buttons)
    if answer:
        results.update(answer)

num=0
for result in results.keys():
    print(result,results[result])
    num+=len(result)

print(num)