# The Pigeon: A Discord Bot
### Video Demo:  <URL HERE>
### Description:

A website and Discord bot that let's users add 'The Pigeon' bot to Discord servers and play Hangman solo or with friends!

***How to Play:***
To start a new game, send **$play** in messages. A random word from a dictionary of [10,000 words](https://www.mit.edu/~ecprice/wordlist.10000) will be chosen and sent as blanks by the bot, as well as instructions on how to play. To guess a single letter, use the **$p** command. To guess the full word, use the **!p** command. After 6 wrong guesses, you lose the game. Good luck!

### Features:
***Discord Bot:***
Python was used to program a Discord bot that adds a gaming feature to a Discord server. Users can play together or continue messaging in the server without impacting the game.
 - Python (Hangman_Bot.py)
    - Frameworks and libraries: Discord, OS, dotenv, random
 
 Note: .env file with [Discord Bot Token](https://discord.com/developers/applications/) required for functioning bot.

***How it Works:*** 
 
A dictionary of [10,000 words](https://www.mit.edu/~ecprice/wordlist.10000) was selected for the Hangman game as to have enough randomly generated, common words where the game is always new and interesting for the user and to minimize heavy data usage. Sending **'$play'** in messages notifies the bot that a new game of Hangman is being requested and will thus randomly select a word and (re)set the game stats to new game defaults. Since updating the blanks for the 'guessing' word is a crucial step repeatedly done throughout the game, the process is all done in the function _blanks(word, letters=[ ])_. _blanks(word, letters=[ ])_ determines the placement of '_' and correctly guessed letters (if any) and returns the string to be sent by the **'$p'** for the next play. 
 
The _history_ and _game_ variables are in place to determine which messages to send at the start and/or end of a game. If the game is being played for the first time and a message is sent using the _'$p'_, and _'!p'_ commands without intiating a game with _'$play'_, the bot will send a message instructing the user to start a game. After a game has ended, using the _'$p'_, and _'!p'_ commands again before starting a new game will cause the bot to send a different message with a 'friendly competition' undertone, as described in stylistic choices.
 
While a game is active, messages that start with the _'$p'_, and _'!p'_ commands are checked for their respective guesses. The _'$p'_ command lets users guess one letter at a time. Conditional statements check the guessed letter against previous guesses, as well as the letters in the 'guessing' word to determine whether the letter is correct or incorrect. Correct letters are sent to _blanks(word, letters=[ ])_, and incorrect letters are tallied to remember all incorrect guesses and determine which _HANGMANPICS_ to send. By the end of one turn, the updated Hangman visual, blanks, and wrong guesses (if any) are sent to the user. The _'!p'_ command lets users guess full words without penalty. This allows users to ease the level of difficulty guessing the word and provide more chances to guess it correctly. Both commands are able to handle non-string submissions, capitalization, and incorrect command arguments, but only the _'$p'_ command handles the counting of incorrect guesses. 
 
Once the game ends, a message is sent by the bot to announce the win or loss, and encourages the user to _'$play'_ again. If the game is lost, the word is revealed to the player.
 
***Stylistic Choices:***

The _'$play'_, _'$p'_, and _'!p'_ were chosen for the game commands to prevent calling the bot between guild members' conversations and were decided to be obscure enough that they would not show up in normal conversation while also maintaining the 'p for play' theme. Players are reminded of the usage of these commands at the beginning of every game, as well as in the bot description. The choice to separate _'$p'_, and _'!p'_ into two distinct commands was mostly a stylistic choice for the _'!p'_ command to evoke a 'eureka' moment. 

<img align="right" src="https://user-images.githubusercontent.com/64821190/147798026-41534726-7bae-4711-8eb7-1890d8ebfc74.PNG">

The correct and incorrectly guessed letters are presented to the user lowercased to improve the readability and comprehension. People are generally more accustomed to lowercase words because most dictionaries and other texts are written and read in lowercase. Hangman is all about guessing the missing letters from a word so the user should have the competitive advantage of familiarity provided by lowercase. Incorrect letters are presented to the player in a comma-separated list and was done so using the _", ".join(wrong)_. This improved the readability of the incorrect letters compared to simply sending a boxed list of wrong letters.
 
The dialogue and visuals from the _HANGMANPICS_ and 'The Pigeon' add a fun component to the game and hint to competitive behaviour to keep the user engaged and playing. 
Similarily, a website was designed to attract users to play.
 
***Website:***
 HTML and CSS were used to create a static webpage that directs users to inviting 'The Pigeon' Discord bot to their servers.
  - HTML (website.html)
    - ‘meta’ tag fits the width of the webpage to any window
    - Favicon website icon adds aesthetic appeal
    - Concise listed description of bot functions + gameplay capture
  - CSS (style.css)
    - Colors and fonts visually reminiscent of Mo Willems' illustrations
    - Round button showcases link to add bot to Discord server
    - Uses a combination of class and element selectors
  
  ![webpage](https://user-images.githubusercontent.com/64821190/147793644-3bcfeef3-daac-4b36-9fa3-eb75ff4d0316.PNG)
  
