from itertools import combinations
import operator as op
from functools import reduce
cardToNum = {"AS": 0, "2S": 1, "3S": 2, "4S": 3, "5S": 4, "6S": 5, "7S": 6, "8S": 7, "9S": 8, "XS": 9, "JS": 10, "QS": 11, "KS": 12,
             "AH": 13, "2H": 14, "3H": 15, "4H": 16, "5H": 17, "6H": 18, "7H": 19, "8H": 20, "9H": 21, "XH": 22, "JH": 23, "QH": 24, "KH": 25,
             "AD": 26, "2D": 27, "3D": 28, "4D": 29, "5D": 30, "6D": 31, "7D": 32, "8D": 33, "9D": 34, "XD": 35, "JD": 36, "QD": 37, "KD": 38,
             "AC": 39, "2C": 40, "3C": 41, "4C": 42, "5C": 43, "6C": 44, "7C": 45, "8C": 46, "9C": 47, "XC": 48, "JC": 49, "QC": 50, "KC": 51}

# 족보


def get_level(cards):  # cards는 set
  cards_int = []
  for i in range(len(cards)):
    cards_int.append(cardToNum[cards[i]])
  cards_int = sorted(cards_int)
  # 문양 같음
  flush = 0
  if cards_int[0] / 13 == cards_int[1] / 13 and cards_int[1] / 13 == cards_int[2] / 13 and cards_int[2] / 13 == cards_int[3] / 13 and cards_int[3] / 13 == cards_int[4] / 13:
    # spade
    if cards_int[0] / 13 == 0:
        if cards_int[1] % 13 == 9 and cards_int[2] % 13 == 10 and cards_int[3] % 13 == 11 and cards_int[4] % 13 == 12 and cards_int[0] % 13 == 0:
            return 1.0
        elif cards_int[0] % 13 == 0 and cards_int[1] % 13 == 2 and cards_int[2] % 13 == 3 and cards_int[3] % 13 == 4 and cards_int[4] % 13 == 5:
            return 2.0
        elif (cards_int[0] % 13) + 1 == cards_int[1] % 13 and (cards_int[1] % 13) + 1 == cards_int[2] % 13 and (cards_int[2] % 13) + 1 == cards_int[3] % 13 and (cards_int[3] % 13) + 1 == cards_int[4] % 13:
            return 3.0
        else:
            flush = 1.0

    # heart
    if cards_int[0] / 13 == 1:
        if cards_int[1] % 13 == 9 and cards_int[2] % 13 == 10 and cards_int[3] % 13 == 11 and cards_int[4] % 13 == 12 and cards_int[0] % 13 == 0:
            return 1.1
        elif cards_int[0] % 13 == 0 and cards_int[1] % 13 == 2 and cards_int[2] % 13 == 3 and cards_int[3] % 13 == 4 and cards_int[4] % 13 == 5:
            return 2.1
        elif (cards_int[0] % 13) + 1 == cards_int[1] % 13 and (cards_int[1] % 13) + 1 == cards_int[2] % 13 and (cards_int[2] % 13) + 1 == cards_int[3] % 13 and (cards_int[3] % 13) + 1 == cards_int[4] % 13:
            return 3.1
        else:
            flush = 1.1

    # diamond
    if cards_int[0] / 13 == 2:
        if cards_int[1] % 13 == 9 and cards_int[2] % 13 == 10 and cards_int[3] % 13 == 11 and cards_int[4] % 13 == 12 and cards_int[0] % 13 == 0:
            return 1.2
        elif cards_int[0] % 13 == 0 and cards_int[1] % 13 == 2 and cards_int[2] % 13 == 3 and cards_int[3] % 13 == 4 and cards_int[4] % 13 == 5:
            return 2.2
        elif (cards_int[0] % 13) + 1 == cards_int[1] % 13 and (cards_int[1] % 13) + 1 == cards_int[2] % 13 and (cards_int[2] % 13) + 1 == cards_int[3] % 13 and (cards_int[3] % 13) + 1 == cards_int[4] % 13:
            return 3.2
        else:
            flush = 1.2

    # club
    if cards_int[0] / 13 == 3:
        if cards_int[1] % 13 == 9 and cards_int[2] % 13 == 10 and cards_int[3] % 13 == 11 and cards_int[4] % 13 == 12 and cards_int[0] % 13 == 0:
            return 1.3
        elif cards_int[0] % 13 == 0 and cards_int[1] % 13 == 2 and cards_int[2] % 13 == 3 and cards_int[3] % 13 == 4 and cards_int[4] % 13 == 5:
            return 2.3
        elif (cards_int[0] % 13) + 1 == cards_int[1] % 13 and (cards_int[1] % 13) + 1 == cards_int[2] % 13 and (cards_int[2] % 13) + 1 == cards_int[3] % 13 and (cards_int[3] % 13) + 1 == cards_int[4] % 13:
            return 3.3
        else:
            flush = 1.3

  count = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
  for i in range(len(cards_int)):
    count[cards_int[i] % 13] = count[cards_int[i] % 13] + 1

  for i in range(13):
    # four card
    if count[i] == 4:
        ret = 4.0
        ret = ret + (13 - (i+1))/100
        return ret  # 4.00~4.12

    if count[i] == 3:
        for j in range(13):
            if i == j:
                continue
            elif count[j] == 2:
                ret = 5.0
                ret = ret + (13 - (i+1))/100
                return ret  # 5.00~5.12
        if flush != 0:
            ret = 5.0 + flush
            return ret  # 6.0~6.3
        else:
            ret = 10.0
            ret = ret + (13 - (i+1))/100
            return ret  # 10.00~10.12


# 여기부터 마저하자. 현재 마운틴부터 하면 됨.
  if cards_int[1] % 13 == 9 and cards_int[2] % 13 == 10 and cards_int[3] % 13 == 11 and cards_int[4] % 13 == 12 and cards_int[0] % 13 == 0:
      ret = 7.0
      ret = ret + ((int(cards_int[0] / 13)) / 10)
      return ret
  elif cards_int[0] % 13 == 0 and cards_int[1] % 13 == 2 and cards_int[2] % 13 == 3 and cards_int[3] % 13 == 4 and cards_int[4] % 13 == 5:
      ret = 8.0
      ret = ret + ((int(cards_int[0] / 13)) / 10)
      return ret
  elif (cards_int[0] % 13) + 1 == cards_int[1] % 13 and (cards_int[1] % 13) + 1 == cards_int[2] % 13 and (cards_int[2] % 13) + 1 == cards_int[3] % 13 and (cards_int[3] % 13) + 1 == cards_int[4] % 13:
      ret = 9.0
      ret = ret + ((int(cards_int[0] / 13)) / 10)
      return ret

  for i in range(13):
      if count[i] == 2:
          for j in range(13):
              if i == j:
                  continue
              elif count[j] == 2:
                  ret = 11.0
                  ret = ret + (13 - (j+1))/100
                  return ret
          ret = 12.0
          ret = ret + (13 - (i+1))/100
          return ret

  ret = 13.0
  max = 0.0
  for i in range(13):
      if count[i] == 1:
          max = (13 - (i+1))/100
  ret = ret + max
  return ret


s = {"AS", "XS", "JS", "QS", "KS"}
print(get_level(s))


class player():
     playerNum = 0
    leftCards={"AS","2S","3S","4S","5S","6S","7S","8S","9S","XS","JS","QS","KS", #남은카드들
              "AH","2H","3H","4H","5H","6H","7H","8H","9H","XH","JH","QH","KH",
              "AD","2D","3D","4D","5D","6D","7D","8D","9D","XD","JD","QD","KD"
              "AC","2C","3C","4C","5C","6C","7C","8C","9C","XC","JC","QC","KC"}
   minLevel=100
    def __init__(self,cards):
      self.set_cards(cards)
      self.playerNum+=1
    
    def set_cards(self,cards): #카드 세팅
      self.cards = cards
      self.leftover()
      
    def leftover(self): #남은카드 정리
      for c in cards:
        self.leftCards.discard(c)
         
    # def backtracking(players): #모든 조합들 시도해보면서 백트래킹
    #     if len(cards) == 7 : #모든 겨
    #     l= get_level(cards)
    #     if(l<min_level) min_level=l
    #     return
    #     for new in self.leftCards:
    #     self.best_comb(cards | {new}) #하나씩 넣기 

    # def best_comb(self): #현재상태에서 가질 수 있는 최고의 조합(level값)찾기
    #   self.minLevel=100
    #   self.backtracking(self.cards)
    #   return self.minLevel


def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def get_best_level(cards):
    ans=10000
    for i in combiantions(cards,5):
        ans=min(ans,get_level(i))
    return ans

def f(playerN, p):
    global res
    if playerN and get_best_level(p[playerN].cards) < my_level : 
        if playerN==2 : res+= ncr(len(p.leftCards),3)
        elif playerN==1 : res+= ncr(len(p.leftCards),3)*ncr(len(p.leftCards)-3,3)
        else res+=1
        return
    if playerN==3:
        return
    for i in combinations(p.leftCards,3)
    p[playerN+1].set_cards(p[playerN+1]+list(i))
    f(playerN+1,p)  
    return  

def win_prob():
    global res
    res=0 #내가 지는 경우의 수
    f(0,p)
    return 1- (res/cnr(33,3)*cnr(30,3)*cnr(27,3)) # (내가이길확률) = 1 - (누군가 다른사람이 이길확률)

 

p=list()

# 플레이어 인스턴스들 생성 -> 프론트랑 합치기
p[0] = player({'AH','XS','4D','JD','7D','7H','8S'}) #나
p[1] = player({'AS','XD','4H','KD'}) #p1
p[2] = player({'2S','QD','5H','KH'}) #p2
p[3] = player({'2S','3D','6H','5D'}) #p3

my_level= get_level(p[0].cards)
print(win_prob(p))

