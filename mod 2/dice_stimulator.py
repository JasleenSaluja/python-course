#wap to create a function that will generate random 3 dice numbers an if all three match, then
#display "you win" else display "you lose/try again"

import random as rnd
def streak():
    dice=[1,2,3,4,5,6]
    c1=rnd.choices(dice,k=3)
    print(f'c1={c1}')
    if c1[0]==c1[1]==c1[2]:
        return'you win'
    else:
        return'you lose'

msg=streak()
print('rolling the dice...')
print(msg)
