from Stack import Stack, pushStack, unstack, emptyStack, getSize
from Data import marvel_characters
from specialBehaviors import sweepStackForPositionWithName, sweepGetCharatersWithMoreThanXMovies, sweepStackForMoviesWithName, sweepStackForCharacterWithFirstLetter
import os



print("=================================================")
print("> [1] - Position of Rocket Racoon and Groot.\n> [2] - Characters wih more than 5 movies.\n> [3] - Quantity of movies where Black Widow appears.\n> [4] - Characters that start with C, D and G.\n> [0] - Exit")
print("=================================================\n")

charactersStack = Stack()
for character in marvel_characters:
    pushStack(charactersStack, character)

auxOp = "not empty"
op = int(input("Select an option "))
while op != 8:
    if op == 1:
        os.system('clear')
        while auxOp != "":
            print("[1] - Position of Rocket Racoon and Groot:\n")
            print(f"Rocket Racoon is in position {sweepStackForPositionWithName(charactersStack, 'Rocket Racoon')}")
            print(f"Groot is in position {sweepStackForPositionWithName(charactersStack, 'Groot')}")
            auxOp = input("\nPress enter to go back to menu")
        os.system('clear')
        auxOp = "not empty"
        
    elif op == 2:
        os.system('clear')
        while auxOp != "":
            print("[2] - Characters wih more than 5 movies:\n")
            moreThanXMovies = sweepGetCharatersWithMoreThanXMovies(charactersStack, 5)
            print(f"Here are the {getSize(moreThanXMovies)} characters with more than 5 movies:")
            while not emptyStack(moreThanXMovies) :
                character = unstack(moreThanXMovies)
                print(f"Name: {character['name']}, Movies: {character['movies']}")
            auxOp = input("\nPress enter to go back to menu")
        os.system('clear')
        auxOp = "not empty"
          
    elif op == 3:
        os.system('clear')
        while auxOp != "":
            print("[3] - Quantity of movies where Black Widow appears: \n")
            print(f"Black Widow has been in {sweepStackForMoviesWithName(charactersStack, 'Black Widow')} Marvel movies")
            auxOp = input("\nPress enter to go back to menu")
        os.system('clear')
        auxOp = "not empty"
        
    elif op == 4:
        os.system('clear')
        while auxOp != "":
            print("Characters with first letter C, D or G: \n")
            charactersFirstLetter = sweepStackForCharacterWithFirstLetter(charactersStack)
            print(f"Here are the {getSize(charactersFirstLetter)} characters with first letter C, D or G:")
            while not emptyStack(charactersFirstLetter) :
                character = unstack(charactersFirstLetter)
                print(f"- {character['name']}")
            auxOp = input("\nPress enter to go back to menu")
        os.system('clear')
        auxOp = "not empty"
    elif op == 0:
        break
        
    else:
        os.system('clear')
        print("Wrong option")
    
    print("=================================================")
    print("> [1] - Position of Rocket Racoon and Groot.\n> [2] - Characters wih more than 5 movies.\n> [3] - Quantity of movies where Black Widow appears.\n> [4] - Characters that start with C, D and G\n> [0] - Exit")
    print("=================================================\n")
    op = int(input("Select an option "))




    