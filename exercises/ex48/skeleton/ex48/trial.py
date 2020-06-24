# Test First Challenge

nouns = ('door', 'bear', 'princess', 'cabinet')
verbs = ('go', 'stop', 'kill', 'eat')
direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
stops = ('the', 'in', 'of', 'from', 'at', 'it')



# Directions
def way(words, direction, result):
    for word in words:
        if word in direction:
            twos = ('direction', word)
            result.append(twos)
    return result


# Verbs
def verb(words, verbs, result):
    for word in words:
        if word in verbs:
            twos = ('verb', word)
            result.append(twos)
    return result


# Stops
def stop(words, stops, result):
    for word in words:
        if word in stops:
            twos = ('stop', word)
            result.append(twos)
    return result


# Nouns
def noun(words, nouns, result):
    print (words)
    for word in words:
        if word in nouns:
            twos = ('noun', word)
        else:
            twos = ('error', word)
        result.append(twos)
    
    return result


# Numbers
def num(words, result):
    for word in words:
        try:
            v = int(word)
            twos = ('number', v)
        except:
            twos = ('error', word)
        result.append(twos)
    return result
        


# Main
def scan(information):
    result = []
    words = information.split()
    
    # return way(words, direction, result)
    
    # return verb(words, verbs, result)
    
    # return stop(words, stops, result)
    
    # return noun(words, nouns, result)
    
    return num(words, result)
    
    # return a list of tuple pairings
    return result