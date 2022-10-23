def solution(args):
    a = []
    i = 0
    while i < len(args):
        b = []
        while i < len(args)-1 and args[i]+1 == args[i+1]:
            b.append(args[i])
            i += 1
        if i > 0 and args[i]-1 == args[i-1]:
            b.append(args[i])
            i += 1
        else:
            a.append(str(args[i]))
            i += 1
        if len(b) >= 3:
            a.append(f'{b[0]}-{b[-1]}')
        elif len(b) == 2:
            a.append(str(b[0]))
            a.append(str(b[1])) 
    return ','.join(a)
    
def solutionn(args):
    out = []
    beg = end = args[0]
    
    for n in args[1:] + [""]:        
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
            beg = n
        end = n
    
    return ",".join(out)
print(solutionn([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20])) #'-6,-3-1,3-5,7-11,14,15,17-20'