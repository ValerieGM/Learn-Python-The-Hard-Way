from sys import sys

def dead(why):
    print(why, "Marvelous!")
    exit(0)

def gold_room():
    print("This room is full of gold. How mucn do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print("Nice, you're practical! Ciao!!")
        exit(0)
    else:
        dead("Greedy bastard!!!")

def bear_room():
    print("There's a bear here")
    print("The bear has honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?!")

    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you and slaps you, hard")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door\nYou may enter!")
            bear == True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Make some sense please!!!")


