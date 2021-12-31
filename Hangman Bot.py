# get token from environment
import os  
from dotenv import load_dotenv

import discord
import random


''' FILES '''
# Get words from dictionary txt file
dictionaryFile = open("wordlist.txt", "r")  # 10,000 word dictionary credit: https://www.mit.edu/~ecprice/wordlist.10000
dictionary = dictionaryFile.read()
wordsList = dictionary.split()  # .split() makes a string into a list of words


''' FUNCTIONS '''
# Returns the string of blanks for the length of the word
# If provided a correct letter guess, will update blanks
def blanks(word, letters = []):
    update = ''
    if letters == []:
        update = '**_** ' * len(word)  # ** ** bolds message in discord
        return update
    else:
        for character in word:
            for letter in letters:
                if character == letter:
                    update += '**' + letter + '** '
            if character not in letters:
                update += '**_** '
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
 |        O  ~('I'll be fine...right?')
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
 |       /|\  (two steps very carefully' -_- )
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
 |        O  ~('...aw man...')
 |       /|\                *dies*
 |       / \ 
 |
=========''']
    if count < 7:
        return HANGMANPICS[count]


''' MAIN '''
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))  # logging in the bot


''' HANGMAN GAME '''
history = False  # determine if very first game (variable remains true after first $play)
game = False  # initialize game variable

@client.event
async def on_message(message):
    global word, guesses, wrong, right, game, history, guess
    
    if message.author == client.user:  # ignore messages from bot
        return

    if message.content.startswith('$play'):
        history = True 
        # start a new game by generating new random word
        game = True
        index = random.randint(0, len(wordsList))  # location of random word
        word = wordsList[index]  # random word
        guesses = []  # all letters guessed by player
        wrong = []  # all incorrect guesses made by player
        right = []  # correct guesses

        await message.channel.send(hangman(0) + "\n" + blanks(word, guesses))
        await message.channel.send("Send $p *letter* to guess the letter. Use !p to guess the full word. Good luck!")

    if game:
        # guess the whole word
        if message.content.startswith('!p') and len(message.content) > 3:  # 3 = !p''
            guess = ''
            for i in range(3, len(message.content)):  # get the message after the command
                guess = guess + message.content[i]

            if guess.isalpha():

                if guess.lower() == word:  # wins if the guess is the same as the word
                    await message.channel.send("You WIN!")
                    await message.channel.send("...this round")
                    await message.channel.send(file=discord.File('pigeon.png'))
                    await message.channel.send("$play again")
                    game = False
                    return
                else:
                    await message.channel.send("Nope! Try sticking with *letter* guesses")
            else: 
                await message.channel.send("Alphabetic characters only!")
        
        # letter guess only
        if message.content.startswith('$p') and len(message.content) == 4:
            guess = message.content
            guess = guess[3]  # get the letter guess from message

            if guess.isalpha():
                guess = guess.lower()

                if guess not in guesses:
                    guesses.append(guess)
                    output = blanks(word, guesses)

                    if guess not in word:
                        wrong.append(guess)
                    else:
                        right.append(guess)

                    await message.channel.send(hangman(len(wrong)))  # print hangman according to incorrect guesses
                    await message.channel.send(output)  # updated blanks with right guesses
                    if len(wrong) > 0:
                        await message.channel.send('Wrong Guesses: ' + ", ".join(wrong))  # list of wrong guesses

                    # end game conditions
                    if len(wrong) == 6 and len(right) != len(word):  # didnt guess the word within 6 guesses
                        await message.channel.send("gAmE oVeR :headstone:")
                        await message.channel.send("The word was **" + word + "**")  # send the word bolded
                        await message.channel.send(file=discord.File('evil-removebg-preview.png'))
                        await message.channel.send("$play again")
                        game = False
                        return

                    # check if the word was completed
                    count = 0
                    for letter in word:
                        if letter in right:
                            count += 1
                    if count == len(word):  
                        await message.channel.send("You WIN!")
                        await message.channel.send("...this round")
                        await message.channel.send(file=discord.File('pigeon.png'))
                        await message.channel.send("$play again")
                        game = False
                        return

                else:
                    await message.channel.send("You already guessed that letter!")

            else:  # user can only guess letters
                await message.channel.send('Single letters only!')

    # prevent user from continuing old game
    elif not game and (message.content.startswith('!p') or message.content.startswith('$p')):
        if not history:  # a game has not been played before
            await message.channel.send("Send $play to start a new game of Hangman")
        else:
            await message.channel.send("Why are you still trying??")
            await message.channel.send("$play again")


dictionaryFile.close()

''' INITIALIZING BOT'''
# access token from environment
load_dotenv()
TOKEN = os.getenv('TOKEN')
client.run(TOKEN)