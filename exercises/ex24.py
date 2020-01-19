print("From The Top!!!")
print('You\'d need to know \'bout escapes with \\ that do:')
print("\n newlines and \t tabs.")

poem = """
\tMove him into the sun—
Gently its touch awoke him once,
At home, whispering of fields half-sown.\nAlways it woke him, even in France,
Until this morning and this snow.
If anything might rouse him now
\n\tThe kind old sun will know.
"""

print("********************")
print(poem)
print("********************")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 100
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 1000
beans, jars, crates = secret_formula(start_point)

## Another way to format strings
print("With a starting point of: {}".format(start_point))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
## Easier way to apply a list to a format string
print("We's have {} beans, {} jars and {} crates".format(*formula))
