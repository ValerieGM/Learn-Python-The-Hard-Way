## COMMANDS

# • close – Closes the file. Like File->Save.. in your editor.
# • read – Reads the contents of the file. You can assign the result to a variable.
# • readline – Reads just one line of a text file.
# • truncate – Empties the file. Watch out if you care about the file.
#   -w == write mode
#   -r == read mode
#   -rwa == read, write and append mode
#   -a == append
# • write('stuff') – Writes ”stuff” to the file.
# • seek(0) – Move the read/write location to the beginning of the file.
# open default is is read mode

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit Ctrl-C")
print("If you do want that, hit RETURN")

input("?")

print("Openingthe file...")
target = open(filename, "w")

print("truncating the file. Ciao!!")
target.truncate()

print("Now I'm going to ask for three line")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm goin to write these to the file")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("And finally, we close it")
target.close()

