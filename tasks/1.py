class InputOutput:
    def getString(self):
        self.s = input("Write text: ")

    def printString(self):
        print("ur text in uppercase: ",self.s.upper())

io = InputOutput()
io.getString()
io.printString()
