import pyglet #to play sound
import sys, random, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing

count = 0
theAnswer = 0
score = 0

def main():

   root = Tk()
   can = Canvas(root, width=400, height=400, borderwidth=5, background='white').pack()

   albumCover = [

      PhotoImage(file="pic/Blank-Space.gif"),
      PhotoImage(file="pic/fifty-shades.gif"),
      PhotoImage(file="pic/goodbye.gif"),
      PhotoImage(file="pic/kate-perry.gif")

   ]

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
              global score
              score = score + 1
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
   
   def randomizer():
      global count 
      count += 1
      global theAnswer
      return randomization(count)

   def createButton(response , option, album):
      return Button(root, image = album, text=response, command=lambda: thatOne(option, randomizer()))

   def game():

      def nextGame():

        play.destroy()
        l1.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        next.destroy()
        game()

      play = Button(root, text="Play")
      play.pack(side=TOP)

      l1 = Label(root, text= "Score: " + str(score))
      l1.pack(side = TOP)

      b1 = createButton("Option1" , 1, albumCover[0])
      b1.image = albumCover[0]
      b1.pack(side=LEFT)

      b2 = createButton("Option2" , 2, albumCover[1])
      b2.image = albumCover[1]
      b2.pack(side=LEFT)

      b3 = createButton("Option3" , 3, albumCover[2])
      b3.image = albumCover[2]
      b3.pack(side=LEFT)

      b4 = createButton("Option4" , 4, albumCover[3])
      b4.image = albumCover[3]
      b4.pack(side=LEFT)  
        
      next = Button(root, text="Next Question", command=lambda: nextGame())
      next.pack(side=LEFT)
  
   game()
   root.mainloop()  

main()
