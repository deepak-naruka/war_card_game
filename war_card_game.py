import random

Faces=["clubs","diamond","heart","spade"]
Faceof=("two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace")
Values={"two":1,"three":2,"four":3,"five":4,"six":5,"seven":6,"eight":7,"nine":8,"ten":9,"jack":10,"queen":11,"king":12,"ace":13}
class card():
    def __init__(self,Faces,Faceof):
        self.face=Faces
        self.faceof=Faceof
        self.value=Values[Faceof]

    def __str__(self) :
        return self.face+"'s "+ self.faceof

card1=card("diamond","three")
print(card1)


class packet():
    def __init__(self) :
        self.allcards=[]
        for x in Faces:
            for y in Faceof:
                newcard=card(x,y)
                self.allcards.append(newcard)

    def dealone(self):
        return self.allcards.pop()

    def suffcard(self):
        random.shuffle(self.allcards)

    def __str__(self) :
        return str(len(self.allcards))


class player():
    def __init__ (self,name) :
        self.name=name
        self.playerallcard=[]

    def remove(self):
        return self.playerallcard.pop(0)

    def addcard(self,adcard):
        if type(adcard)==type([]):
            self.playerallcard.extend(adcard)
        else:
            self.playerallcard.append(adcard)

    def __str__(self):
        return f"{self.name} has {len(self.playerallcard)}"

newpac=packet()
newpac.suffcard()
p1=player("player1")
p2=player("player2")
for x in range(26):
    p1.addcard(newpac.dealone())
    p2.addcard(newpac.dealone())


game=True
round=0
while game:
    round +=1
    print(f"round : {round}")

    if len(p1.playerallcard) == 0 :
        print(f" {p1.name} has no card left so {p2.name} won this match")
        game=False
        break

    elif len(p2.playerallcard) == 0 :
        print(f" {p2.name} has no card left so {p1.name} won this match")
        game=False
        break




    gamecard1=[]
    gamecard1.append(p1.remove())
    gamecard2=[]
    gamecard2.append(p2.remove())





    war=True
    while war :


        if gamecard1[-1].value > gamecard2[-1].value:
            p1.addcard(gamecard1)
            p1.addcard(gamecard2)
            war = False

        elif gamecard1[-1].value < gamecard2[-1].value:
            p2.addcard(gamecard1)
            p2.addcard(gamecard2)
            war = False


        else :
            print("war!")
            if len(p1.playerallcard) <5:
                print(f"{p1.name} is out of card during war so {p2.name} won")
                game= False
                break


            elif len(p2.playerallcard) <5:
                print(f"{p2.name} is out of card during war so {p1.name} won")
                game=False
                break
            else:
                for y in range(5):
                    gamecard1.append(p1.remove())
                    gamecard2.append(p2.remove())
