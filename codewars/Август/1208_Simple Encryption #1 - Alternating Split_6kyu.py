def decrypt(encrypted_text, n):
    l = len(encrypted_text) // 2
    for j in range(n):
        res = []
        for i in range(len(encrypted_text)):
            if i % 2 == 0:
                res.append(encrypted_text[l:][i//2])
            else:
                res.append(encrypted_text[:l][i//2])

        encrypted_text = ''.join(res)
    return encrypted_text

def encrypt(text, n):
    for j in range(n):
        odd = []
        even = []
        for i in range(len(text)):
            if i % 2 == 0:
                even.append(text[i])
            else:
                odd.append(text[i])
        text = ''.join(odd)+''.join(even)
    return text
print(decrypt("This is a test!", 4)) # "This is a test!")
print(encrypt("This is a test!", 3))

from random import choice, randint
from string import ascii_letters, digits, punctuation

try:
    from itertools import chain, izip_longest as zip_longest
except ImportError:
    from itertools import chain, zip_longest


VALID_CHARS = '{}{}{}'.format(ascii_letters, digits, punctuation)


def generate_random_text():
    return ''.join(choice(VALID_CHARS) for _ in range(randint(5, 40)))


def decrypt_solution(encrypted_text, n):
    if not encrypted_text or n <= 0:
        return encrypted_text
    half = len(encrypted_text) // 2
    result = encrypted_text
    for _ in range(n):
        result = ''.join(chain(*zip_longest(
            result[half:], result[:half], fillvalue=''
        )))
    return result


def encrypt_solution(text, n):
    if not text or n <= 0:
        return text
    result = text
    for _ in range(n):
        result = result[1::2] + result[::2]
    return result


test.describe('Basic Tests')
test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

test.assert_equals(encrypt("", 0), "")
test.assert_equals(decrypt("", 0), "")
test.assert_equals(encrypt(None, 0), None)
test.assert_equals(decrypt(None, 0), None)

test.describe('Random Tests')
# Encrypt Tests
for _ in range(75):
    random_text = generate_random_text()
    random_n = randint(-100, 1000)
    test.it("{}\n   n={}".format(random_text, random_n))
    test.assert_equals(encrypt(random_text, random_n),
                       encrypt_solution(random_text, random_n))

# Decrypt Tests
for _ in range(75):
    random_text = generate_random_text()
    random_n = randint(-100, 1000)
    test.it("{}\n   n={}".format(random_text, random_n))
    test.assert_equals(decrypt(random_text, random_n),
                       decrypt_solution(random_text, random_n))