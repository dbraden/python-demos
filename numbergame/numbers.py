"""Number high/low guessing game.

Interactive with you (the player), who provides the upper bounds
and then answers the high/low/correct prompts in order for the
computer to determine the number you are thinking of.
"""


class NumberGame(object):
    """Number guessing game."""

    def __init__(self):
        """Init method."""
        self.scores = []
        self.minValue = 1
        self.maxValue = None
        self.startMaxValue = None
        self.guesses = []
        self.inProgress = False

    def setStartMaxValue(self, value):
        """Set the starting max value entered by the player."""
        self.startMaxValue = value

    def getStartMaxValue(self):
        """Return the starting max value."""
        return self.startMaxValue

    def setMinValue(self, value):
        """Set the min value."""
        self.minValue = value

    def setMaxValue(self, value):
        """Set the max value."""
        self.maxValue = value

    def getMinValue(self):
        """Get the current minimum value in the range."""
        return self.minValue

    def getMaxValue(self):
        """Get the current maximum value in the range."""
        return self.maxValue

    def setGameInProgress(self, value):
        """Set the flag that indicates a game is in progress."""
        self.inProgress = value

    def getGameInProgress(self):
        """Whether a game is in progress."""
        return self.inProgress

    def getGuesses(self):
        """Return the list of numbers that have been guessed during this
        game.
        """
        return self.guesses

    def clearGuesses(self):
        """Clear the list of guesses."""
        self.guesses = []

    def addGuess(self, guess):
        """Add a guess to the list of guesses."""
        self.guesses.append(guess)

    def instructions(self):
        """Print the instructions."""
        bars = '*' * 50
        msg = ('\n%s\n' % bars + '\n' +
               'Very fun number guessing game. \n\n' +
               'You will be prompted to enter a number, which will be ' +
               'the upper bound (inclusive). \nThen, pick a number within ' +
               'the range from 1 to this number that the computer will ' +
               'guess.\n\nFor example, if you entered 100, you would pick a ' +
               'number between 1-100 for the computer to guess.\n' +
               '\n%s' % bars + '\n')
        print msg

    def getRawInput(self, msg, allowed):
        """Get the raw input value from the player, only accepting a value from
        the list of allowed values. Will cast the value to .lower()"""
        inputValue = raw_input(msg).lower()
        while inputValue not in allowed:
            print 'Command not recognized.\n'
            inputValue = raw_input(msg).lower()
        return inputValue

    def getIntegerInput(self, msg):
        """Get an integer input value from the player."""
        inputValue = None
        while not inputValue:
            try:
                inputValue = int(input(msg))
            except NameError:
                inputValue = None
                print 'Error: Please enter an integer only. \n'
        return inputValue

    def menu(self):
        """Print the instruction menu."""
        msg = ('Type \'play\' to play. ' +
               'Type \'help\' for the instructions. ' +
               'Type \'exit\' to exit. \n')

        inputValue = self.getRawInput(msg, ('play', 'help', 'exit'))
        if inputValue == 'play':
            self.play()
        elif inputValue == 'help':
            self.instructions()
            self.menu()
        elif inputValue == 'exit':
            return

    def reset(self):
        """Reset the values and guesses."""
        self.setMinValue(1)
        self.setMaxValue(None)
        self.clearGuesses()
        self.setGameInProgress(True)

    def play(self, maxValue=None):
        """Play the game."""
        self.reset()
        if not self.getStartMaxValue():
            msg = 'Please enter a number n: '
            maxValue = self.getIntegerInput(msg)
            self.setStartMaxValue(maxValue)
        self.setMaxValue(self.getStartMaxValue())
        print '\nGuessing a number between %s-%s' % (self.getMinValue(),
                                                     self.getMaxValue())
        print 'Answer each guess with l for low, h for high, c for correct.\n'
        while self.getGameInProgress():
            self.doGuess()

    def getHighGuess(self, midpoint):
        """Get the next guess from the midpoint in increasing value, skipping
        values that have already been used.
        """
        guess = midpoint + 1
        while guess < self.getMaxValue() and guess in self.getGuesses():
            guess += 1
        return guess

    def getLowGuess(self, midpoint):
        """Get the next guess from the midpoint in decreasing value, skipping
        values that have already been used.
        """
        guess = midpoint - 1
        while guess > self.getMinValue() and guess in self.getGuesses():
            guess -= 1
        return guess

    def getNextGuess(self):
        """Return the next guess. If the midpoint between the current min and
        max has not been guessed, use that. Otherwise find the closest unused
        value to the midpoint.
        """
        midpoint = (self.getMinValue() +
                    int((self.getMaxValue() - self.getMinValue()) / 2))
        if midpoint not in self.getGuesses():
            return midpoint

        guessHi = self.getHighGuess(midpoint)
        guessLo = self.getLowGuess(midpoint)
        diffHi = abs(guessHi - midpoint)
        diffLo = abs(guessLo - midpoint)
        if diffHi <= diffLo:
            return guessHi

        return guessLo

    def doGuess(self):
        """Determine the number."""
        number = self.getNextGuess()
        self.addGuess(number)
        if self.getMinValue() == self.getMaxValue():
            # Only one option.
            print 'Your number is %d' % number
            answer = 'c'
        else:
            msg = 'Is the number %d? (l/h/c) '
            answer = self.getRawInput(msg % number, ('l', 'h', 'c'))

        if answer == 'c':
            self.scores.append(len(self.getGuesses()))
            self.printStats()
            self.setGameInProgress(False)
            self.gameOver()
        elif answer == 'h':
            self.setMaxValue(number - 1)
        elif answer == 'l':
            self.setMinValue(number + 1)

        if self.isBoundErrorCondition():
            self.boundError()

    def isBoundErrorCondition(self):
        """Return true if the min value is larger than the max value. This
        should not happen, and indicates the player did not answer accurately.
        """
        return self.getMinValue() > self.getMaxValue()

    def boundError(self):
        """Print a message and exit the game if the bounds enter an error
        condition.
        """
        msg = ('I\'m sorry, I\'m afraid I can\'t do that. ' +
               'The min value is higher than the max value.\n' +
               'I\'ve already guessed: %s' % sorted(self.getGuesses()) + '. ' +
               'Exiting. \n')
        print msg
        self.setGameInProgress(False)
        self.gameOver()

    def gameOver(self):
        """Display end of game dialogue."""
        msg = 'Play again? (y/n) \n'
        inputValue = self.getRawInput(msg, ('y', 'n'))
        if inputValue == 'y':
            self.play()
        else:
            return

    def getAverageScore(self):
        """Return the average number of guesses per game."""
        return float(sum(self.scores)) / len(self.scores)

    def printStats(self):
        """Print the game statistics."""
        if len(self.getGuesses()) > 1:
            msg = 'It took %d guesses. \n'
        else:
            msg = 'It took %d guess. \n'
        print msg % len(self.getGuesses())

        if len(self.scores) > 1:
            msg = 'I\'ve averaged %0.1f guesses per game for %s games'
        else:
            msg = 'I\'ve averaged %0.1f guesses per game for %s game'
        print msg % (self.getAverageScore(), len(self.scores))


if __name__ == '__main__':
    runner = NumberGame() #pylint: disable=C0103
    runner.menu()
