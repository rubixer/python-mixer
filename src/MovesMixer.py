#! /usr/bin/python3

from random import randint
import numpy
from itertools import cycle
import sys


class MovesMixer:
    """
    Generates random rubik cube moves.
    """


    allPossibleMoves_3x3 = [
        ["U", "U'", "U2"],
        ["D", "D'", "D2"],
        ["F", "F'", "F2"],
        ["B", "B'", "B2"],
        ["R", "R'", "R2"],
        ["L", "L'", "L2"]
    ]


    groupMoves = [
        ["U", "D"],
        ["F", "B"],
        ["R", "L"]
    ]


    def getMixedMoves(self, moves, length):
        """
           :param moves:  A list of list of possible moves
           :param length: How many moves do you want
           :type moves:   list
           :type length:  int
           :returns:      list of mixed moves
           :rtype:        list
        """
        len_list = len(moves)
        temp = list(moves)
        last_move = temp.pop(randint(0, len_list - 1))
        mixed_moves = [last_move[randint(0, len(last_move) - 1)]]

        for _ in range(0, length - 1):
            temp_move = temp.pop(randint(0, len(temp) - 1))
            mixed_moves.append(temp_move[randint(0, len(temp_move) - 1)])
            temp.append(last_move)
            last_move = temp_move

        return mixed_moves


    def getGroupSymmetricalMoves(self, mixedMoves, groups):
        """
            :param mixedMoves: A list with random moves
            :param groups:      A list of list with strings
            :type mixedMoves:  list
            :type groups:       list
            :returns:           list of grouped moves
            :rtype:             list with list
        """
        groupedMoves = []
        length = len(mixedMoves)

        i = 0
        while i < length - 1:
            is_found = False

            for group in groups:
                if (group[0] in mixedMoves[i] and group[1] in mixedMoves[i + 1]) or \
                        (group[1] in mixedMoves[i] and group[0] in mixedMoves[i + 1]):
                    found = True
                    break

            if is_found:
                groupedMoves.append([mixedMoves[i], mixedMoves[i + 1]])
                i += 2
            else:
                groupedMoves.append([mixedMoves[i]])
                i += 1

        return groupedMoves


    def __init__(self, numberOfMoves=50):
        self.numberOfMoves = numberOfMoves
        self.mixedMoves = self.getMixedMoves(self.allPossibleMoves_3x3, self.numberOfMoves)
        self.groupedMoves = self.getGroupSymmetricalMoves(self.mixedMoves, self.groupMoves)


    def show(self, numParts=5):
        '''
        prints the randomized values
        :param numParts number of times to insert a new line in the result list:
        :return:
        '''
        print("")
        print("mixed moves with length [%s]:" % (self.numberOfMoves))
        for part in numpy.split(numpy.array(self.mixedMoves), numParts):
            print("\t%s" % part)

        print("")
        print("grouped moves with length [%s]:" % self.numberOfMoves)
        licycle = cycle(self.groupedMoves)
        part = []
        for i in range(0, len(self.groupedMoves)):
            if i % (self.numberOfMoves / numParts) == 0 and not not part:
                print("\t%s" % part)
                part = []
            part.append(licycle.next())


if __name__ == "__main__":
    mixer = MovesMixer()
    mixer.show()
