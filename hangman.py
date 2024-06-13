class Hangman:
    miss = 0
    text = ''

    def __init__(self, word):
        self.word = word.lower()
        self.letters = []
        for i in self.word:
            if i == ' ':
                self.text += ' '
            else:
                self.text += '_'
        print(r'''
Let's play Hangman!
Guess the word represented by a series of dashes.
Good luck!

Lives remaining: ******

  +---+
  |   |
      |
      |
      |
      |
========     ''' + self.text + '\n')

    def __str__(self):
        image = ''
        used_letters = ''
        if self.miss == 0:
            image = r'''
  +---+
  |   |
      |
      |
      |
      |
======== '''
        elif self.miss == 1:
            image = r'''
  +---+
  |   |
  O   |
      |
      |
      |
======== '''
        elif self.miss == 2:
            image = r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
======== '''
        elif self.miss == 3:
            image = r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
======== '''
        elif self.miss == 4:
            image = r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
======== '''
        elif self.miss == 5:
            image = r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
======== '''
        elif self.miss == 6:
            image = r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
======== '''
        for i in self.letters:
            used_letters += i
        return image + '    ' + self.text + '\n\nUsed letters: ' + ', '.join(used_letters) + '\n'


def start_game(game_name):
    while game_name.miss < 6:
        guess_word_q = input('Do you want to guess the word (Y/N)? ').lower()
        if guess_word_q in ('y', 'yes'):
            guess_word = input('Enter word: ').lower()
            if guess_word == game_name.word:
                print('*' * (25 + len(game_name.word)))
                print(f"CONGRATULATIONS! YOU WON!\n<{game_name.word}> is the correct answer!")
                print('*' * (25 + len(game_name.word)))
                quit()
            else:
                game_name.miss += 1
                print('\nLives remaining:', '*' * (6 - game_name.miss))
            print(game_name)
        elif guess_word_q in ('n', 'no'):
            guess = input('Enter letter: ').lower()
            if len(guess) > 1:
                print("Please enter only one letter.")
                continue
            if guess in game_name.letters:
                print('Letter already used.')
                continue
            game_name.letters.append(guess)
            for i in range(len(game_name.word)):
                if game_name.word[i] in guess:
                    game_name.text = game_name.text[:i] + game_name.word[i] + game_name.text[i+1:]
                if game_name.text == game_name.word:
                    print('*' * (25 + len(game_name.word)))
                    print(f"CONGRATULATIONS! YOU WON!\n<{game_name.word}> is the correct answer!")
                    print('*' * (25 + len(game_name.word)))
                    quit()
            if guess not in game_name.word:
                game_name.miss += 1
                print('\nLives remaining:', '*' * (6 - game_name.miss))
            print(game_name)
        else:
            print('Invalid command. Please enter Y (Yes) or N (No)')
            continue
    if game_name.miss >= 6:
        print('*' * (10 + len(game_name.word)))
        print(f'GAME OVER!\nSolution: {game_name.word}')
        print('*' * (10 + len(game_name.word)))
    quit()
