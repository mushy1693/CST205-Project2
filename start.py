import pyglet #to play sound
import sys, random, png #png used for the initial image
from Tkinter import * #all for convenience 
from PIL import Image, ImageTk, ImageOps 
#Image is Pillow, ImageTK is the way to use images within tkinter, ImageOps used to work with the image after resizing

# initialize the variables
count = 0
theAnswer = 0
score = 0
result = []

def main():

   # Creates root frame and gives it a dimension and background color
   root = Tk()
   root.geometry("%dx%d%+d%+d" % (400, 400, 0, 0))
   root.configure(background='deepskyblue2')

   # Creates the top Frame
   topFrame = Frame(root)
   topFrame.pack(side = TOP)

   # creates the bottom Frame
   bottomFrame = Frame(root, bg = "peachpuff4")
   bottomFrame.pack(side = BOTTOM)

   # Holds all the album cover
   albumCover = [

      PhotoImage(file="pic/Blank-Space.gif"),
      PhotoImage(file="pic/fifty-shades.gif"),
      PhotoImage(file="pic/goodbye.gif"),
      PhotoImage(file="pic/kate-perry.gif")

   ]

   # Check to see if the album is correct or incorrect
   # Show popup alerting user the result they got
   def check(getCheck):

      if(getCheck == "correct"):
        correctLabel = 'correct'
      else:
        correctLabel = 'incorrect'
      
      toplevel = Toplevel()
      label1 = Label(toplevel, text=correctLabel, height=10, width=30, background = "tan4")
      label1.pack()
   
   # Creates a random array to hold music test values 
   def createRandomArray():
      for x in range (1, 5):
        ran = random.randint(1, 4)
        while ran in result:
        	 ran = random.randint(1, 4)
        result.append(ran)
      print result   

   # Create the sounds when answered correctly or incorrectly
   def buttonSounds():
      global player
      player = pyglet.media.Player()
      correct = pyglet.media.load('sound/correct.wav', streaming=False)
      incorrect = pyglet.media.load('sound/wrong.wav', streaming=False)
      player.queue(correct)
      player.queue(incorrect)
   
   # Keep track of score
   # Start the sound
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

   # Keep track of when the scores changes the label will update every second
   def counter_label(label):
      def count():
        global score
        label.config(text= "Score: " + str(score))
        label.after(1000, count)
      count()

   # Create a cover button
   def createButton(response , option, album):
      return Button(bottomFrame, image = album, text=response, command=lambda: thatOne(option, randomizer()))

   # Increase the count each time and pass the first song to the randomizer
   def randomizer():
      global count 
      count += 1
      global theAnswer
      return randomization(count)

   # Return the number at the random array
   def randomization(c):
      c = c-1
      num = result[c]
      return num

   # Save the album cover object and package the button the the left
   def createCoverAndPack(button, coverIndex):
      button.image = albumCover[coverIndex]
      button.pack(side=LEFT)

   # Create main title
   title = Label(topFrame, text= "Music Trivia", font=("Helvetica", 40), height = 5 , background = "goldenrod4")
   title.pack(side = TOP)

   # Create play button
   play = Button(bottomFrame, text="Play", command=lambda: game(), font=("Helvetica", 18))
   play.pack(side=TOP)

   # Define game feature function
   def game():

      # Destroy the title and play button when game start
      title.destroy()
      play.destroy()

      # Set the size and color of the root window
      root.geometry("%dx%d%+d%+d" % (900, 400, 0, 0))
      root.configure(background='burlywood')

      # destroy everything on the frame and move on to next game
      def nextGame():

        l1.destroy()
        b1.destroy()
        b2.destroy()
        b3.destroy()
        b4.destroy()
        next.destroy()
        game()

      # Creates label for displaying scores
      l1 = Label(bottomFrame, text= "Score: " + str(score), font=("Helvetica", 25), background = "peachpuff4")
      l1.pack(side = TOP)
      counter_label(l1)

      # Create the 4 album cover buttons
      b1 = createButton("Option1" , 1, albumCover[0])
      createCoverAndPack(b1, 0)

      b2 = createButton("Option2" , 2, albumCover[1])
      createCoverAndPack(b2, 0)

      b3 = createButton("Option3" , 3, albumCover[2])
      createCoverAndPack(b3, 0)

      b4 = createButton("Option4" , 4, albumCover[3])
      createCoverAndPack(b4, 0)
      
      # Create the next question button
      next = Button(topFrame, text="Next Question", command=lambda: nextGame(), font=("Helvetica", 16))
      next.pack(side=LEFT)

   #create random array
   createRandomArray()
   root.mainloop()  

main()
