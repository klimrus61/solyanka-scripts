class Poker():

    DATA = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    SUITS = {'♥', '♠', '♣', '♦'}

    def __init__(self, hole_cards, community_cards):
        self.all_cards_list = hole_cards + community_cards
        self.sorted_cards = sorted(self.all_cards_list, key=lambda x: Poker.DATA.get(x[:-1]), reverse=True)
        self.rank = 0
        self.sings = [val[:-1] for val in self.sorted_cards]
    

    def straight_flush(self):
        arr = self.sorted_cards
        data = Poker.DATA
        for 
        

    def is_straight(self):
        arr = self.sorted_cards
        data = Poker.DATA
        if len(set(arr)) >=5:
            for i in range(2):
                chunk = []
                for j in range(5):

                    if not len(chunk) or data.get(arr[i+j][:-1]) == data.get(chunk[-1])-1:
                        chunk.append(arr[i+j][:-1])
                    else:
                        break
                if len(chunk) == 5:
                    self.rank = 4
                    return chunk
        return []
    
    def is_flush(self):
        suits = [s[-1] for s in self.sorted_cards]
        res = []
        for s in self.sorted_cards:
            if suits.count(s[-1]) >=5:
                res.append(s[:-1])
        if len(res) >=5:
            self.rank = 5
            return [i for i in res]
        else: return []
    
    def num_of_a_kind(self, num):
        sings = self.sings
        res = []
        for s in self.sorted_cards:
            if num == 4 and sings.count(s[:-1]) == 4:
                self.rank = 7
                res.append(s[:-1])
                res.extend([i for i in set(sings) if i != s[:-1]])
                return res[:2]
            if num == 3 and sings.count(s[:-1]) == 3:
                self.rank = 3
                res.append(s[:-1])
                res.extend([i[:-1] for i in self.sorted_cards if i[:-1] != s[:-1]])
                return res[:3]
        return []

    def full_house(self):
        sings = self.sings
        res = []
        stop = 0
        for val in set(sings):
            if sings.count(val) == 3:
                res.append(val)
            if sings.count(val) == 2 and stop == 0:
                res.append(val)
                stop = 1

        if len(res) >= 2:
            return res[:2]
        return []
    
    def two_pair(self):
        sings = self.sings
        res = []
        for s in set(self.sorted_cards):
            if sings.count(s[:-1]) == 2 and res.count(s[:-1])==0:
                res.append(s[:-1])
            elif sings.count(s[:-1]) == 2 and res.count(s[:-1])==0:
                res.append(s[:-1])
        if len(res) == 2:
            res = sorted(res, key=lambda x: Poker.DATA.get(x[:-1]), reverse=True) + [i for i in self.sorted_cards if not in res]

    def pair(self):
        sings = self.sings
        res = []
        for s in self.sorted_cards:
            if sings.count(s[:-1]) == 2 and res.count(s[:-1])==0:
                res.append(s[:-1])
            elif sings.count(s[:-1]) == 1 and res.count(s[:-1])==0:
                res.append(s[:-1])
            if len(res)==2:
                self.rank = 2
                return res[:4]
        return []

    def hand_max(self):
        # ans = self.is_straight(check_flush=True)
        # if len(ans) != 0:
        #     return ('straight-flush', ans)
        ans = self.num_of_a_kind(num=4)
        if len(ans) != 0:
            return ('four-of-a-kind', ans)
        ans = self.full_house()
        if len(ans) != 0:
            return ('full house', ans)
        ans = self.is_flush()
        if len(ans) != 0:
            return ('flush', ans)
        ans = self.is_straight()
        if len(ans) != 0:
            return ('straight', ans)
        ans = self.num_of_a_kind(num=3)
        if len(ans) != 0:
            return ('three-of-a-kind', ans)
        ans = self.two_pair()
        if len(ans) != 0:
            return ('two pair', ans)
        ans = self.pair()
        if len(ans) != 0:
            return ('two pair', ans)
        return ('nothing', [i[:-1] for i in self.sorted_cards[:5]])
def hand(hole_cards, community_cards):
    poker = Poker(hole_cards, community_cards)
    return poker.hand_max()







print(hand(['J♣', '2♥'], ['2♦', '8♦', '10♠', '9♠', 'J♠']))




