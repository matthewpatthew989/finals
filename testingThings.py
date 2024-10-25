keyCount = 0    
    while True:
            password = input("whats the password ")
            if password == "surreptitious":
                print("you found a key")
                keyCount += 1
                break
            else:
                print("try again")