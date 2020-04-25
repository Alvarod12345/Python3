# BlackJack Game
from random import shuffle

def createDeck():
    deck = []
    facesValues = ["A","J","Q","K"]

    for i in range(4):
        for card in range(2,11):
            deck.append(str(card))
        for card in facesValues:
            deck.append(card)
    shuffle(deck)
    return deck

cardDeck = createDeck()
# print(cardDeck)

class player:
    def __init__(self, hand = [], money = 100):
        self.hand = hand
        self.score = self.setScore()
        print(self.score)
        self.money = money

    def __str__(self):
        currentHand = ""
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + " Score: " + str(self.score) 
        return finalStatus

    def setScore(self):
        self.score = 0
        faceCardDict = {"A":11,"J":10,"Q":10,"K":10,"2":2,
                        "3":3,"4":4,"5":5,"6":6,"7":7,"8":8,
                        "9":9,"10":10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21  and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1

        return self.score

    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()


Player1 = player(["8","10","9"])
print(Player1)

Player1.hit("A")
Player1.hit("A")
print(Player1)

Player1.play(["A","K"])
print(Player1)


    
