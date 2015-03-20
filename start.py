import pyglet #to play sound
import sys, os, random, png  #png used for the initial image
from random import randrange #used for music
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
   
   songs = [
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
   #http://stackoverflow.com/questions/21744963/how-to-generate-a-range-of-random-numbers-in-python-without-repetition 
   def createRandomArray():
      for x in range (1, 5):
        ran = random.randint(1, 4)
        while ran in result:
        	 ran = random.randint(1, 4)
        result.append(ran)
      print result

   # Create the sounds when answered correctly or incorrectly
   def buttonSounds(y):
      global player
      player = pyglet.media.Player()

      if (y==1): #plays correct
         correct = pyglet.media.load('sound/correct.mp3', streaming=False)
         player.queue(correct)
      else:      #plays incorrect
         incorrect = pyglet.media.load('sound/wrong.mp3', streaming=False)
         player.queue(incorrect)

   #Plays the song once the Play Song button is clicked
   def theSong(array):
         print "playing song" , array[count]
         songPlayer(array[count])                #takes in the element of the random array
         ran_pitch = random.uniform(0.5, 1.7)    #randomizer for pitch
         if ran_pitch == 1.0:
            ran_pitch = random.uniform(0.5, 1.7) #randomize again if pitch is normal
         music.pitch = ran_pitch
          
         ran_seek = randrange(30,120) #randomizer for song position
         music.seek(ran_seek)         
         timeGAP = music.time + 20    #plays the song for 20 secs
         
         while (music.time < timeGAP): #plays until the 20 secs are up
            music.play()
         music.pause() #ends the song once out of the loop

   # Creates a music player for the songs
   def songPlayer(x):
      global music
      music = pyglet.media.Player()

      if (x==1): #loads the song if it satisfies condition
        sng1 = pyglet.media.load('songs/taylor.mp3', streaming=False)
        music.queue(sng1)

      elif (x==2):
         sng2 = pyglet.media.load('songs/ellie.mp3', streaming=False)
         music.queue(sng2)

      elif (x==3):
         sng3 = pyglet.media.load('songs/glenn.mp3', streaming=False)
         music.queue(sng3)

      elif (x==4):
         sng4 = pyglet.media.load('songs/katy.mp3', streaming=False)
         music.queue(sng4)
   
   # Keep track of score
   # Start the sound
   def thatOne(op, r):
      if op == r :
              y = 1 #if its true
              global score
              score = score + 1
              print "correct"
              check("correct")
              buttonSounds(y)
              player.play()
              
      else :
              y = 0 #if its false
              print "incorrect"
              check("incorrect")
              buttonSounds(y)
              player.play()
              
      print "{}{}{}{}".format("You chose ", op," correct was: ", r)

   #destroy the label
   def removeWidget(label):
      label.destroy()

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
   quit = Button(bottomFrame, text="Quit", command=lambda: exit(), font=("Helvetica", 18))
   quit.pack(side=BOTTOM)

   # Define game feature function
   def game():
      # Destroy the title and play button when game start
      removeWidget(title)
      removeWidget(play)
      removeWidget(quit)

      # Set the size and color of the root window
      root.geometry("%dx%d%+d%+d" % (900, 400, 0, 0))
      root.configure(background='burlywood')

      # destroy everything on the frame and move on to next game
      def nextGame():
        global count
        if count == 4:
           endgame()
        else:
           removeWidget(scoreLabel)
           removeWidget(coverButton1)
           removeWidget(coverButton2)
           removeWidget(coverButton3)
           removeWidget(coverButton4)
           removeWidget(songButton)
           removeWidget(nextButton)
           game()


      # Creates label for displaying scores
      scoreLabel = Label(bottomFrame, text= "Score: " + str(score), font=("Helvetica", 25), background = "peachpuff4")
      scoreLabel.pack(side = TOP)
      counter_label(scoreLabel)

      # Create the 4 album cover buttons
      coverButton1 = createButton("Option1" , 1, albumCover[0])
      createCoverAndPack(coverButton1, 0)

      coverButton2 = createButton("Option2" , 2, albumCover[1])
      createCoverAndPack(coverButton2, 1)

      coverButton3 = createButton("Option3" , 3, albumCover[2])
      createCoverAndPack(coverButton3, 2)

      coverButton4 = createButton("Option4" , 4, albumCover[3])
      createCoverAndPack(coverButton4, 3)
      
      songButton = Button(topFrame, text="Play Song", command=lambda: theSong(result), font=("Helvetica", 16))
      songButton.pack(side=LEFT)
      
      # Create the next question button
      nextButton = Button(topFrame, text="Next Question", command=lambda: nextGame(), font=("Helvetica", 16))
      nextButton.pack(side=LEFT)
     
   def endgame():
      #https://www.daniweb.com/software-development/python/code/260268/restart-your-python-program-
      python = sys.executable
      os.execl(python, python, * sys.argv)
      
   def exit():
      sys.exit()

   #create random array
   createRandomArray()
   root.mainloop()  

main()
