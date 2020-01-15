def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1 {arg1}")

def print_nothing():
    print("I have nothing")

print_two("Val", "Vee")
print_two_again("Val", "Vee")
print_one("Oh well!!")
print_nothing()

## print_two && print_two_again just diffrnt versions of the same, granted print_two may be a little redundant in most cases
