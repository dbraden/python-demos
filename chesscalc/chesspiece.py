"""Chesspiece module provides functionality for each type of piece.

Pieces subclass the base ChessPiece class and implement
getBoardCharacter and isValidMove in order to calculate the valid
moves.

Classes must be registered via registerClass.
"""

classes = {} #pylint: disable=C0103


def registerClass(name, cls):
    """Register a class for a type of piece."""
    classes[name] = cls


def getClass(name):
    """Return the class for the given name of chess piece."""
    return classes.get(name, None)


class ChessPiece(object):
    """Base class for chess piece."""

    def __init__(self, row, column):
        self.row = row
        self.column = column

    def getRow(self):
        """Return the row."""
        return self.row

    def getColumn(self):
        """Return the column."""
        return self.column

    def isPiecePosition(self, row, column):
        """Return true if this is the piece's positon."""
        return self.getRow() == row and self.getColumn() == column

    def getBoardCharacter(self):
        """Return the character for this piece on the board."""
        pass

    def isValidMove(self, row, column):
        """Whether the given row + column is a valid move for this piece,
        given it's current location.
        """
        pass


class Knight(ChessPiece):
    """Class for the Knight piece."""

    def getBoardCharacter(self):
        """Return the character for this piece."""
        return 'k'

    def isValidMove(self, row, column):
        """Whether this is a valid move."""
        if self.isPiecePosition(row, column):
            return False

        isValid = False
        moves = [[-2, -1], [2, -1], [2, 1], [-2, 1],
                 [-1, -2], [1, -2], [1, 2], [-1, 2]]
        for move in moves:
            rowMove, colMove = move
            if (row + rowMove == self.getRow() and
                    column + colMove == self.getColumn()):
                isValid = True

        return isValid


class King(ChessPiece):
    """Class for the King piece."""

    def getBoardCharacter(self):
        """Return the character for this piece."""
        return 'K'

    def isValidMove(self, row, column):
        """Whether this is a valid move."""
        if self.isPiecePosition(row, column):
            return False

        isValid = False
        if (abs(row - self.getRow()) <= 1 and
                abs(column - self.getColumn()) <= 1):
            isValid = True

        return isValid


class Queen(ChessPiece):
    """Class for the Queen piece."""

    def getBoardCharacter(self):
        """Return the character for this piece."""
        return 'Q'

    def isValidMove(self, row, column):
        """Whether this is a valid move."""
        if self.isPiecePosition(row, column):
            return False

        if row == self.getRow():
            return True
        elif column == self.getColumn():
            return True
        else:
            rowDiff = abs(row - self.getRow())
            colDiff = abs(column - self.getColumn())
            if rowDiff == colDiff:
                return True

        return False


class Rook(ChessPiece):
    """Class for the Rook piece."""

    def getBoardCharacter(self):
        """Return the character for this piece."""
        return 'R'

    def isValidMove(self, row, column):
        """Whether this is a valid move."""
        if self.isPiecePosition(row, column):
            return False

        rowDiff = abs(row - self.getRow())
        colDiff = abs(column - self.getColumn())
        if rowDiff == colDiff:
            return True

        return False


class Castle(ChessPiece):
    """Class for the Castle piece."""

    def getBoardCharacter(self):
        """Return the character for this piece."""
        return 'C'

    def isValidMove(self, row, column):
        """Whether this is a valid move."""
        if self.isPiecePosition(row, column):
            return False

        return row == self.getRow() or column == self.getColumn()


registerClass('knight', Knight)
registerClass('king', King)
registerClass('queen', Queen)
registerClass('rook', Rook)
registerClass('castle', Castle)
