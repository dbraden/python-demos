"""Chess Calculator.

This module calculates the valid chess moves for the give piece at the
given position, with the assumption that there are no other pieces on
the board.

Usage:

python -m chesscalc.chess --piece [piece] --position [pos] [--visual [bool]]

Arguments:
    - piece is one of ['castle', 'king', 'knight', 'queen', 'rook']
    - position is a board position in the standard form form of [a-h][1-8]
    - visual (optional) - displays the board and valid moves in addition to
            returning the moves as output.
"""

import argparse
from . import chesspiece


class ChessCalculator(object):
    """Chess move calculator."""

    def __init__(self, pieceName, position, visual=False):
        """Init method."""
        column = self.getColumnIndex(position[0])
        if not column:
            msg = ('\nError: Invalid column specified. Position should be ' +
                   'in the form: [a-h][1-8].\nex: \'d3\'\n')
            print msg
            return

        try:
            row = int(position[1])
        except ValueError:
            msg = ('\nError: Invalid row specified. Position should be ' +
                   'in the form: [a-h][1-8].\nex: \'d3\'\n')
            print msg
            return

        cls = chesspiece.getClass(pieceName.lower())
        if not cls:
            msg = ('\nError: Class for piece type \'%s\' not found.\n' % (
                pieceName.lower(),))
            print msg
            return

        self.piece = cls(row, column)
        self.visual = bool(visual)
        self.run()

    def colorString(self, string, color):
        """Print a string in the given color. Uses control characters to
        provide coloring. This may not work in all terminals, it is only
        provided as a courtesy.
        """
        colors = {'purple': '\033[95m',
                  'blue': '\033[94m'}

        endColor = '\033[0m'
        if color not in colors:
            return string

        return colors.get(color) + string + endColor

    def getBoardRows(self):
        """Return a sequence of the board rows, represented as an integer.
        Indexes are returned in reverse order to conform with standard
        chess notation.
        """
        return range(1, 9)[::-1]

    def getBoardColumns(self):
        """Return a sequence of the board columns expressed as integers."""
        return range(1, 9)

    def run(self):
        """Determine the valid moves."""
        if self.visual:
            print ''

        moves = []
        pieceChar = self.piece.getBoardCharacter()
        for row in self.getBoardRows():
            rowStr = '%s ' % row
            for column in self.getBoardColumns():
                if self.piece.isPiecePosition(row, column):
                    rowStr += self.colorString('[%s]' % pieceChar, 'purple')
                elif self.piece.isValidMove(row, column):
                    rowStr += self.colorString('[+]', 'blue')
                    moves.append('%s%s' % (self.getColumnLetter(column), row))
                else:
                    rowStr += '[ ]'

            if self.visual:
                print rowStr

        if self.visual:
            colStr = '  '
            for column in self.getBoardColumns():
                colStr += ' %s ' % self.getColumnLetter(column)

            print colStr
            print ''

        print ', '.join(sorted(moves))

    def getColumnIndex(self, letter):
        """Return the column index for the given alpha representation."""
        cols = 'abcdefgh'
        if not letter:
            return None

        letter = str(letter)
        if letter not in cols:
            return None

        return cols.find(letter) + 1

    def getColumnLetter(self, index):
        """Return the column letter for the given index."""
        cols = 'abcdefgh'
        if not index:
            return None

        try:
            index = int(index)
        except ValueError:
            return None

        if index > 8 or index < 1:
            return None

        return cols[index - 1]


def usage():
    """Print usage information."""
    clsNames = sorted(chesspiece.classes.keys())
    print ''
    print '''Usage:
\tpython -m chesscalc.chess --piece [piece] --position [pos] [--visual [bool]]
\t\t- piece is one of %s
\t\t- position is a board position in the form of [a-h][1-8]
\t\t- visual (optional) - displays the board and valid moves
''' % clsNames
    print ''


if __name__ == '__main__':
    parser = argparse.ArgumentParser() # pylint: disable=C0103
    parser.add_argument('--piece')
    parser.add_argument('--position')
    parser.add_argument('--visual', type=int)

    args = parser.parse_args() # pylint: disable=C0103
    if not (args.piece and args.position):
        usage()
    else:
        obj = ChessCalculator(args.piece, args.position, args.visual)  # pylint: disable=C0103
