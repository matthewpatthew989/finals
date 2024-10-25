#make a text based adventure game(escape room) - Mat+hew, Valeri3, Mar@

#making variable key count - Gr0up
keyCount = 0
    
#Start - Mar@
print("You awake on a hard bed, and see a door with 4 padlocks. \nInteresting... you look around the room, and you notice 4 corresponding puzzles. \nYou must solve those to get out! Good Luck!")
    
#Puzzle room 1(riddle) - Mar@
def Rm1(void):
    global keyCount
    print("You look at the first wall and see an engraving in it. It says: What do you bury when it's alive, and dig up when it's dead?")
    
    while True:
        solution1 = input("What is the solution?(NO CAPITALS)")
        if solution1 == "a plant":
            print("That is correct!The section of concrete the riddle was on slides out and lands on the floor. Inside of it is a key! Good job!!")
            keyCount += 1
            break
        else:
            print("That is not correct :(. Try again.")
    selRm("bibity bobity boo")
#Puzzle room 2(Unscramble words) - Mat+hew
def Rm2(void):
    global keyCount
    print("you look around the wall and see some letters opon closer inspection you see they are a scrambled word")
    print("the letters on the wall: tnnseqincoialeu")
    print("you investigate farther you find a space to put the correct word")
    while True:
        password = input("whats the password ")
        if password == "inconsequential":
            print("you found a key")
            keyCount += 1
            break
        else:
            print("try again")
    selRm("vbids")
#Puzzle room 3(morse code) - Mat+hew
def Rm3(void):
    global keyCount
    print("you see some puculear dots and dashes on the wall")
    print("the dots and dashes on the wall: ... ..- .-. .-. . .--. - .. - .. --- ..- ...")
    print("you find a place to put the password")
    #the anwer will be surreptitious
    while True:
        password = input("whats the password ")
        if password == "surreptitious":
            print("you found a key")
            keyCount += 1
            break
        else:
            print("try again")
    selRm("dbsihh")        
#Puzzle room 4(Finding messages in plain text) - Valeri3
def Rm4(void):
    global keyCount
    print("You look around the room and see a letter on the ground. There is also a keypad with letters on the nearby wall.")
    print("The letter says: dear Leo. Occasionally, Leah kind of annoys the dog, Luna. \nYou should've fed the Goat by the way. At least you didn't Give the 'thing' away.")
    while True:
        solution = "Lollygag"
        userThinkSol = input("What is the secret word?:")
        if userThinkSol == solution:
            print("You type in your word on the panel on the wall. Aha! The panel flips over, and on the other side is a key.\n")
            keyCount +=  1
            break
        elif userThinkSol == "lollygag":
            print("You think that's the right word, but something is off.\n")
            break
        else:
            print("You type in your word on the panel on the wall. Oh. Nothing happens\n")
    selRm("abcdefg")
    #the End - Valeri3
def end(void):
    global keyCount
    if keyCount==4:
        print("You use the keys on their corresponding padlocks. Then you open the door to the room. \nYou finally exit the building, and see a city in the distance. Time to go home...")
    elif keyCount > 4:
        print("How'd you get several keys!? Did you bring like, a copy machine or something!? \nYou cheater. Restart the game again and DO. IT. RIGHT.")
    else:
        print("Looks like you need more keys.\n")
        selRm("BOO!")

#Room selection - Gr0up
def selRm(void):
    while True:
        puzzleSel = input("Select a wall(1,2,3,4,end): ")
        if puzzleSel == "end" or puzzleSel == "End":
            print("You walk over to the door in your room.")
            end(void)
            break
        elif puzzleSel == "1":
            Rm1(void)
            break
        elif puzzleSel == "2":
            Rm2(void)
            break
        elif puzzleSel == "3":
            Rm3(void)
            break
        elif puzzleSel == "4":
            Rm4(void)
            break
        else:
            print("That room doesn't exist dummy.")
    return f"You walk over to wall {puzzleSel}."
selRm("why not wooooooo")