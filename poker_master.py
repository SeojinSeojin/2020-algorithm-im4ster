from itertools import combinations
import operator as op
import time
from functools import reduce
cardToNum = {"AS": 0, "2S": 1, "3S": 2, "4S": 3, "5S": 4, "6S": 5, "7S": 6, "8S": 7, "9S": 8, "XS": 9, "JS": 10, "QS": 11, "KS": 12,
             "AH": 13, "2H": 14, "3H": 15, "4H": 16, "5H": 17, "6H": 18, "7H": 19, "8H": 20, "9H": 21, "XH": 22, "JH": 23, "QH": 24, "KH": 25,
             "AD": 26, "2D": 27, "3D": 28, "4D": 29, "5D": 30, "6D": 31, "7D": 32, "8D": 33, "9D": 34, "XD": 35, "JD": 36, "QD": 37, "KD": 38,
             "AC": 39, "2C": 40, "3C": 41, "4C": 42, "5C": 43, "6C": 44, "7C": 45, "8C": 46, "9C": 47, "XC": 48, "JC": 49, "QC": 50, "KC": 51}
leftCards = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "XS", "JS", "QS", "KS",  # 남은카드들
             "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "XH", "JH", "QH", "KH",
             "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "XD", "JD", "QD", "KD",
             "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "XC", "JC", "QC", "KC"]
# 족보


def get_level(cards):  # cards는 set
    return 100
    cards_int = []
    for i in cards:
        cards_int.append(cardToNum[i])
    cards_int = sorted(cards_int)
    # 문양 같음
    flush = 0
    if cards_int[0] / 13 == cards_int[4] / 13:  # 플러쉬
        for i in range(4):
            if cards_int[0] / 13 == i:
                if cards_int[1] % 13 == 9 and cards_int[0] % 13 == 0:  # 로얄 스트레이트 플러쉬
                    return 1.0+(i/10)
                elif cards_int[0] % 13 == 0 and cards_int[4] % 13 == 4:  # 백스트레이트 플러쉬
                    return 2.0+(i/10)
                elif (cards_int[0] % 13) + 4 == cards_int[4] % 13:  # 스트레이트 플러쉬
                    return 3.0+(i/10)
                else:
                    flush = 1.0+(i/10)

    count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in cards_int:
        count[i % 13] += 1

    for i in range(13):
        # four card
        if count[i] == 4:
            ret = 4.0 + (13 - (i+1))/100
            return ret  # 4.00~4.12

        if count[i] == 3:
            for j in range(13):
                if i == j:
                    continue
                elif count[j] == 2:  # 풀하우스
                    ret = 5.0 + (13 - (i+1))/100
                    return ret  # 5.00~5.12
            if flush != 0:  # 플러쉬
                ret = 5.0 + flush
                return ret  # 6.0~6.3
            else:  # 트리플
                ret = 10.0 + (13 - (i+1))/100
                break
                return ret  # 10.00~10.12

# 여기부터 마저하자. 현재 마운틴부터 하면 됨.
    cards_num = []  # 모양빼고 숫자만
    for i in cards_int:
        cards_num.append(i % 13)
    cards_num = sorted(cards_num)
    if cards_num[1] == 9 and cards_num[0] == 0:  # 마운틴
        ret = 7.0
        for j in cards_int:
            if j % 13 == 9:
                ret = ret + (int((j / 13)) / 10)
                return ret
    elif cards_num[0] == 0 and cards_num[4] == 4:  # 백스트레이트
        ret = 8.0
        for j in cards_int:
            if j % 13 == 0:
                ret = ret + (int((j / 13)) / 10)
                return ret
    elif cards_num[0] + 4 == cards_num[4]:  # 스트레이트
        ret = 9.0
        maxx = 0
        for j in cards_int:
            maxx = max(maxx, (int((j / 13)) / 10))  # 숫자먼저 고려 -> 문양?
            return ret + maxx

    for i in range(13):
        if count[i] == 2:
            for j in range(13):
                if i == j:
                    continue
                elif count[j] == 2:  # 투페어 +i숫자 + 문양도 고려
                    ret = 11.0 + (13 - (j+1))/100
                    return ret
            ret = 12.0 + (13 - (i+1))/100  # 원페어  +문양도 추가해야함
            return ret

    ret = 13.0
    maxx = 0.0
    for i in range(13):  # 노페어
        if count[i] == 1:
            maxx = max(maxx, (13 - (i+1))/100)  # 두번째 max도 고려
    ret = ret + maxx
    return ret


s = {"AS", "XS", "JS", "QS", "KS"}
print(get_level(s))
levels = dict()
print(leftCards)
# for i in combinations(leftCards, 5):
#     print(i)
#     l = get_level(set(i))
#     if(l in levels):
#         print(l, "레벨 겹침:", i)
#     levels[l] = 1


class player():
    playerNum = 0
    # minLevel = 100

    def __init__(self, cards):
        self.cards = cards
        player.playerNum += 1
        for c in cards:
            leftCards.remove(c)


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom


def get_best_level(cards):
    ans = 10000
    for i in combinations(cards[:-1], 4):
        list(i).append(cards[-1])
        ans = min(ans, get_level(i))  # 마지막 원소는 항상 포함
    return ans


def f(p, N):
    global res, leftCards
    #print(p[1].cards, p[2].cards)

    if len(p[N].cards) > 4:  # 같은 플레이어 카드끼리는 순서 없음
        new_leftCards = leftCards[leftCards.index(p[N].cards[-1]):]
    else:
        new_leftCards = leftCards
    for ind, i in enumerate(new_leftCards):
        if ind+7-len(p[N].cards) > 37:
            continue
        flag = 0
        for j in range(p[0].playerNum):
            if i in p[j].cards:  # 불가능한 경우 (카드 겹침)
                flag = 1
        if flag:
            continue
        p[N].cards.append(i)

        # print(i, playerN, p[playerN].cards)
        if get_best_level(p[N].cards) < my_level:  # 내가 짐 -> 가지치기
            # print(ind, len(new_leftCards)-ind-1, 7-l[1])
            if N == 1:
                res += ncr(len(new_leftCards)-ind-1, 7 -
                           len(p[1].cards))*ncr(34, 7-len(p[2].cards))
            elif N == 2:
                res += ncr(len(new_leftCards)-ind-1, 7 -
                           len(p[2].cards))
            # print("##", res)
            flag = 1
        if not flag:
            if len(p[N].cards) == 7:
                if N != 2:
                    f(p, N+1)
            else:
                f(p, N)
        p[N].cards.pop()


def win_prob(p):
    global res
    res = 0  # 내가 지는 경우의 수
    f(p, 1)
    # (내가이길확률) = 1 - (누군가 다른사람이 이길확률)
    return 1 - (res/(ncr(37, 3)*ncr(34, 3)))


p = []
start = time.time()
# 플레이어 인스턴스들 생성 -> 프론트랑 합치기
p.append(player(['AH', 'XS', '4D', 'JD', '7D', '7H', '8S']))  # 나
p.append(player(['AS', 'XD', '4H', 'KD']))  # p1
p.append(player(['2S', 'QD', '5H', 'KH']))  # p2
# p[3] = player(['2H', '3D', '6H', '5D'])  # p3

my_level = 10
# for i in combinations(p[0].cards, 5):
# my_level = min(my_level, get_level(i))
print("내레벨: ", my_level)
print("승리확률:", win_prob(p))
print("실행시간: ", time.time()-start)
