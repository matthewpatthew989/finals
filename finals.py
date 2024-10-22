#make a text based adventure game(escape room) - Mat+hew, Valeri3, Mar@

#player name - Gr0up
playerName = input("What do you want your characters name to be? \n")
#key count - Gr0up
keyCount = 0
#Room selection - Gr0up

#Start - Mar@
print("You awake on a hard bed, and see a door with 4 padlocks. \nInteredting... \nAs you look around the room, you notice 4 corresponding puzzles. \nYou must solve those to get out! Good Luck!o")#Puzzle room 1(riddle) - Mar@
#Puzzle room 1(riddle) - Mar@
print("You look at the ")
#Puzzle room 2(Unscramble words) - Mat+hew
print("you look around the room and see some letters opon closer inspection you see they are scrambled words")
print("the letters on the wall: tnnseqincoialeu")
input("do you want top investigate further: type yes or no")
if input == "yes":
    print("you find a space to put the correct word",input("Whats the password"))
    if input == "inconsequential":
        print("you found a key")
        keyCount += 1
    else:
        print("try again")
else:
    print("look around the room!")
#Puzzle room 3(morse code) - Mat+hew
    #the anwer will be surreptitious
#Puzzle room 4(Finding messages in plain text) - Valeri3
print("You look around the room and see a letter on the ground.")
print("It says: dear Leo. Occasionally, Leah kind of annoys the dog, Luna. You should've fed the Goat! At least ")
solution = "Lollygag"
userThinkSol = input("What is the secret word?")
if userThinkSol == solution:
    print("You type in your word on the panel on the wall. Aha! The panel flips over, and on the other side is a key.\n")
    keyCount += 
1
    print("You type in your word on the panel on the wall. Oh. Nothing happens.")
#End - Valeri3\n
if keyCount==4:
    print(""))
else:
    print("Looks like you need more keys.\n")