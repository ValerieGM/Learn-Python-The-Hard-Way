print("""You enter a dark room with 2 doors.
        Do you go through door #1 or door #2""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating acheese cake")
    print("What do you do?!")
    print("1) Take the cake")
    print("2) Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Well done!!!")
    elif bear == "2":
        print("The bear eats your legs off. Well done!!!")
    else:
        print(f"Well, doing {bear} is probably better")
        print("Bear runs away")

elif door == "2":
    print("You stare into the endless abyss. What do you see?!?!")
    print("1) Blueberries")
    print("2) Yellow Jacket Clothespins")
    print("3) Understanding Revolvers Yelling Melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello\nWell done!!!")
    else:
        print("The insanity rots youe eyes into a pool of muck\nWell done!!!")
else:
    print("You stumble around and fall on a knife and die. Marvelous!!!")
