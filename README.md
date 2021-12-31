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

 A dictionary of [10,000 words](https://www.mit.edu/~ecprice/wordlist.10000) was selected for the Hangman game as to have enough randomly-generated, common words where the game is always new and interesting for the user and to minimize heavy data usage. Sending **'$play'** in messages notifies the bot that a new game of Hangman is being requested and will thus randomly select a word and set the game stats to new game defaults. Since updating the blanks for the 'guessing' word is a crucial step repeatedly done throughout the game, the process is all done in the function _blanks(word, letters=[ ])_. _blanks(word, letters=[ ])_ determines the placement of '_' and correctly-guessed letters (if any) and returns the string to be sent by the **'$p'** for the next play. 
 
 
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
  
