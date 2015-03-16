import pyglet #to play sound
import sys, random, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing

count = 0
theAnswer = 0

def main():
   root = Tk()
   can = Canvas(root, width=400, height=400, borderwidth=5, background='white').pack()
   
   photo=PhotoImage(file="pic/Blank-Space.gif")

   def check(getCheck):

      if(getCheck == "correct"):
        correctLabel = 'correct'
      else:
        correctLabel = 'incorrect'
      
      toplevel = Toplevel()
      label1 = Label(toplevel, text=correctLabel, height=10, width=30)
      label1.pack()  

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

   def buttonSounds():
      global player
      player = pyglet.media.Player()
      correct = pyglet.media.load('sound/correct.wav', streaming=False)
      incorrect = pyglet.media.load('sound/wrong.wav', streaming=False)
      player.queue(correct)
      player.queue(incorrect)
   
   def thatOne(op, r):
      if op == r :
              print "correct"
              check("correct")
              buttonSounds()
              player.play()
              
      else :
              print "incorrect"
              check("incorrect")
              buttonSounds()
              player.next()
              player.play()
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", r)
   
   def game(): 

      global count 
      count += 1
      global theAnswer
      theAnswer = randomization(count) 
                
   play = Button(root, text="Play").pack(side=TOP)

   b1 = Button(root, image=photo, command=lambda: thatOne(1, theAnswer))
   b1.image = photo
   b1.pack(side=LEFT) 

   b2 = Button(root, image=photo, command=lambda: thatOne(2, theAnswer))
   b2.image = photo
   b2.pack(side=LEFT)

   b3 = Button(root, image=photo, command=lambda: thatOne(3, theAnswer))
   b3.image = photo
   b3.pack(side=LEFT)

   b4 = Button(root, image=photo, command=lambda: thatOne(4, theAnswer))
   b4.image = photo
   b4.pack(side=LEFT)
      
   next = Button(root, text="Next Question", command=lambda: game())
   next.pack(side=LEFT)
   
   game()
   root.mainloop()  

main()
