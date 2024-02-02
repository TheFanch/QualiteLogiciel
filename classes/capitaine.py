class Capitaine:
    name: str

    def setName(self, entryName):
        if entryName != "" and entryName != " ":
            self.name = entryName
        else:
            raise ValueError('the name is not Valid')
