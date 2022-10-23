def expanded_form(num: int) -> str:
    # Получает число и возвращает строку формы "800 + 7 + 3/10 + 4/1000"
    a = str(num).split('.')
    b = ' + '.join([c + '0'*(len(a[0])-i-1) for i, c in enumerate(a[0]) if int(c)!=0])
    c = ' + '.join([c + '/1' + '0'*(i+1) for i, c in enumerate(a[1]) if int(c)!=0])
    return b + ' + ' + c if b else c

# Чужое решение
def expanded_form(num):
    integer_part, fractional_part = str(num).split('.')

    result = [str(int(num) * (10 ** i)) for i, num in enumerate(integer_part[::-1]) if num != '0'][::-1]
    result += [str(num) + '/' + str(10 ** (i + 1)) for i, num in enumerate(fractional_part) if num != '0']

    return ' + '.join(result)

def expanded_form(num):
    xs = str(num).split('.')
    return ' + '.join(
        [f'{x}{"0" * i}' for i, x in enumerate(xs[0][::-1]) if x != '0'][::-1]
        + [f'{x}/{10 ** i}' for i, x in enumerate(xs[1], 1) if x != '0']
    )
