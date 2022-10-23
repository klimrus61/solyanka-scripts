def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    result = []
    for number in range(a, b+1):
        pow_sum = 0
        for i, digit in enumerate(str(number),1):
            pow_sum += int(digit)**i
        if pow_sum == number:
            result.append(number)
    return result
    