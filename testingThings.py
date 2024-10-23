keyCount = 0
print("you look around the room and see some letters opon closer inspection you see they are a scrambled word")
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
