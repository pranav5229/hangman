import time
import random
name = input("What is your name? ")
print ("Hello, " + name, "Time to play hangman!")
time.sleep(1)
print ("Start guessing...\n")
time.sleep(0.5)
## A List Of Secret Words
words = ["january","border","image","film","promise","kids","lungs","doll","rhyme","damage"
                   ,"plants"]
word = random.choice(words)
guesses = ''
turns = 5
while turns > 0:
      if turns == 5:
            # time.sleep(1)
            print("   _____ \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
      elif turns == 4:
            # time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
      elif turns == 3:
        #    time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     | \n"
                 "  |      \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
      elif turns == 2:
            # time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
      elif turns == 1:
            # time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "__|__\n")
      failed = 0             
      for char in word:      
          if char in guesses:    
              print (char,end="")    
          else:
              print ("_",end=""),     
              failed += 1    
      if failed == 0:        
          print ("\nYou won") 
          break              
      print("\n\nYou have", + turns, 'more guesses') 
      guess = input("\nguess a character:") 
      guesses += guess                    
      if guess not in word:  
          turns -= 1        
          print("\nWrong")    
          print("\nYou have", + turns, 'more guesses') 
          if turns == 0:  
              print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")        
              print ("\nYou are Hanged") 