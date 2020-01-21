the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

## same variable type list
for number in the_count:
    print(f"This is count {number}")

for fruit in fruits:
    print(f"A fruit type: {fruit}")

## mixed variable type list
for v in change:
    print(f"I got {v}")

## building lists
elements = []

## range(start, end) function to limit the maximum amount (end - 1) --> range doesn't include the last number
for v in range(0, 6):
    print(f"Adding {v} to the list")
    ## append == adding to lists specifically
    elements.append(v)

for v in elements:
    print(f"Elements was: {v}")

## 2D lists == lists within lists
