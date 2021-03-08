import discord
import random

# FILES
# Get words from dictionary txt file
dictionaryFile = open("wordlist.txt", "r")
dictionary = dictionaryFile.read()
wordsList = dictionary.split()  # .split() makes a string into a list of words

# FUNCTIONS

# Returns the string of blanks for the length of the word
# If provided a correct char guess, will update blanks
def blanks(word, letters = []):
    update = ''
    n = len(word)
    if letters == []:
        update = '**-** ' * n  # ** ** bolds message in discord
        return update
    else:
        for i in range(0, n):
            for j in range(0, len(letters)):
                if word[i] == letters[j]:
                    update += '**' + letters[j] + '** '
            if word[i] not in letters:
                update += '**-** '
        return update

# Returns pictures of the Hangman for each 6 wrong guesses
def hangman(count):
    HANGMANPICS = ['''
    +-----+
 |         |
 |
 |
 |
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('that's fine')
 |
 |
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('I am fine...right?')
 |         |
 |
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('...I have some concerns')
 |       /|
 |
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('you should think of your next) 
 |       /|\  (two steps very carefully'  -_-  )
 |
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('I don't feel so good' O_o) 
 |       /|\ 
 |       /
 |
=========''', '''
          +-----+
 |         |
 |        O  ~('...should've gone for the head...')
 |       /|\                *dies*
 |       / \ 
 |
=========''']
    if count < 7:
        return HANGMANPICS[count]

# MAIN #
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # initialize the bot

@client.event
async def on_message(message):
    global word, guesses, wrong, right, game, guess

    if message.author == client.user:  # ignore messages from bot
        return

    if message.content.startswith('$play'):
        # start a new game by generating new random word
        game = True
        index = random.randint(0, len(wordsList))  # location of random word
        word = wordsList[index]  # random word

        guesses = []  # all letters guessed by player
        wrong = []  # all incorrect guesses made by player
        right = []  # correct guesses

        output = blanks(word, guesses)
        await message.channel.send(output)
        await message.channel.send("Send $p *letter* to guess the letter. Use !p to guess the full word. Good luck!")

    if message.content.startswith('!p') and len(message.content) != 4:  # guess the whole word
        guess = ''
        for i in range(3, len(message.content)):  # get the message after the command
            guess = guess + message.content[i]

        if guess.lower() == word:  # wins if the guess is the same as the word
            await message.channel.send("You WIN!")
            await message.channel.send("...this round")
            await message.channel.send(file=discord.File('pigeon.png'))
            await message.channel.send("$play again")
            game = False
            return

        else:
            await message.channel.send("Try sticking with *letter* guesses")

    if message.content.startswith('$p') and len(message.content) == 4:  # letter guess only
        guess = message.content
        guess = guess[3]  # get letter guess from message

        if game == True:  # game on

            if guess.isalpha():
                guess = guess.lower()

                if guess not in guesses:
                    guesses.append(guess)
                    output = blanks(word, guesses)

                    if guess not in word:
                        wrong.append(guess)
                    else:
                        right.append(guess)
                        print(right)

                    await message.channel.send(hangman(len(wrong)))  # print hangman according to incorrect guesses
                    await message.channel.send(output)  # updated blanks with right guesses
                    if len(wrong) > 0:
                        await message.channel.send('Wrong Guesses: ' + str(wrong))  # list of wrong guesses

                    # End game conditions
                    if len(wrong) == 6 and len(right) != len(word):  # didnt guess the word within 6 guesses
                        await message.channel.send("gAmE oVeR :headstone:")
                        await message.channel.send("The word was **" + word + "**")  # send the word bolded
                        await message.channel.send(file=discord.File('evil-removebg-preview.png'))
                        await message.channel.send("$play again")
                        game = False
                        return

                    count = 0
                    for i in word:
                        if i in right:
                            count += 1
                    if count == len(word):  # check if the word was completed
                        await message.channel.send("You WIN!")
                        await message.channel.send("...this round")
                        await message.channel.send(file=discord.File('pigeon.png'))
                        await message.channel.send("$play again")
                        game = False
                        return

                else:
                    await message.channel.send("You already guessed that letter")

            else:  # user can only guess letters
                await message.channel.send('Use letters only')

        else:  # prevent user from continuing old game
            await message.channel.send("Why are you still trying??")
            await message.channel.send("$play again")


dictionaryFile.close()
client.run('TOKEN')

