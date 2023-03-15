with open('pi.txt') as fo:
    contents = fo.read()
# print(len(contents))

running = True
while running:
    birthday = input("> What is your birthday? (like this: ddmmyy): \n> ")

    if birthday in contents:
        print("Your birthday appears in the first million digits of pi")
    else:
        print("Your birthday does not appear in the first million digits of pi")

    quit = input(">would you like to quit the program?(y/n) \n> ").lower()
    
    if quit == 'y':
        running = False
    else:
        running = True