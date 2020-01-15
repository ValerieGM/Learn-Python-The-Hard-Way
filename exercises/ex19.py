def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("More than enough for y'all!!")
    print("Grab a throw!!\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(10, 60)

print("Or variables from the script:")
cheese = 10
crackers = 60
cheese_and_crackers(cheese, crackers)

print("Math can be done within too:")
cheese_and_crackers(10, 50 + 10)

print("Or a combination of variables and math:")
cheese_and_crackers(cheese + 30, crackers - 20)
