# Find F(n) * F(n+1) = prod 
def productFib(prod):
    fib = [0, 1]
    max_f = fib[0]
    while max_f <= prod:
        if fib[-2] * fib[-1] == prod:
            return [fib[-2], fib[-1], True]
        elif fib[-2] * fib[-1] > prod:
            return [fib[-2], fib[-1], False]
        max_f = fib[-2] + fib[-1]
        fib.append(max_f)


productFib(0)

def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]