import pyglet #to play sound
import sys, random, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing

count = 0

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

   def randomizer():
      global count 
      count += 1
      return randomization(count)    

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

   def createButton(response , option):
      return Button(root, image = photo, text=response, command=lambda: thatOne(option, randomizer()))
   
   def thatOne(op, ran):
      if op == ran :
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
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", ran)
      next = Button(root, text="Next Question", command=lambda: game()).pack(side=LEFT)
   
   def game(): 
                
      play = Button(root, text="Play").pack(side=TOP)

      b1 = createButton("Option1" , 1)
      b1.image = photo
      b1.pack(side=LEFT) 

      b2 = createButton("Option2" , 2)
      b2.image = photo
      b2.pack(side=LEFT)

      b3 = createButton("Option3" , 3)
      b3.image = photo
      b3.pack(side=LEFT)

      b4 = createButton("Option4" , 4)
      b4.image = photo
      b4.pack(side=LEFT)
   
   game()
   root.mainloop()  

main()
