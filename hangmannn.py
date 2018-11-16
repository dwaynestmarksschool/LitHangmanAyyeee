from turtle import*
from random import randint
import time

wordList = ['extrapolate','appropriate','ciccarello', 'lynchie','steelers', \
            'baguette','sourdough','NERD', 'croquet','crypt', 'lebron',\
            'yeet', 'yeast', 'Bag This Baguette']

sw=600
sh=800
s=getscreen()
s.setup(600,800)
s.bgcolor('#4286f4')
t=getturtle()
t.color('#f40404')
t.width(8)
t.speed(0)

tWriter = Turtle()
tWriter.hideturtle()
tWriter.color("#f4a442")

tBadLetters = Turtle()
tBadLetters.hideturtle()

alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
displayWord=""
secretWord =""
lettersWrong =""
lettersCorrect =""
fails = 6
fontS = int(sh*0.06)
gameDone = False


def displayText(newText):
    print("In displayText newText is " + newText)
    tWriter.clear()
    tWriter.penup()
    #                   x               y
    #tWriter.goto( -int(sw*0.4), -int(sh*0.50) )
    # 0.5 is too much for the y coordinate  try 0.44 see below
    tWriter.goto( -int(sw*0.4), -int(sh*0.44) )
    tWriter.write(newText, font = ('Arial' ,fontS, 'bold'))

def displayBadLetters(newText):
    print("In displayText newText is " + newText)
    tBadLetters.clear()
    tBadLetters.penup()
    #                   x               y
    #tWriter.goto( -int(sw*0.4), -int(sh*0.50) )
    # 0.5 is too much for the y coordinate  try 0.44 see below
    tBadLetters.goto( -int(sw*0.4), int(sh*0.44) )
    tBadLetters.write(newText, font = ('Arial' ,fontS, 'bold'))


    
def chooseWord():
    global secretWord
    secretWord = wordList[randint(0,len(wordList)-1)]
    print("The secret word is " + secretWord)


def makeDisplay():
    global displayWord, secretWord, lettersCorrect
    displayWord = ""
    for letter in secretWord:
        if letter in alpha:
            if letter.lower() in lettersCorrect.lower():
                displayWord += letter + " "
            else:
                displayWord += "_" + " "
    
        
        else:
            displayWord += letter + " "

def getGuess():
    boxTitle = "Letters Used: " + lettersWrong
    guess = s.textinput(boxTitle, "Enter a guess or type  $$ to guess the word")
    return guess
def updateHangmanPerson():
    global fails
    if fails == 5:
        drawHead()
    if fails ==4:
        drawTorso()
    if fails == 3:
        drawRLeg()
    if fails == 2:
        drawLLeg()
    if fails == 1:
        drawRArm()
    if fails == 0:
        drawLArm()

def checkWordGuess():
    global gameDone, fails
    boxTitle = "Guess the Word!!!"
    guess = s.textinput(boxTitle, "Enter yout guess here..")
    if guess.lower() == secretWord.lower():
        displayText("Congratulations!! " + secretWord + " is the word!")
        gameDone = True
    else:
        displayText("SMH " + guess + " ain't it chief!")
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangmanPerson()

def playGame():
    global fails, lettersCorrect, lettersWrong, alpha, gameDone
    while gameDone == False and fails > 0 and "_" in displayWord:

        theGuess = getGuess()

        if theGuess == "$$":
            checkWordGuess()

        elif  len(theGuess) > 1 or theGuess  == "":
            displayText("No! " + theGuess + " should be one letter please")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess  not in alpha:
            displayText("No! " + theGuess + " not a letter")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeDisplay()
            displayText(displayWord)
        elif theGuess.lower() not in lettersWrong.lower():
            displayText("No " + theGuess + " is not in the word")
            time.sleep(1)
            lettersWrong += theGuess.lower() + ", "
            displayBadLetters("That aint it chief: {" + lettersWrong + "}")
            displayText(displayWord)
            fails -= 1
            updateHangmanPerson()
        else:
            displayText("No " + theGuess + " has already been used")
            time.sleep(1)
            displayText(displayWord)
        if fails <= 0:
            displayBadLetters("No more guesses")
            displayText("You Lose. Word is : " + secretWord)
            gameDone = True
        if "_" not in displayWord:
            displayBadLetters("You got it!!!!!!")
            gameDone = True

    
            
   

def drawGallows():
    t.penup()
    t.goto(-int(sw/4), -int(sh/4) )
    t.pendown()
    t.forward(int(sw/2) )
    t.left(180)
    t.forward(60)
    t.right(90)
    t.forward(400)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.forward(40)


def drawHead():
  hr = int(sw*0.07)
  t.penup()
  t.goto(t.xcor()-hr, t.ycor()-hr)
  t.pendown()
  t.circle(hr)

  t.penup()
  t.goto(t.xcor()+hr, t.ycor()-hr)
  







def drawTorso():
    t.penup()
    t.pendown()
    t.forward(int(sh*0.2) )
   







def drawRLeg():
    t.left(40)
    t.forward(80)
    




def drawLLeg():
    t.right(180)
    t.forward(80)
    t.right(260)
    t.forward(80)




def drawRArm():
    t.backward(80)
    t.right(140)
    t.forward(80)
    t.right(30)
    t.forward(60)

    
def drawLArm():
    t.backward(60)
    t.left(60)
    t.forward(60)

    
#this is the wrong place
#displayText("Have a nice day")
drawGallows()
drawHead()
drawTorso()
drawRLeg()
drawLLeg()
drawRArm()
drawLArm()

t.clear()
time.sleep(1)
t.right(120)
drawGallows()
chooseWord()
makeDisplay()
displayText(displayWord)
displayBadLetters("That aint it chief: {" + lettersWrong + "}")
playGame()
