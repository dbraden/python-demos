"""Tests for the chesspiece module."""

import unittest
from . import chesspiece


class TestChessPieceModule(unittest.TestCase):
    """Tests for the chesspiece module."""

    def testGetClasses(self):
        """Tests for the getClasses method."""
        self.assertIn('knight', chesspiece.classes)
        self.assertIn('queen', chesspiece.classes)
        self.assertIn('king', chesspiece.classes)
        self.assertIn('rook', chesspiece.classes)
        self.assertIn('castle', chesspiece.classes)

        self.assertTrue(issubclass(chesspiece.getClass('knight'),
                                   chesspiece.Knight))
        self.assertTrue(issubclass(chesspiece.getClass('queen'),
                                   chesspiece.Queen))
        self.assertTrue(issubclass(chesspiece.getClass('king'),
                                   chesspiece.King))
        self.assertTrue(issubclass(chesspiece.getClass('castle'),
                                   chesspiece.Castle))
        self.assertTrue(issubclass(chesspiece.getClass('rook'),
                                   chesspiece.Rook))

    def testRegisterClass(self):
        """Test the registerClass method."""
        class TestClass(object):
            """An example class."""
            pass

        chesspiece.registerClass('TestClass', TestClass)
        self.assertIn('TestClass', chesspiece.classes)

    def testGetClass(self):
        """Test the getClass method."""
        class TestClass(object):
            """An example class."""
            pass

        chesspiece.registerClass('TestClass', TestClass)
        self.assertIn('TestClass', chesspiece.classes)

        cls = chesspiece.getClass('TestClass')
        self.assertTrue(cls)
        self.assertTrue(issubclass(cls, TestClass))


class TestChessPiece(unittest.TestCase):
    """Tests for the chesspiece base class."""

    def testGetRow(self):
        """Test getRow method."""
        self.obj = chesspiece.ChessPiece(4, 3)
        self.assertEqual(self.obj.getRow(), 4)

    def testGetColumn(self):
        """Test getColumn method."""
        self.obj = chesspiece.ChessPiece(4, 3)
        self.assertEqual(self.obj.getColumn(), 3)

    def testIsPiecePosition(self):
        """Test the isPiecePosition method."""
        self.obj = chesspiece.ChessPiece(4, 3)

        self.assertFalse(self.obj.isPiecePosition(3, 4))
        self.assertFalse(self.obj.isPiecePosition(2, 5))
        self.assertTrue(self.obj.isPiecePosition(4, 3))
        self.assertFalse(self.obj.isPiecePosition(5, 3))


class ChessPieceCommon(unittest.TestCase):
    """Common tests for all chess pieces."""

    def setUp(self):
        """Create fixture."""
        super(ChessPieceCommon, self).setUp()
        self.obj = None

    def testIsValidMovePiecePosition(self):
        """Test that isValidMove returns False for the current piece
        position.
        """
        if not self.obj:
            return

        valid = self.obj.isValidMove(self.obj.getRow(),
                                     self.obj.getColumn())
        self.assertFalse(valid)


class TestKnight(ChessPieceCommon):
    """Tests for the Knight class."""

    def setUp(self):
        """Create fixture."""
        super(TestKnight, self).setUp()
        self.obj = chesspiece.Knight(4, 4)

    def testGetBoardCharacter(self):
        """Test the getBoardCharacter method."""
        self.assertEqual('k', self.obj.getBoardCharacter())

    def testIsValidMove(self):
        """Test the isValidMove method."""
        valid = [[6, 3], [6, 5], [5, 2], [5, 6], [3, 2], [3, 6],
                 [2, 3], [2, 5]]

        # Moves in knight format (2 x 1) are valid.
        for x in range(1, 9):
            for y in range(1, 9):
                coord = [x, y]
                if coord in valid:
                    self.assertTrue(self.obj.isValidMove(x, y))
                else:
                    self.assertFalse(self.obj.isValidMove(x, y))


class TestQueen(ChessPieceCommon):
    """Tests for the Queen class."""

    def setUp(self):
        """Create fixture."""
        super(TestQueen, self).setUp()
        self.obj = chesspiece.Queen(5, 3)

    def testGetBoardCharacter(self):
        """Test the getBoardCharacter method."""
        self.assertEqual('Q', self.obj.getBoardCharacter())

    def testIsValidMove(self):
        """Test the isValidMove method."""
        # Same row is valid.
        self.assertTrue(self.obj.isValidMove(5, 1))
        self.assertTrue(self.obj.isValidMove(5, 2))
        self.assertTrue(self.obj.isValidMove(5, 4))
        self.assertTrue(self.obj.isValidMove(5, 5))

        # Same column is valid.
        self.assertTrue(self.obj.isValidMove(3, 3))
        self.assertTrue(self.obj.isValidMove(4, 3))
        self.assertTrue(self.obj.isValidMove(6, 3))
        self.assertTrue(self.obj.isValidMove(7, 3))

        # Diagonals are valid.
        self.assertTrue(self.obj.isValidMove(3, 1))
        self.assertTrue(self.obj.isValidMove(4, 2))
        self.assertTrue(self.obj.isValidMove(4, 4))
        self.assertTrue(self.obj.isValidMove(6, 2))
        self.assertTrue(self.obj.isValidMove(6, 4))
        self.assertTrue(self.obj.isValidMove(7, 5))
        self.assertTrue(self.obj.isValidMove(7, 1))

        # Test some invalids.
        self.assertFalse(self.obj.isValidMove(6, 1))
        self.assertFalse(self.obj.isValidMove(4, 1))
        self.assertFalse(self.obj.isValidMove(4, 5))
        self.assertFalse(self.obj.isValidMove(6, 5))


class TestKing(ChessPieceCommon):
    """Tests for the King class."""

    def setUp(self):
        """Create fixture."""
        super(TestKing, self).setUp()
        self.obj = chesspiece.King(3, 3)

    def testGetBoardCharacter(self):
        """Test the getBoardCharacter method."""
        self.assertEqual('K', self.obj.getBoardCharacter())

    def testIsValidMove(self):
        """Test the isValidMove method."""
        valid = [[2, 4], [3, 4], [4, 4], [2, 3], [4, 3],
                 [2, 2], [3, 2], [4, 2]]

        # Moves within one space are valid.
        for x in range(1, 9):
            for y in range(1, 9):
                coord = [x, y]
                if coord in valid:
                    self.assertTrue(self.obj.isValidMove(x, y))
                else:
                    self.assertFalse(self.obj.isValidMove(x, y))


class TestRook(ChessPieceCommon):
    """Tests for the Rook class."""

    def setUp(self):
        """Create fixture."""
        super(TestRook, self).setUp()
        self.obj = chesspiece.Rook(5, 3)

    def testGetBoardCharacter(self):
        """Test the getBoardCharacter method."""
        self.assertEqual('R', self.obj.getBoardCharacter())

    def testIsValidMove(self):
        """Test the isValidMove method."""
        # Diagonals are valid.
        self.assertTrue(self.obj.isValidMove(3, 1))
        self.assertTrue(self.obj.isValidMove(4, 2))
        self.assertTrue(self.obj.isValidMove(4, 4))
        self.assertTrue(self.obj.isValidMove(6, 2))
        self.assertTrue(self.obj.isValidMove(6, 4))
        self.assertTrue(self.obj.isValidMove(7, 5))
        self.assertTrue(self.obj.isValidMove(7, 1))

        # Non-diagonals are not valid.
        self.assertFalse(self.obj.isValidMove(4, 3))
        self.assertFalse(self.obj.isValidMove(3, 3))
        self.assertFalse(self.obj.isValidMove(6, 3))
        self.assertFalse(self.obj.isValidMove(5, 4))
        self.assertFalse(self.obj.isValidMove(5, 5))
        self.assertFalse(self.obj.isValidMove(5, 2))
        self.assertFalse(self.obj.isValidMove(7, 2))


class TestCastle(ChessPieceCommon):
    """Tests for the Castle class."""

    def setUp(self):
        """Create fixture."""
        super(TestCastle, self).setUp()
        self.obj = chesspiece.Castle(4, 4)

    def testGetBoardCharacter(self):
        """Test the getBoardCharacter method."""
        self.assertEqual('C', self.obj.getBoardCharacter())

    def testIsValidMove(self):
        """Test the isValidMove method."""
        # Same row or same column is valid.
        for x in range(1, 9):
            for y in range(1, 9):
                if x == 4 and y == 4:
                    # This is the piece position.
                    self.assertFalse(self.obj.isValidMove(x, y))
                elif x == 4 or y == 4:
                    self.assertTrue(self.obj.isValidMove(x, y))
                else:
                    self.assertFalse(self.obj.isValidMove(x, y))
