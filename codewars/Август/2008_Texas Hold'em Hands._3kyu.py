def isstraight(arr):
    for i in range(2):
        res, chunk = [], []
        for j in range(5):
            if not len(chunk) or DATA.get(arr[i+j][:-1]) == DATA.get(chunk[-1]) - 1:          #     if first or consecutive
                chunk.append(arr[i+j][:-1])                                #         add to current chunk
            else:                        #     else, it's a gap
                break
        if len(chunk) == 5:
            return chunk
    return False

def isflush(arr):
    all_cards_suits = [i[-1] for i in arr]
    for suit in SUITS:
        if all_cards_suits.count(suit) >= 5:
            return [val[:-1] for val in arr if suit in val]
    return False
    


def hand(hole_cards, community_cards):
    all_cards_list = hole_cards + community_cards
    sorted_cards = sorted(all_cards_list, key=lambda x: DATA.get(x[:-1]), reverse=True)
    # nums = [DATA.get(i[:-1]) for i in sorted_cards]
    # Is Straight-flush 
    is_straigh = isstraight(sorted_cards)
    is_flush = isflush(sorted_cards)
    if is_straigh and isflush(is_straigh):
        return ('straight-flush', is_straigh)
    elif is_flush:
        return ('flush', is_flush)
    



DATA = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
SUITS = {'♥', '♠', '♣', '♦'}



print(hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"])) #  ("flush", ["Q", "J", "10", "5", "3"]),

# Possible hands are, in descending order of value:

#     Straight-flush (five consecutive ranks of the same suit). Higher rank is better.
#     Four-of-a-kind (four cards with the same rank). Tiebreaker is first the rank, then the rank of the remaining card.
#     Full house (three cards with the same rank, two with another). Tiebreaker is first the rank of the three cards, then rank of the pair.
#     Flush (five cards of the same suit). Higher ranks are better, compared from high to low rank.
#     Straight (five consecutive ranks). Higher rank is better.
#     Three-of-a-kind (three cards of the same rank). Tiebreaker is first the rank of the three cards, then the highest other rank, then the second highest other rank.
#     Two pair (two cards of the same rank, two cards of another rank). Tiebreaker is first the rank of the high pair, then the rank of the low pair and then the rank of the remaining card.
#     Pair (two cards of the same rank). Tiebreaker is first the rank of the two cards, then the three other ranks.
#     Nothing. Tiebreaker is the rank of the cards from high to low.
# hand(["A♠", "A♦"], ["J♣", "5♥", "10♥", "2♥", "3♦"])
# # ...should return ("pair", ranks: ["A", "J", "10", "5"]})
# hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"])
# # ...should return ("flush", ["Q", "J", "10", "5", "3"])

# with describe("Texas Hold'em Hands"):
#     with it("nothing"):
#         test.assert_equals(
#             hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
#             ("nothing", ["A", "K", "Q", "J", "9"]),
#         )
#     with it("pair"):
#         test.assert_equals(
#             hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]),
#             ("pair", ["Q", "K", "J", "9"]),
#         )
#     with it("two pair"):
#         test.assert_equals(
#             hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]),
#             ("two pair", ["K", "J", "9"]),
#         )
#     with it("three of a kind"):
#         test.assert_equals(
#             hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]),
#             ("three-of-a-kind", ["Q", "J", "9"]),
#         )
#     with it("straight"):
#         test.assert_equals(
#             hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]),
#             ("straight", ["K", "Q", "J", "10", "9"]),
#         )
#     with it("flush"):
#         test.assert_equals(
#             hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]),
#             ("flush", ["Q", "J", "10", "5", "3"]),
#         )
#     with it("full house"):
#         test.assert_equals(
#             hand(["A♠", "A♦"], ["K♣", "K♥", "A♥", "Q♥", "3♦"]),
#             ("full house", ["A", "K"]),
#         )
#     with it("four of a kind"):
#         test.assert_equals(
#             hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]),
#             ("four-of-a-kind", ["2", "3"]),
#         )
#     with it("straight flush"):
#         test.assert_equals(
#             hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]),
#             ("straight-flush", ["J", "10", "9", "8", "7"]),
#         )