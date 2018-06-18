"""Tests for the numbers module."""

import unittest
from . import numbers


class TestNumberGame(unittest.TestCase):
    """Tests for the NumberGame class. Tested with nosetests."""

    def setUp(self):
        """Create fixture."""
        self.obj = numbers.NumberGame()

    def testGetMinValueInit(self):
        """Tests for the getMinValue method is set to 1 initially."""
        self.assertEqual(self.obj.getMinValue(), 1)

    def testGetMinValue(self):
        """Test that getMinValue returns the minValue value on the object."""
        self.obj.setMinValue(10)
        self.assertEqual(self.obj.getMinValue(), 10)

    def testGetMaxValueInit(self):
        """Tests for the getMaxValue method is set to None initially."""
        self.assertEqual(self.obj.getMaxValue(), None)

    def testGetStartMaxValue(self):
        """Test the getStartMaxValue method."""
        self.obj.setStartMaxValue(10)
        self.assertEqual(self.obj.getStartMaxValue(), 10)

    def testGetMaxValue(self):
        """Test that getMaxValue returns the minValue value on the object."""
        self.obj.setMaxValue(10)
        self.assertEqual(self.obj.getMaxValue(), 10)

    def testGetGameInProgressInit(self):
        """Test that the game in progress flag is set to False initially."""
        self.assertFalse(self.obj.getGameInProgress())

    def testGetGameInProgress(self):
        """Test the getGameInProgress method."""
        self.obj.setGameInProgress(True)
        self.assertTrue(self.obj.getGameInProgress())

        self.obj.setGameInProgress(False)
        self.assertFalse(self.obj.getGameInProgress())

    def testClearGuesses(self):
        """Test the clearGuesses method."""
        self.obj.clearGuesses()
        self.assertEqual(self.obj.getGuesses(), [])

    def testAddGuess(self):
        """Test the addGuess method."""
        self.obj.clearGuesses()
        self.obj.addGuess(5)
        self.obj.addGuess(7)
        self.assertEqual(set(self.obj.getGuesses()), set([5, 7]))

    def testReset(self):
        """Test the reset method."""
        self.obj.reset()
        self.assertTrue(self.obj.getGameInProgress())
        self.assertEqual(self.obj.getMinValue(), 1)
        self.assertEqual(self.obj.getMaxValue(), None)
        self.assertEqual(self.obj.getGuesses(), [])

    def testGetNextGuess(self):
        """Test the getNextGuess method."""
        self.obj.reset()
        self.obj.setMaxValue(10)

        self.assertEqual(self.obj.getMinValue(), 1)
        self.assertEqual(self.obj.getMaxValue(), 10)
        self.assertEqual(self.obj.getGuesses(), [])

        guess = self.obj.getNextGuess()
        self.assertEqual(guess, 5)

    def testGetNextGuessMidpointGuessed(self):
        """Test the getNextGuess method when the midpoint value is already
        in the list of guesses.
        """
        self.obj.reset()
        self.obj.setMaxValue(10)
        self.obj.addGuess(5)

        self.assertEqual(self.obj.getMinValue(), 1)
        self.assertEqual(self.obj.getMaxValue(), 10)
        self.assertEqual(self.obj.getGuesses(), [5])

        self.assertEqual(self.obj.getHighGuess(5), 6)
        self.assertEqual(self.obj.getLowGuess(5), 4)
        self.assertEqual(self.obj.getNextGuess(), 6)

    def testGetNextGuessMidpointGuessedHigh(self):
        """Test the getNextGuess method when the midpoint value is already
        in the list of guesses, as well as some of the next higher values.
        The lower value should be returned.
        """
        self.obj.reset()
        self.obj.setMaxValue(10)
        self.obj.addGuess(5)
        self.obj.addGuess(6)

        self.assertEqual(self.obj.getMinValue(), 1)
        self.assertEqual(self.obj.getMaxValue(), 10)
        self.assertEqual(set(self.obj.getGuesses()), set([5, 6]))

        self.assertEqual(self.obj.getHighGuess(5), 7)
        self.assertEqual(self.obj.getLowGuess(5), 4)
        self.assertEqual(self.obj.getNextGuess(), 4)

    def testGetNextGuessMidpointGuessedLow(self):
        """Test the getNextGuess method when the midpoint value is already
        in the list of guesses, as well as some of the next lower values.
        The higher value should be returned.
        """
        self.obj.reset()
        self.obj.setMaxValue(10)
        self.obj.addGuess(3)
        self.obj.addGuess(4)
        self.obj.addGuess(5)
        self.obj.addGuess(6)

        self.assertEqual(self.obj.getMinValue(), 1)
        self.assertEqual(self.obj.getMaxValue(), 10)
        self.assertEqual(set(self.obj.getGuesses()), set([3, 4, 5, 6]))

        self.assertEqual(self.obj.getHighGuess(5), 7)
        self.assertEqual(self.obj.getLowGuess(5), 2)
        self.assertEqual(self.obj.getNextGuess(), 7)

    def testIsBoundErrorCondition(self):
        """Test whether the current min / max values are in an error state."""
        self.obj.setMinValue(10)
        self.obj.setMaxValue(100)
        self.assertFalse(self.obj.isBoundErrorCondition())

        self.obj.setMinValue(10)
        self.obj.setMaxValue(5)
        self.assertTrue(self.obj.isBoundErrorCondition())

    def testGetAverageScore(self):
        """Test the getAverageScore method."""
        self.obj.scores = [2, 5]

        self.assertEqual(self.obj.getAverageScore(), 3.5)
