import re
def count_smileys(arr):
    x = re.findall(r'(?:\:|\;){1}(?:-|~){0,1}(?:\)|D){1}', ' '.join(arr))
    return len(x)


from re import findall
def count_smileys(arr):
    return len(list(findall(r"[:;][-~]?[)D]", " ".join(arr))))

def count_smileys(arr):
    eyes = [":", ";"]
    noses = ["", "-", "~"]
    mouths = [")", "D"]
    count = 0
    for eye in eyes:
        for nose in noses:
            for mouth in mouths:
                face = eye + nose + mouth
                count += arr.count(face)
    return count
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))