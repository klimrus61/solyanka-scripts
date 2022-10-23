def zero(ar=0): #your code here
    if ar == 0:
        return '0'
    else:
        return eval('0'+ar)
def one(ar=1): #your code here
    if ar == 1:
        return '1'
    else:
        return eval('1'+ar)
def two(ar=2): #your code here
    if ar == 2:
        return '2'
    else:
        return eval('2'+ar)
def three(ar=3): 
    if ar == 3:
        return '3'
    else:
        return eval('3'+ar)
def four(ar=4):
    if ar == 4:
        return '4'
    else:
        return eval('4'+ar)
def five(ar=5):
    if ar == 5:
        return '5'
    else:
        return eval('5'+ar)
def six(ar=6):
    if ar == 6:
        return '6'
    else:
        return eval('6'+ar)
def seven(ar=7):
    if ar == 7:
        return '7'
    else:
        return eval('7'+ar) 
def eight(ar=8):
    if ar == 8:
        return '8'
    else:
        return eval('8'+ar)
def nine(ar=9): 
    if ar == 9:
        return '9'
    else:
        return eval('9'+ar)

def plus(ar): #your code here
    return f'+{ar}'


def minus(ar): #your code here
    return f'-{ar}'
def times(ar):
    return f'*{ar}' #your code here
def divided_by(ar):
    return f'/{ar}'

print(one(plus(one())))