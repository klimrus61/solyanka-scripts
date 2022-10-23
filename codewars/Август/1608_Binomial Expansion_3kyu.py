import re
from math import factorial as fact
def combinations(n, k):
    return int(fact(n)/(fact(k)*fact(n-k)))
    
def expand(expr):
    a = re.search(r'[+-]?\d*[a-z]\b', expr)[0]
    var = a[-1]
    if a[:-1] == '' or a[:-1] == '+':
        a = 1
    elif a[:-1] in '-':
        a = -1
    else:
        a = int(a[:-1])
    b = int(re.search(r'[-+]?\d+\b', expr)[0])

    n = int(re.search(r'\^\d+', expr)[0][1:])
    res = ''
    for k in range(n+1):
        sub_res = ''
        c = combinations(n=n, k=k)*pow(a, n-k)*pow(b, k)
        if n-k >= 1:
            if int(c) == 1:
                c = ''
            elif int(c) == -1:
                c = '-'
            if n-k >= 2:
                sub_res = str(c) + var + f'^{n-k}'
            else:
                sub_res = str(c) + var
        else:
            sub_res = str(c)
        if k == 0:
            res = sub_res
        else:
            if '-' in sub_res:
                res = res + sub_res
            else:
                res = res + '+' + sub_res 
    return res
        

import re

P = re.compile(r'\((-?\d*)(\w)\+?(-?\d+)\)\^(\d+)')

def expand(expr):
    a,v,b,e = P.findall(expr)[0]
    
    if e=='0': return '1'
    
    o   = [int(a!='-' and a or a and '-1' or '1'), int(b)]
    e,p = int(e), o[:]
    
    for _ in range(e-1):
        p.append(0)
        p = [o[0] * coef + p[i-1]*o[1] for i,coef in enumerate(p)]
    
    res = '+'.join(f'{coef}{v}^{e-i}' if i!=e else str(coef) for i,coef in enumerate(p) if coef)
    
    return re.sub(r'\b1(?=[a-z])|\^1\b', '', res).replace('+-','-')
    
print(expand("(2x+5)^6")) # "x^2+2x+1"))