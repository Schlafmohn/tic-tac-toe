from random import choice

class TicTacToe:
    def __init__(self):
        print('Добро пожаловать в игру "Крестики-нолики"!')

        self.__STANDART_SYMBOLS = ('X', 'O', '0')
        self.__STANDART_NUMBERS = (0, 1, 2, 3, 4, 5, 6, 7, 8)

        while not self.chooseSymbolPlayer():
            pass

        self.__standardNumbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.__desk = ['-'] * 9
        self.__step = 0
        self.__lastSymbol = ''

        self.rules()
        self.startGame()

    def chooseSymbolPlayer(self):
        print('Выберите, за кого вы играете')
        inputSymbol = input('Введите X, если за крестика, или O, если за нолик: ').upper()

        if not inputSymbol in self.__STANDART_SYMBOLS:
            return False

        if inputSymbol == 'X':
            self.__symbolPlayer = 'X'
            self.__messageSymbolPlayer = 'крестик'
        else:
            self.__symbolPlayer = 'O'
            self.__messageSymbolPlayer = 'нолик'

        print('Отлично! Вы выбрали {} и будете играть за {}'.format(self.__symbolPlayer, self.__messageSymbolPlayer))
        self.__chooseSymbolBot()
        return True

    def __chooseSymbolBot(self):
        if self.__symbolPlayer == 'X':
            self.__symbolBot = 'O'
            self.__messageSymbolBot = 'нолик'
        else:
            self.__symbolBot = 'X'
            self.__messageSymbolBot = 'крестик'

    def rules(self):
        print('Имеется доска из 9 пронумерованных клеток:')
        print('1 2 3\n4 5 6\n7 8 9')
        print('При вашем ходе вы вводите число нужной клетки, куда и ставится ваш {} {}'.format(self.__messageSymbolPlayer, self.__symbolPlayer))

    def startGame(self):
        if self.__symbolPlayer == 'O':
            self.__gameBot()
            self.printActualDesk()
            self.__step += 1

        while self.__continueGame():
            self.__mainGame()

        self.__finishGame()

    def __mainGame(self):
        while not self.__gamePlayer():
            pass

        self.__step += 1

        if self.__continueGame():
            self.__gameBot()
            self.__step += 1

        self.printActualDesk()

    def __gamePlayer(self):
        inputNumber = int(input('Введите число нужной клетки: ')) - 1

        if not inputNumber in self.__STANDART_NUMBERS:
            self.rules()
            return False

        if self.__desk[inputNumber] != '-':
            print('Клетка под номером {} уже занята {}. Введите другую клетку'.format(inputNumber + 1, self.__desk[inputNumber]))
            return False

        self.__desk[inputNumber] = self.__symbolPlayer
        self.__lastSymbol = self.__symbolPlayer
        return True

    def __gameBot(self):
        isEmptyCell = False

        while not isEmptyCell:
            cellNumber = choice(self.__STANDART_NUMBERS)

            if self.__desk[cellNumber] == '-':
                isEmptyCell = True
                self.__desk[cellNumber] = self.__symbolBot

        self.__lastSymbol = self.__symbolBot

    def printActualDesk(self):
        indexDesk = 0

        for i in self.__desk:
            print(i, end=' ')
            indexDesk += 1

            if indexDesk % 3 == 0:
                print()

    def __continueGame(self):
        if self.__isNoPossibleSteps():
            return False

        indexLine = 0
        indexRow = 0

        while indexRow < 3:
            chekingLine = self.__desk[indexLine] != '-' and (self.__desk[indexLine] == self.__desk[indexLine + 1] and self.__desk[indexLine] == self.__desk[indexLine + 2])
            chekingRow = self.__desk[indexRow] != '-' and (self.__desk[indexRow] == self.__desk[indexRow + 3] and self.__desk[indexRow] == self.__desk[indexRow + 6])

            if chekingLine or chekingRow:
                return False

            indexLine += 3
            indexRow += 1

        if self.__desk[4] == '-':
            return True

        chekingFirstTrait = self.__desk[0] == self.__desk[4] and self.__desk[0] == self.__desk[8]
        chekingSecondTrait = self.__desk[2] == self.__desk[4] and self.__desk[2] == self.__desk[6]

        if chekingFirstTrait or chekingSecondTrait:
            return False

        return True

    def __finishGame(self):
        if self.__isNoPossibleSteps():
            print('Игра окончена! Ничья: никто не выиграл и не проиграл')

        elif self.__lastSymbol == self.__symbolPlayer:
            print('Игра окончена! Выиграл {} {}'.format(self.__messageSymbolPlayer, self.__symbolPlayer))

        else:
            print('Игра окончена! Выиграл {} {}'.format(self.__messageSymbolBot, self.__symbolBot))

        print('Количество ходов: {}'.format(self.__step))

    def __isNoPossibleSteps(self):
        if not '-' in self.__desk:
            return True

        return False

TicTacToe()
