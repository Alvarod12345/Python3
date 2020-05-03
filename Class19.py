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
        # print(self.score)
        self.money = money
        self.bet = 0    

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

    def betMoney(self,amount):
        self.money -= amount #bet = 20; money 100 -> 80
        self.bet += amount  # bet 0 -> 20

    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2*self.bet

            self.bet = 0
        else:
            self.bet = 0

    def draw(self):
        self.money += self.bet
        self.bet = 0

    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False

def printHouse(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("House: ","X", end = " ")
        elif card == len(House.hand) - 1:
            print(House.hand[card])
        else:
            print(House.hand[card], end = " ")
            
            
# def test

    # Player1 = player(["8","10","9"])
    # print(Player1)

    # Player1.hit("A")
    # Player1.hit("A")
    # print(Player1)


    # Player1.betMoney(20)
    # print("Your money: ",Player1.money,"Your bet: ", Player1.bet)

    # Player1.win(True)
    # print("You win: ",Player1.money,"Your bet now: ", Player1.bet)


    # Player1.play(["A","K"])
    # print(Player1)
    # Player1.betMoney(20)
    # print("Your bet: ", Player1.bet)
    # Player1.win(True)
    # print("You win", Player1.money)


cardDeck = createDeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]
Player1 = player(firstHand)
House = player(secondHand)
cardDeck = createDeck()

while(True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    
    Player1.play(firstHand)
    House.play(secondHand)

    bet = int(input("Enter your bet: "))
    
    Player1.betMoney(bet)
    printHouse(House)
    print("Player1: ",Player1)

    if Player1.hasBlackJack():
        if House.hasBlackJack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        while(Player1.score < 21):
            action = (input("Do you want another card? (y/n): ").lower())
            if action == "y":
                Player1.hit(cardDeck.pop())
                printHouse(House)
                print("Player1: ",Player1)

            else: 
                printHouse(House)
                print("Player1 : ",Player1)
                break
        
        while(House.score < 16):
            House.hit(cardDeck.pop())
            
        
        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
            else:
                Player1.win(False)
        elif Player1.score > House.score:
            Player1.win(True)
        elif Player1.score == House.score:
            Player1.draw()
        else:
            if House.score > 21:
                Player1.win(True)
            else:
                Player1.win(False)
    print("House: ",House)
    print("Money: ",Player1.money)
