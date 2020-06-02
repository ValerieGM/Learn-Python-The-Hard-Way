import mystuff

# find the key "apple"
# dict style
mystuff1 = {'apple': "I AM APPLES!"}
print (mystuff1['apple'])
print('-' * 10)

# module style
mystuff.apple()
print('-' * 10)
print(mystuff.tangerine)
print('-' * 10)

# class style
thing  = mystuff.MyStuff()
thing.apple()
print('-' * 10)
print(thing.tangerine)