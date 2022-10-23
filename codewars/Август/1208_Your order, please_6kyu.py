import re
def order(sentence):
    if sentence != '':
        s = sentence.split(' ')
        return ' '.join(sorted(s, key=lambda x: int(re.search(r'\d', x)[0])))


def order(words):
  return ' '.join(sorted(words.split(), key=lambda w:sorted(w)))
