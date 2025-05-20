from itertools import combinations
from collections import Counter


def card_value(card):
    """카드 값을 숫자로 변환"""
    value_map = {1: 1, 11: 11, 12: 12, 13: 13}
    return card if isinstance(card, int) else value_map[card]


def count_hands():
    suits = [0, 1, 2, 3]  # 0: 하트, 1: 다이아몬드, 2: 클로버, 3: 스페이드
    values = list(range(1, 14))  # 1: A, 2-10, 11: J, 12: Q, 13: K
    deck = [(value, suit) for suit in suits for value in values]
    all_hands = list(combinations(deck, 6))

    hand_counts = Counter()

    for hand in all_hands:
        values = sorted([card[0] for card in hand])
        suits = [card[1] for card in hand]
        value_counts = Counter(values)
        suit_counts = Counter(suits)

        def is_flush_straight(hand):
            """ 같은 문양이면서 연속된 5장의 카드인지 확인 """
            sorted_hand = sorted(hand, key=lambda x: (x[1], x[0]))
            for i in range(len(sorted_hand) - 4):
                segment = sorted_hand[i:i + 5]
                if all(segment[j][1] == segment[0][1] for j in range(5)) and \
                        [card[0] for card in segment] == list(range(segment[0][0], segment[0][0] + 5)):
                    return True, segment
            return False, []

        is_flush = max(suit_counts.values()) >= 5
        unique_values = sorted(set(values))
        flush_straight, flush_straight_cards = is_flush_straight(hand)

        if flush_straight and set([1, 2, 3, 4, 5]) == set(card[0] for card in flush_straight_cards):
            hand_counts["로얄 스트레이트 플러쉬"] += 1
        elif flush_straight:
            hand_counts["스트레이트 플러쉬"] += 1
        elif 4 in value_counts.values():
            hand_counts["포카드"] += 1
        elif 3 in value_counts.values() and 2 in value_counts.values():
            hand_counts["풀하우스"] += 1
        elif list(value_counts.values()).count(3) == 2:
            hand_counts["풀하우스"] += 1
        elif is_flush:
            hand_counts["플러쉬"] += 1
        elif set([1, 2, 3, 4, 5]).issubset(values):
            hand_counts["빽스트레이트"] += 1
        elif set([10, 11, 12, 13, 1]).issubset(values):
            hand_counts["마운틴"] += 1
        elif len(unique_values) >= 5 and any(
                unique_values[i:i + 5] == list(range(unique_values[i], unique_values[i] + 5)) for i in
                range(len(unique_values) - 4)):
            hand_counts["스트레이트"] += 1
        elif 3 in value_counts.values():
            hand_counts["트리플"] += 1
        elif list(value_counts.values()).count(2) >= 2:
            hand_counts["투페어"] += 1
        elif 2 in value_counts.values():
            hand_counts["원페어"] += 1
        else:
            hand_counts["탑"] += 1

    return hand_counts


# 경우의 수 계산
hand_counts = count_hands()
print("각 족보의 경우의 수:")
for hand, count in hand_counts.items():
    print(f"{hand}: {count}")

def solution():
    def euc(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    total = 20358520
    case = [6612900,9730740,2532816,732160,282060,39780,39780,205976,165984,14664,1472,188]
    print(sum(case))
    for c in case:
        t = euc(total, c)
        print(f"{c//t}/{total//t}")
solution()