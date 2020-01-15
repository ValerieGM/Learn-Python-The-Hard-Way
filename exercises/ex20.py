from sys import argv

script, input_file = argv

def print_all(doc):
    print(doc.read())

def rewind(doc):
    # seek deals in bytes, not lines
    doc.seek(0)

def print_a_line(line_count, doc):
    # readline looks for the \n character
    print(line_count, doc.readline())

current_file = open(input_file)

print("Full document being printed::")
print_all(current_file)

# all the way back to the beginning of the file after reading it
print("Rewind::")
rewind(current_file)

print("Display 3 lines::")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

## seek(1, 2) == 1)from a specified position
##               2)relative to:: 
##                         0 == absolute file positioning:: 
##                         1 == relative to current position::
##                         2 == relative to file's end
