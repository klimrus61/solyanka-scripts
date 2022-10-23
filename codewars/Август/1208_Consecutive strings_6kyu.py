# Получает лист строк и число необходимых подстрок, находит 1 попавшуюся строку состоящию из k элем массива strarr

def longest_consec(strarr, k):
    n = len(strarr)
    if n > k and k > 0:
        a = [''.join(strarr[0:0+k]),]
        for i in range(n-k+1):
            if len(''.join(strarr[i:i+k])) > len(a[0]):
                a.append(''.join(strarr[i:i+k]))
                del a[0]
        return a[0]
    return ''


def longest_consec_notmy(strarr, k):
    result = ""
    
    if k > 0 and len(strarr) >= k:
        for index in range(len(strarr) - k + 1):
            s = ''.join(strarr[index:index+k])
            if len(s) > len(result):
                result = s
            
    return result

def longest_consec_cool(s, k):
    return max(["".join(s[i:i+k]) for i in range(len(s)-k+1)], key=len) if s and 0 < k <= len(s) else ""

def test_str(answ, right='rrruiihhqqqkaattfuuutttdqqqkkmmqqggaoooiiiddjjpppszzzxxxdduuzjjkkktttlppprvvvuucgggfffdsrjbbbfffiiixxrrvvvgxxcccuuuciivvvewbbiivknnnhhhaaaqqzhhhbyyyddttyyyyxxakccffoouuugkaaaccddwwwvvvaakggmmmtttqqvvggbbeewlusjjjntttcccupgggjjjjxxvvhhzzzwnnnyyyaacoodmxxjjjjvvvqgggqqllnnyqqquujjymmwwwzzzxxyyyvvvpxxxzzzfuxwwpzzzbbbvvxxxczzvviffmmmwwwmmmrrriihhffhhkmmqqrrrbbuuuahhphhyyyfmmmoosskkkvvgbvvvvpooorrbbbrnaaaggsgggaafddfffpyyyqqllbbppyyasssphyyytttilbbbffyyeeevvvihhfftttoofooogssqqvgggdyyttttppeeebbwww'):
    if answ == right:
        print("Заебок")
    else:
        print('Переделывай')
        print('Твое говно:', answ)
        print('Как надо:', right)
        print(len(answ), len(right))
test_str(longest_consec(['pprlllzzffrrccc', 'mzzzzzmm', 'ssddzzz', 'jjxsshzzr', 'nnnhzbbb', 'tjjssxxxccvvp', 'qqqbby', 'liiifiiizz', 'evjssswwwbbfffnn', 'kkkmmmmmmc', 'fkqqqkkrgg', 'roiiinnrltttt', 'jlllppp', 'yyydttf', 'zttqqbbbmmnn', 'llyyg', 'obbottt', 'bbvfffykm', 'rrrpzmmmgggk', 'llldddwzzznnn', 'llrrree', 'wiicbbtt', 'iizzzoooqqaammmtt', 'xlllqqiqqqaa', 'uwwww', 'wwwwkkkjj', 'uffaa', 'qqqllppzzzgggmmjjj', 'ppphttmmjbg', 'ieeiiuvvvbb', 'laaavvvrrxxvvllccc', 'jjloggg', 'rrrbbbzzzoiii', 'mmmfffccc', 'jjqqqbbqqq', 'zziisszzzggg', 'hhyjkkkvvvbbbhhh', 'kkkqqvv', 'rrrmmmmmmwww', 'rrraaauuutt', 'ffeezoox', 'paaffiiiiiill', 'ewwwjxzzhh', 'icoooii', 'fllly', 'tvjg', 'ozczza', 'lllccaaasss', 'ykddd', 'ooqqqggopwwheee', 'zxxrrrccb', 'lllvvrtbb', 'nnnaaassqqqp', 'oojxxiii', 'vvvbbbffdd', 'mlvvuuu', 'aazfffyy', 'kkoojjzzb', 'nttchh', 'tttbbdiin', 'ddvvhg', 'ccpppppiiiu', 'sssoomxooorroo', 'pzzncccwwzzztttppb', 'dddrrwwiippp', 'aaajqqqjjrrrkkooz', 'qqdnkkk', 'zzzccmunrrr', 'aaaaaazzfffzg', 'eevvzzdvv', 'yyhhhqqxx', 'xggguqw', 'mmggddgjjjw', 'lnnnnppfffvvvi', 'mmmmmrrmllddduuuttt', 'zzeeefffjjjgbbzzzoo', 'tciixzjjpp', 'bbbxxppqqkj', 'eebbvpp', 'mmmaaapp', 'kmmmm', 'hfbsqqq', 'ooleeyymmm', 'tttooov', 'xxewnnii', 'uqgggollll', 'jjjpphh', 'bbbmmmhhhhvvvrrr', 'rrrhhffx', 'nnngyeee', 'llkkuxxfffq', 'ffvvha', 'nhhhwwwz', 'jklbbqqfg', 'vvvkwww', 'mmttuugj', 'ddggguggo', 'zzxxvvvhhhzzzooo', 'uuffyrrrfff', 'mlljjcqq', 'fffvvsssfffn', 'kkkjjmmww', 'eeelvvvkdddhhhhh', 'rrrddgxb', 'yyyuuan', 'hhhccyzz', 'vaaahhjjll', 'sspzppl', 'keeemiffa', 'ssszzllyyyc', 'tddookkkcccbbv', 'nnhhvh', 'mmiipwwtt', 'jtrr', 'pptplii', 'oooffpkkksss', 'xxwwwdtttn', 'juucccinnrii', 'wwwwss', 'qqiihhhvvoor', 'kkmmmbbkk', 'wwrrryyysjjjyy', 'kkgggfffoozzzffv', 'llljxxxxxeett', 'xxmx', 'lllyyyqqqf', 'vvrrrraaabbb', 'thhooqnnjjj', 'llooodh', 'ddrrrvveezd', 'ifzzzvv', 'oggkkklllooo', 'ooovvjjm', 'rrruiihhqqq', 'kaattfuuutttd', 'qqqkkmmqqgg', 'aoooiiiddjjpppszzz', 'xxxdduuz', 'jjkkktttl', 'ppprvvvuuc', 'gggfffdsrjbbb', 'fffiiixxrrvvvgxx', 'cccuuuciivvv', 'ewbbiivk', 'nnnhhhaaaqqzhhhbyyy', 'ddttyy', 'yyxxakccffoo', 'uuugk', 'aaaccddwwwvvvaa', 'kggmmmtttqqvvgg', 'bbeewl', 'usjjjnttt', 'cccupgggjjj', 'jxxvvhhzzz', 'wnnnyyyaacoo', 'dmxxjjjjvvvq', 'gggqqllnnyqqquujj', 'ymmwwwzzzxxyyy', 'vvvpxxx', 'zzzfuxwwpzzz', 'bbbvvxxxczzvv', 'iffmmmwwwmmmrrr', 'iihhffhhk', 'mmqqrrrbb', 'uuuahhp', 'hhyyyfmmmoo', 'sskkkvvgb', 'vvvvpooorrbbbr', 'naaaggsgggaafdd', 'fffpyyy', 'qqllbbppyyasss', 'phyyyttti', 'lbbbffyyeee', 'vvvihhfftttoo', 'fooogssqqv', 'gggdyyttttppeeebbwww', 'ggsssurrccq', 'cjjppffaaag', 'xiihlluuddkww', 'fvvaaaf', 'xttqqiig', 'qqhggwwwccwwwy', 'xlllooorrr', 'ihiiijjjyyiiic', 'bbfffoyyy', 'ffxpppzzllv', 'gggrrrvvggc', 'iikkqqqnfhhhhf', 'knnpppvq', 'gnllu', 'ammmxxxwwpppiiiqqq', 'eebbbgff', 'qqjrrrkzzaa', 'cczzss', 'vvvazooommmll', 'bbbmaafffwwwuu', 'uuuccckwwwrr'], 43))
#'rrruiihhqqqkaattfuuutttdqqqkkmmqqggaoooiiiddjjpppszzzxxxdduuzjjkkktttlppprvvvuucgggfffdsrjbbbfffiiixxrrvvvgxxcccuuuciivvvewbbiivknnnhhhaaaqqzhhhbyyyddttyyyyxxakccffoouuugkaaaccddwwwvvvaakggmmmtttqqvvggbbeewlusjjjntttcccupgggjjjjxxvvhhzzzwnnnyyyaacoodmxxjjjjvvvqgggqqllnnyqqquujjymmwwwzzzxxyyyvvvpxxxzzzfuxwwpzzzbbbvvxxxczzvviffmmmwwwmmmrrriihhffhhkmmqqrrrbbuuuahhphhyyyfmmmoosskkkvvgbvvvvpooorrbbbrnaaaggsgggaafddfffpyyyqqllbbppyyasssphyyytttilbbbffyyeeevvvihhfftttoofooogssqqvgggdyyttttppeeebbwww'