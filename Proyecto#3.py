"""

"""

from random import shuffle

def createDeck():
    deck = []
    facesValues = ["A","J","Q","K","Jk"] # A = 1, J = 11, Q = 12, K = 13, JK = 14

    for i in range(4):
        for card in range(2,11):
            deck.append(str(card))
        for card in facesValues:
            deck.append(card)
    shuffle(deck)
    return deck

cardDeck = createDeck()

class player:
    def __init__(self,name="",hand = [],money = 50):
        self.name = name
        self.hand = hand
        self.score = self.setScore()
        self.money = money
        self.bet = 0
        
    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += card + " " 
        finalStatus = self.name + " cards: " + currentHand
        return finalStatus        

    def setScore(self):
        self.score = 0        
        faceCardDict = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,
                        "7":7,"8":8,"9":9,"10":10,"J":11,
                        "Q":12,"K":13,"JK":14}
        for card in range(1,14):
            if self.hand[-1] == card:
                self.score += 5
                print(self.hand)
            else:
                continue
        return self.score
    
    def hit(self,card):
        self.hand.append(card)

    def play(self,newHand):
        self.hand = newHand
        
    def betMoney(self,amount):
        self.money -= amount
        self.bet += amount

    def win(self,result):
        if result == True:
            if cardDeck == 0:
                self.money += self.bet
            else:
                self.money -= self.bet
            self.bet = 0
        else:
            self.bet = 0
            self.money -= self.bet

name1 = str(input("Enter your name: "))
Player1 = player(name1)
bet1 = int(input("Enter your bet: "))
Player1.betMoney(bet1)

name2 = str(input("Enter your name: "))
Player2 = player(name2)
bet2 = int(input("Enter your bet: "))
Player2.betMoney(bet2)

Player1Hand = [cardDeck.pop()]
Player2Hand = [cardDeck.pop()]

Player1 = player(name1,Player1Hand)
print(Player1, end = "\n")
Player2 = player(name2,Player2Hand)
print(Player2, end = "\n\n")

while(len(cardDeck)> 0): 
    print(name1)
    action = str(input("Do you want hit a card? (y/n)").lower())
    if action == "y":
        Player1 = player(name1,Player1Hand)
        Player1.hit(cardDeck.pop())
        print(Player1, end = "\n\n")
    else:
        break
    
    print(name2)
    action = str(input("Do you want hit a card? (y/n)").lower())
    if action == "y":
        Player2 = player(name2,Player2Hand)
        Player2.hit(cardDeck.pop())
        print(Player2, end = "\n\n")
    else:
        break

    if Player1.hand < 1:
        if Player2.hand > 2:
            Player1.win(True)
        else:
            Player2.win(True)
    print(name1,Player1.money)