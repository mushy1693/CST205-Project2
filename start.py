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


def main():
   root = Tk()
   can = Canvas(root, width=400, height=400, borderwidth=5, background='white').pack()

   def check(getCheck):

      if(getCheck == "correct"):
        correctLabel = 'correct'
      else:
        correctLabel = 'incorrect'
      
      toplevel = Toplevel()
      label1 = Label(toplevel, text=correctLabel, height=10, width=30)
      label1.pack()
     
   def thatOne(op, ran):

      if op == ran :
              print "correct"
              check("correct")
              player = pyglet.media.Player()
              correct = pyglet.media.load('correct.wav', streaming=False)
              player.queue(correct)
              player.play()
      else :
              print "incorrect"
              check("incorrect")
              player = pyglet.media.Player()
              false = pyglet.media.load('wrong.wav', streaming=False)
              player.queue(false)
              player.play()
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", ran)
      next = Button(root, text="Next Question", command=lambda: game()).pack(side=LEFT)
   
   def game(): 

      ran = random.randrange(1,5) 

      def createButton(response , option):
        return Button(root, text=response, command=lambda: thatOne(option, ran)).pack(side=LEFT)
               
      b1 = createButton("Option1" , 1)
      b2 = createButton("Option2" , 2)
      b3 = createButton("Option3" , 3)
      b4 = createButton("Option4" , 4)
   
   game()
   root.mainloop()  

main()
