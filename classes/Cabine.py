class Cabine:
    number: int
    passenger: str

    def setpassenger(self, entrypassenger):
        if entrypassenger != "" and entrypassenger != " ":
            self.passenger = entrypassenger
        else:
            raise ValueError('the passenger is not Valid')

    def setnumber(self, entrynumber):
        if entrynumber != 0 and entrynumber > 1:
            self.number = entrynumber
        else:
            raise ValueError('The number must be superior to one')