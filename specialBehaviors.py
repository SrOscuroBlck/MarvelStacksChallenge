from Stack import Stack, pushStack, unstack, emptyStack, getSize

def sweepStackForPositionWithName (stack, name) :
    auxStack = Stack()
    while not emptyStack(stack) :
        data = unstack(stack)
        pushStack(auxStack, data)
        if data["name"].lower() == name.lower() :
            position = getSize(auxStack)
            break
    
    while not emptyStack(auxStack) :
        data = unstack(auxStack)
        pushStack(stack, data)
        
    return position

def sweepStackForCharacterWithFirstLetter(stack) :
    auxStack = Stack()
    charactersFirstLetter = Stack()
    while not emptyStack(stack) :
        data = unstack(stack)
        pushStack(auxStack, data)
        if data["name"].lower().startswith("c") or data["name"].lower().startswith("d") or data["name"].lower().startswith("g") :
            pushStack(charactersFirstLetter, data)

    while not emptyStack(auxStack) :
        data = unstack(auxStack)
        pushStack(stack, data)
        
    return charactersFirstLetter

def sweepStackForMoviesWithName (stack, name) :
    movies = 0
    auxStack = Stack()
    while not emptyStack(stack) :
        data = unstack(stack)
        if data["name"].lower() == name.lower() :
            movies += data["movies"]
        pushStack(auxStack, data)
    
    while not emptyStack(auxStack) :
        data = unstack(auxStack)
        pushStack(stack, data)
        
    return movies

def sweepGetCharatersWithMoreThanXMovies(stack, nMovies) :
    moreThtanXMovies = Stack()
    auxStack = Stack()
    while not emptyStack(stack) :
        data = unstack(stack)
        if data["movies"] > nMovies :
            pushStack(moreThtanXMovies, data)
        pushStack(auxStack, data)
    
    while not emptyStack(auxStack) :
        data = unstack(auxStack)
        pushStack(stack, data)
        
    return moreThtanXMovies