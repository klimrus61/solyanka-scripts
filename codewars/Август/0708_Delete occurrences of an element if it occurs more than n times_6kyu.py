def delete_nth(order,max_e):
    verified_order = []
    count_int = {str(i): 0 for i in order}
    for i in order:
        if count_int[str(i)] < max_e:
            verified_order.append(i)
            count_int[str(i)] += 1
    return verified_order

def delete_nth(order,max_e):
    ans = []
    for o in order:
        if ans.count(o) < max_e: ans.append(o)
    return ans
    
def delete_nth(order, max_e):
    d = {}
    res = []
    for item in order:
      n = d.get(item, 0)
      if n < max_e:
        res.append(item)
        d[item] = n+1
    return res
print(delete_nth([20,43,20,50,20], 2))