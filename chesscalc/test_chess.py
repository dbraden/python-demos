"""Tests for the chess module."""

import unittest
from . import chess


class TestChess(unittest.TestCase):
    """Tests for the chess module."""

    def setUp(self):
        """Create fixture."""
        super(TestChess, self).setUp()

        self.obj = chess.ChessCalculator('knight', 'b3')

    def testGetColumnIndex(self):
        """Test the getColumnIndex method."""
        self.assertEqual(self.obj.getColumnIndex('a'), 1)
        self.assertEqual(self.obj.getColumnIndex('b'), 2)
        self.assertEqual(self.obj.getColumnIndex('c'), 3)
        self.assertEqual(self.obj.getColumnIndex('d'), 4)
        self.assertEqual(self.obj.getColumnIndex('e'), 5)
        self.assertEqual(self.obj.getColumnIndex('f'), 6)
        self.assertEqual(self.obj.getColumnIndex('g'), 7)
        self.assertEqual(self.obj.getColumnIndex('h'), 8)

    def testGetColumnIndexNegative(self):
        """Negative test cases for getColumnIndex."""
        self.assertFalse(self.obj.getColumnIndex('i'))
        self.assertFalse(self.obj.getColumnIndex('z'))
        self.assertFalse(self.obj.getColumnIndex(5))
        self.assertFalse(self.obj.getColumnIndex(None))

    def testGetColumnLetter(self):
        """Test the getColumnLetter method."""
        self.assertEqual(self.obj.getColumnLetter(1), 'a')
        self.assertEqual(self.obj.getColumnLetter(2), 'b')
        self.assertEqual(self.obj.getColumnLetter(3), 'c')
        self.assertEqual(self.obj.getColumnLetter(4), 'd')
        self.assertEqual(self.obj.getColumnLetter(5), 'e')
        self.assertEqual(self.obj.getColumnLetter(6), 'f')
        self.assertEqual(self.obj.getColumnLetter(7), 'g')
        self.assertEqual(self.obj.getColumnLetter(8), 'h')

    def testGetColumnLetterNegative(self):
        """Negative test cases for the getColumnLetter method."""
        self.assertFalse(self.obj.getColumnLetter(0))
        self.assertFalse(self.obj.getColumnLetter(9))
        self.assertFalse(self.obj.getColumnLetter(-1))
        self.assertFalse(self.obj.getColumnLetter(None))

    def testGetBoardColumns(self):
        """Test the getColumns method."""
        cols = self.obj.getBoardColumns()
        self.assertEqual(set(cols), set([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(cols[0], 1)
        self.assertEqual(cols[-1], 8)

    def testGetRows(self):
        """Test the getRows method."""
        rows = self.obj.getBoardRows()
        self.assertEqual(set(rows), set([1, 2, 3, 4, 5, 6, 7, 8]))
        self.assertEqual(rows[0], 8)
        self.assertEqual(rows[-1], 1)
