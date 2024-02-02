from classes.Ferry import Ferry


class Company:

    name: str
    ferrys = []

    def setName(self, entryName):
        if entryName != "" and entryName != " ":
            self.name = entryName
        else:
            raise ValueError('the name is not Valid')

    def affect(self, entryFerry):
        if entryFerry is None:
            raise ValueError('the Ferry is not Valid')
        else:
            self.ferrys.append(entryFerry)
