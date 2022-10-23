def title_case(title, minor_words=''):
    res = []
    for word in title.split():
        if len(res)==0 or word.lower() not in minor_words.lower().split():
            res.append(word.title())
        else:
            res.append(word.lower())
    return ' '.join(res)