''' Implement a class called player that represents a cricket player.The player class should have a
method called play() which prints"The players is playing cricket.derive a two classes,Batsman and 
bowler,from the player class.override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling", respectively.write a program to create subjects or both the
Batsman and Bowler classes and call the play () method for each object.'''


# define the base class player 
class player:
       def play(self):
          print ("The player is playing cricket.")

# Define the derived class Batsman
class Batsman(player):
      def play(self):
          print("The batsman is batting.")

# Define the derived class Bowler
class Bowler(player):
       def play(self):
          print("The bowler is bowling.")

# create object of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# call the play() method for each object
batsman.play()
bowler.play()