# Hangman
---
> Description : Hangman is a guessing game for two or more players. One player thinks of a word, phrase, or sentence and the other(s) tries to guess it by suggesting letters or numbers within a certain number of guesses.
>  This Python Program allows player to play this game against another player.
---

## Overview

The word to guess is represented by a row of dashes representing each letter or number of the word. Rules may permit or forbid proper nouns, such as names, places, brands, or slang. If the guessing player suggests a letter which occurs in the word, the other player writes it in all its correct positions. If the suggested letter does not occur in the word, the other player adds (or alternatively, removes) one element of a hanged stick figure as a tally mark. Generally, the game ends once the word is guessed, or if the stick figure is complete — signifying that all guesses have been used.

The player guessing the word may, at any time, attempt to guess the whole word. If the word is correct, the game is over and the guesser wins. Otherwise, the other player may choose to penalize the guesser by adding an element to the diagram. If the guesser makes enough incorrect guesses to allow the other player to complete the diagram, the guesser loses. However, the guesser can also win by guessing all the letters that appear in the word, thereby completing the word, before the diagram is completed.
[Read More on Wikipedia](https://en.wikipedia.org/wiki/Hangman_(game))

## Algorithm

1. The player1 creates the game with folloving command: **object name = Hangman('word, phrase, or sentence')**<br>Example:<br>guess_movie = Hangman('The Lord of the Rings')
2. When the player2 is ready to guess, game can be started with following command: **start_game(object_name)**<br>In our example:<br>start_game(guess_movie)
3. In each turn, player2 will be asked a question: Do you want to guess the word?
   - If player2 asnwers with 'Yes', he gets a chance to guess the word.
     - If he guess correctly, he wins and the game is over.
     - Otherwise, he loses one life and one element of 'hangman' diagram is added.
   - If player2 asnwers with 'No', he gets a chance to guess the letter.
     - If he guess correctly, the letter he choose will be unvailed in all positions of the word presentation.
     - Otherwise, he loses one life and one element of 'hangman' diagram is added.
4. The game is finished either:
   - When 'hangman' is completed (in which case player1 wins)
   - When the word or all the letters are guessed (in which case player2 wins)

## Dependencies

* Python


A Project by (https://github.com/Dzonix)
