#make a text based adventure game(escape room) - Mat+hew, Valeri3, Mar@

#player name - Gr0up (maybe get rid of)
#playerName = input("What do you want your characters name to be? \n")

#making variable key count - Gr0up
keyCount = 0
#Room selection - Gr0up
def selRm(void):
    puzzleSel = input("Select a wall(1,2,3,4,End): ")
    if puzzleSel = "End":
        print("You walk over to the door in your room.")
    return f"You walk over to wall {puzzleSel}."
    
#Start - Mar@
print("You awake on a hard bed, and see a door with 4 padlocks. \nInteresting... you look around the room, and you notice 4 corresponding puzzles. \nYou must solve those to get out! Good Luck!")
#Puzzle room 1(riddle) - Mar@
answer1 = input("You look at the first wall and see an engraving in it. It says: What do you bury when it's alive, and dig up when it's dead? Would you like to inspect further?")
if answer1 == "yes":
    solution1 = input("You look closer at the ingraving, and realize that there is a keypad ingraved underneath it. What is the solution?")

    if solution1 == "A plant":
        print("That is correct!The section of concrete the riddle was on slides out and lands on the floor. Inside of it is a key! Good job!!")
        keyCount += 1
    else:
        print("That is not correct :(. Try again.")
else:
    print("You walk away from the puzzle.")
    print(selRm("Start"))
#Puzzle room 2(Unscramble words) - Mat+hew

print("you look around the wall and see some letters opon closer inspection you see they are a scrambled word")
print("the letters on the wall: tnnseqincoialeu")
print("you investigate ferther you find a space to put the correct word")
while True:
    password = input("whats the password ")
    if password == "inconsequential":
        print("you found a key")
        keyCount += 1
        break
    else:
        print("try again")

#Puzzle room 3(morse code) - Mat+hew
    #the anwer will be surreptitious
#Puzzle room 4(Finding messages in plain text) - Valeri3
print("You look around the room and see a letter on the ground. There is also a keypad with letters on the nearby wall.")
inspect = input("Do you want to inspect further?:")
if inspect=="yes":
    print("The letter says: dear Leo. Occasionally, Leah kind of annoys the dog, Luna. \nYou should've fed the Goat by the way. At least you didn't Give the 'thing' away.")
    solution = "Lollygag"
    userThinkSol = input("What is the secret word?:")
    if userThinkSol == solution:
        print("You type in your word on the panel on the wall. Aha! The panel flips over, and on the other side is a key.\n")
        keyCount +=  1
    elif userThinkSol == "lollygag":
        print("You think that's the right word, but something is off.\n")
    else:
        print("You type in your word on the panel on the wall. Oh. Nothing happens\n")
else:
    print(selRm("ef"))
#tthe End - Valeri3
if keyCount==4:
    print("")
else:
    print("Looks like you need more keys.\n")