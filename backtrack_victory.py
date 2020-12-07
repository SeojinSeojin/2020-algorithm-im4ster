from itertools import combinations
import operator as op
import time
from functools import reduce
leftCards = []
# 족보 구한 결과파일 가져오기
level = dict()
cnt = 0
my_level = 0
f = open('write.txt', 'r')
lines = f.readlines()
for itr in lines:
    itr = itr[2:-3].split("', '")
    level[tuple(itr)] = cnt
    cnt += 1
f.close()

#print(level)

def get_level(cards):  # cards는 set
    cards = list(cards)
    cards.sort()
    ret = level[tuple(cards)]
    return ret


#s = ["AS", "XS", "JS", "QS", "KS"]
#print(get_level(s))


class player():
    playerNum = 0

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
    ans = 3000000
    for i in combinations(cards[:-1], 4):
        i=list(i)
        i.append(cards[-1])
        ans = min(ans, get_level(i))  # 마지막 원소는 항상 포함
    return ans


def f(p, N):
    global res, leftCards
    global my_level
    print(p[1],p[2],N)
    if len(p[N].cards) > 4:  # 같은 플레이어 카드끼리는 순서 없음
        new_leftCards = leftCards[leftCards.index(p[N].cards[-1]):]
    else:
        new_leftCards = leftCards
        
    for ind, i in enumerate(new_leftCards):
        if N==2:
            l=len(new_leftCards)
            nn=new_leftCards[ind:]
            if p[1].cards[4] in nn: l-=1
            if p[1].cards[5] in nn: l-=1
            if p[1].cards[6] in nn: l-=1
        if (N==1 and ind+7-len(p[N].cards) > 37) or (N==2 and ind+7-len(p[N].cards)>l): #남은칸 채울 카드가 부족할때
            continue
        flag = 0
        for j in range(p[0].playerNum):
            if i in p[j].cards:  # 불가능한 경우 (카드 겹침)
                flag = 1
        if flag:
            continue
        p[N].cards.append(i)

        if get_best_level(p[N].cards) < my_level:  # 내가 짐 -> 가지치기
            if N == 1:
                res += ncr(len(new_leftCards)-ind-1, 7 - len(p[1].cards))*ncr(34, 3)
            elif N == 2:
                res += ncr(l-ind-1, 7 - len(p[2].cards))
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



def set_leftCards():
    global leftCards
    leftCards = ["AS", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "XS", "JS", "QS", "KS",  # 남은카드들
    "AH", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "XH", "JH", "QH", "KH",
    "AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "XD", "JD", "QD", "KD",
    "AC", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "XC", "JC", "QC", "KC"]

def get_victory_percentage(cards):

    global my_level
    set_leftCards()
    p = []
    player.playerNum=0
    p.append(player(cards[8:]))  # 나
    p.append(player(cards[:4]))  # p1
    p.append(player(cards[4:8]))  # p2
    print(leftCards)
    my_level = 3000000
    for i in combinations(p[0].cards, 5):
        my_level = min(my_level, get_level(i))
    print("내레벨: ", my_level)
    vp = win_prob(p)
    print("승리확률:", vp)
    #print("실행시간: ", time.time()-start)
    return vp
