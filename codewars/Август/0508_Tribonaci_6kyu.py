def tribonacci(sig, n):
    for i in range(n-3):
        sig.append(sig[i]+sig[i+1]+sig[i+2])
    return sig[:n]
    