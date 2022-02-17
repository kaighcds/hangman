
from drawing import drawing
import turtle
import random


  wordsThings = ["fork","shoe","chair","hammer","wall","cord"]
  


  word = random.word(wordsThings)
  return word

height = 300
width = 500
myWindow = turtle.setup(width,height)
myWindow = turtle.Screen()
myWindow.bgcolor("light blue")
myWindow.title("My Hangman")
myWindow.reset() 
Pen = turtle.Turtle()
drawing(Pen,0)
drawing(Pen,1)
drawing(Pen,2)
wordsThings = initgame() 
words = chooseword(wordsThings)
print(words)

 def printword(word,Letters):