#importing relevant libraries
from colorama import Fore
import random

#lists and variables
alreadyGuessed = []
incorrectLetters = []
guessed = False
y = 1

#functions:
#function to select category:
def chooseCategory():
  #At least 20 different words per category
  #The word will be picked at random by computer from the user's chosen category
  print ("Here are the categories available:")
  print ("1. CITIES")
  print ("2. OBJECTS")
  print ("3. ANIMALS")
  print ("4. FOOD")
  print ("5. SPORTS")
  c = int(input("Please choose  a category: "))
  global cat
  if c == 1:
    print ()
    print ("You have chosen CITIES as your category!")
    cat = ["toronto", "mumbai", "atlanta", "singapore", "london", "chicago", "paris", "stokholm", "berlin", "athens", "venice", "seoul", "shanghai", "moscow", "orlando", "vancouver", "dubai", "nairobi", "tokyo", "barcelona"]   
  elif c == 2:
    print ()
    print ("You have chosen OBJECTS as your category!")
    cat = ["computer", "paper", "chair", "scissors", "table", "sandals", "towel", "plate", "spoon", "bottle", "glass", "socks", "shirt", "pants", "gloves", "couch", "pencil", "crayon", "folder", "phone"]
  elif c == 3:
    print ()
    print ("You have chosen ANIMALS as your category!")
    cat = ["dog", "cat", "camel", "elephant", "octopus", "giraffe", "zebra", "rhinoceros", "snake", "shark", "tiger", "leopard", "peacock", "moose", "beaver", "chicken", "sheep", "cow", "horse", "gazelle", "panda", "koala", "kangaroo", "squirrel"]
  elif c == 4:
    print ()
    print ("You have chosen FOOD as your category!")
    cat = ["cereal", "yogurt", "bread", "lasagna", "pizza", "hamburger", "sorbet", "samosa", "dumpling", "pepperoni", "popcorn", "sandwich", "cracker", "noodles", "salami", "chocolate", "spaghetti", "meatball", "cheese", "croissant", "salad"]
  elif c == 5:
    print ()
    print ("You have chosen SPORTS as your category!")
    cat = ["soccer", "baseball", "basketball", "hockey", "swimming", "lacrosse", "cricket", "fencing", "archery", "skiing", "skating", "tennis", "badminton","volleyball", "football", "curling", "boxing", "bowling", "dodgeball", "handball", "golf"]
#function to create graphics of the game
def updateGraphics():
  if m == 0:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("       |             \ ||           ")
    print ("                      \||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
  elif m == 1:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |o o|            \||           ")
    print ("     |_-_|             ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
  elif m == 2:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |o o|            \||           ")
    print ("     |_-_|             ||           ")
    print ("       |               ||           ")
    print ("       |               ||           ")
    print ("       |               ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
  elif m == 3:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |o o|            \||           ")
    print ("     |_-_|             ||           ")
    print ("       |               ||           ")
    print ("      /|               ||           ")
    print ("     / |               ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
  elif m == 4:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |o o|            \||           ")
    print ("     |_-_|             ||           ")
    print ("       |               ||           ")
    print ("      /|\              ||           ")
    print ("     / | \             ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
  elif m == 5:
    print ("        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |o o|            \||           ")
    print ("     |_-_|             ||           ")
    print ("       |               ||           ")
    print ("      /|\              ||           ")
    print ("     / | \             ||           ")
    print ("       |               ||           ")
    print ("      /                ||           ")
    print ("     /                 ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
  elif m == 6:
    print (Fore.RED + "        ________________            ")
    print ("       |            \  ||           ")
    print ("      _|_            \ ||           ")
    print ("     |x x|            \||           ")
    print ("     |_^_|             ||           ")
    print ("       |               ||           ")
    print ("      /|\              ||           ")
    print ("     / | \             ||           ")
    print ("       |               ||           ")
    print ("      / \              ||           ")
    print ("     /   \             ||           ")
    print ("                       ||           ")
    print ("                       ||           ")
    print ("                     __||__         ")
    print()
    print ("Incorrect Letters: {}".format(incorrectLetters))
#function to choose a game mode
def chooseGamemode():
  global gm
  print ("Please choose a gamemode:")
  print ()
  print (Fore.GREEN + "BEGINNER Mode")
  print (Fore.LIGHTRED_EX + "ADVANCED Mode")
  print ()
  print (Fore.WHITE + "BEGINNER mode will start with one letter revealed.")
  print ("ADVANCED mode will start with no letters revealed.")
  gm = int(input("Enter 0 to play BEGINNER mode or enter 1 to play ADVANCED mode: "))
  print ()
#function to play the game
def playGame(gm):
  global m
  m = 0
  d = 0
  spaces = space1
  spacelist = list(spaces)
  while d < 1:
    g = input(Fore.WHITE + "Please guess a letter: ")
    #making sure that the guess is valid
    if len(g) != 1:
      print ("Please enter one letter at a time.")
      print ()
    elif g in alreadyGuessed:
      print ("You already guessed this letter try again.")
      print ()
    elif g not in 'qwertyuiopasdfghjklzxcvbnm':
      print ("Please enter a letter.")
      print ()
    else:
      alreadyGuessed.append(g)
      if g in yourWord:
        print ("Great guess, {} is in the word!".format(g))
        #converting the word to a list
        listword = list(yourWord)   
        #finds positions of the guess in the wordlist
        indices = [i for i, x in enumerate(listword) if x == g]
        #replaces those positions in the space list with the guess
        for index in indices:
          spacelist[index] =  g
        #converting the spacelist back into the variable
        spaces = ''.join(spacelist)
        print ()
        updateGraphics()
        print ()
        print ()
        print (Fore.LIGHTYELLOW_EX + (spaces))
        if "_" in spaces:
          print()
        else:
          print (Fore.GREEN + "        ________________            ")
          print ("       |            \  ||            ")
          print ("       |             \ ||            ")
          print ("                      \||            ")
          print ("                       ||            ")
          print ("                       ||            ")
          print ("                       ||       ___  ")
          print ("                       ||      |o o| ")
          print ("                       ||      |_v_| ")
          print ("                       ||     \  |  /")
          print ("                       ||      \_|_/ ")
          print ("                       ||        |   ")
          print ("                       ||       / \  ")
          print ("                     __||__    /   \ ")
          #deleting these lists so next round will have them empty
          del alreadyGuessed[:]
          del incorrectLetters[:]
          print ()
          print (Fore.LIGHTYELLOW_EX + "Congratulations, you guessed the correct word!")
          d += 1
      else:
        print ("Sorry, {} is not in the word!".format(g))
        incorrectLetters.append(g)
        m += 1
        print ()
        updateGraphics()        
        print ()
        print () 
        print (Fore.LIGHTYELLOW_EX + (spaces))
        print ()
        if m == 6:
          del alreadyGuessed[:]
          del incorrectLetters[:]
          print ("You lost! The word was: {}".format(yourWord))
          print ("Better luck next time...")
          break     

#main game
print ("Welcome to Hangman!")
#game loop
while y == 1:
  chooseGamemode()
  chooseCategory()
  yourWord = random.choice(cat)
  global nol
  nol = 0
  for char in yourWord:
    nol += 1
  print ()
  print ()
  if gm == 0:
    space1 = "_" * (nol)
    listspace1 = list(space1)
    listword1 = list(yourWord)
    u = random.choice(listword1)
    indices1 = [i for i, x in enumerate (listword1) if x == u]
    for index in indices1:
      listspace1[index] =  u
      space1 = ''.join(listspace1)
    print (Fore.LIGHTYELLOW_EX + (space1))
    print ()
    print (Fore.LIGHTCYAN_EX + "This is a {} letter word".format(nol))
    playGame(gm)
  elif gm == 1:
    space1 = "_" * (nol)
    print (Fore.LIGHTYELLOW_EX + (space1))
    print ()
    print (Fore.LIGHTCYAN_EX + "This is a {} letter word".format(nol))
    playGame(gm)
  print ()
  print (Fore.WHITE + "Would you like to play again? ")
  u = int(input("Please type 0 for yes, or type 1 for no: "))
  if y+u == 1:
    print(gm)
  else:
    print ("Thanks for playing!")
    break