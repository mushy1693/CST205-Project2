import pyglet #to play sound
import sys, random#, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing

#player = pyglet.media.Player()
#correct = pyglet.media.load('correct.wav', streaming=False)
#incorrect = pyglet.media.load('wrong.wav', streaming=False)
#player.queue(correct)
#player.queue(incorrect)

count = 0

def main():
   root = Tk()
   can = Canvas(root, width=400, height=400, borderwidth=5, background='white').pack()
   result = []
   
   for x in range (1, 5):
       ran = random.randint(1, 4)
       while ran in result:
        	ran = random.randint(1, 4)
       result.append(ran)
   print result   
   
   def randomization(c):
      c = c-1
      num = result[c]
      return num
   
   def thatOne(op, ran):
      if op == ran :
              print "correct"
              player = pyglet.media.Player()
              correct = pyglet.media.load('correct.wav', streaming=False)
              player.queue(correct)
              player.play()
      else :
              print "incorrect"
              player = pyglet.media.Player()
              false = pyglet.media.load('wrong.wav', streaming=False)
              player.queue(false)
              player.play()
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", ran)
      next = Button(root, text="Next Question", command=lambda: game()).pack(side=LEFT)
   
   def game():  
      global count 
      count += 1
      ran = randomization(count)                   
      b1 = Button(root, text="Option1", command=lambda: thatOne(1, ran)).pack(side=LEFT)
      b2 = Button(root, text="Option2", command=lambda: thatOne(2, ran)).pack(side=LEFT)
      b3 = Button(root, text="Option3", command=lambda: thatOne(3, ran)).pack(side=LEFT)
      b4 = Button(root, text="Option4", command=lambda: thatOne(4, ran)).pack(side=LEFT)
   
   game()
   root.mainloop()  

main()
