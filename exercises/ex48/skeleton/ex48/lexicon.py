nouns = ('door', 'bear', 'princess', 'cabinet')
verbs = ('go', 'stop', 'kill', 'eat')
direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
stops = ('the', 'in', 'of', 'from', 'at', 'it')

def scan(info):
    result = []
    words = info.split()
    
    for word in words:
        if word in nouns:
            twos = ('noun', word)
        elif word in verbs:
            twos = ('verb', word)
        elif word in direction:
            twos = ('direction', word)
        elif word in stops:
            twos = ('stop', word)
        elif word.isnumeric():
            v = int(word)
            twos = ('number',v)
        else:
            twos = ('error', word)
        result.append(twos)
    
    return result