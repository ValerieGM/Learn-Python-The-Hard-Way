formater = "{} {} {} {}"

print(formater.format(1, 2, 3, 4))
print(formater.format("one", "two", "three", "four"))
print(formater.format(True, False, True, False))
print(formater.format(formater, formater, formater, formater))
print(formater.format(
    "Roses are red",
    "Violets are blue",
    "Sugar is sweet",
    "And so are Marshmallows"
    ))

## take formatter string that is defined
## call it's format function which is similar to telling it to do a command line command named format (command line things)
## pass 4 arguments to formater, seeing as this matches up to the 4 braces in formater
## result of format is that of a new string with it's respective replacements
