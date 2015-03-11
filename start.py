import pyglet #to play sound
import sys, random#, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing


def main():
   root = Tk()
   can = Canvas(root, width=400, height=400, borderwidth=5, background='white').pack()
   
   def thatOne(op, ran):
      player = pyglet.media.Player()
#      song.play()
#      pyglet.app.run()

      if op == ran :
              print "correct"
              correct = pyglet.media.load('correct.wav', streaming=False)
              player.queue(correct)
              player.play(correct)
      else :
              print "incorrect"
              false = player.load('correct.wav', streaming=False)
              player.queue(false)
              player.play(false)
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", ran)
      next = Button(root, text="Next Question", command=lambda: game()).pack(side=LEFT)
   
   def game():  
      ran = random.randrange(1,5)   
      #if ran = prev:
              #ran = random.randrange(1,5)
      #else:                  
      b1 = Button(root, text="Option1", command=lambda: thatOne(1, ran)).pack(side=LEFT)
      b2 = Button(root, text="Option2", command=lambda: thatOne(2, ran)).pack(side=LEFT)
      b3 = Button(root, text="Option3", command=lambda: thatOne(3, ran)).pack(side=LEFT)
      b4 = Button(root, text="Option4", command=lambda: thatOne(4, ran)).pack(side=LEFT)
   
   game()
   root.mainloop()  

main()
