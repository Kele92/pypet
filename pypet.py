import random
import os

pypets = [
    {
        'name': 'Fluffy',
        'age': 5,
        'weight': 9.5,
        'hungry': True,
        'photo': '(=^o.o^=)__',
        'phrases': ['Meow!', 'purrrrrrrrr purrrrrrrr purr', 'BUUURRRP!!']
    },
    {
        'name': 'Queso',
        'age': 3,
        'weight': 2.5,
        'hungry': False,
        'photo': '<:3 )~~~~',
        'phrases': ['squeak squeak', 'eeeek!', 'munch munch munch']
    }
]


def chat_with_pypet(pypet):
    print "Your pypet says:"
    phrase = random.choice(pypet['phrases'])
    os.system("say -v Zarvox '{}'".format(phrase))


def startup_pypet():
    print "#######################################"
    print "Welcome to Pypet!"
    os.system("say -v Zarvox 'Welcome to Pypet'")

    # list current pypets
    for pypet in pypets:
        print pypet['name']

    # get user input of which pypet
    print "Which pypet do you choose: "
    pypet_choice = raw_input('> ')

    for pypet in pypets:
        if pypet['name'] == pypet_choice:
            print "You chose " + pypet['name']
            return pypet

    print "No pypet with that name was found"
    return startup_pypet()


def pypet_stats(pypet):
    print pypet['photo']
    print pypet['name'] + " weighs " + str(pypet['weight']) + " pounds "

    if pypet['weight'] > 5:
        print "That's a BIG pypet!"

    if pypet['hungry']:
        print "Your pypet is hungry!"
    else:
        "Your pypet *BURPS* loudly"


def feed_pypet(pypet):
    print "Onomnomnom, you fed your pypet!"
    pypet['weight'] = pypet['weight'] + 1
    pypet['hungry'] = False

pypet = startup_pypet()

terminate = False

# while terminate is NOT true
while not terminate:
    # prints a line
    print "#######################################"

    # asks user for input
    user_input = raw_input('> ')

    # allows user to quit
    if user_input == "quit":
        terminate = True

    elif user_input == "chat":
        chat_with_pypet(pypet)

    # allows user to feed pypet
    elif user_input == "feed":
        feed_pypet(pypet)

    elif user_input == "stats":
        pypet_stats(pypet)

    else:
        print "Command not recognized, please try again."

print "You have quit Pypet"
os.system("say -v Zarvox 'Good bye'")
