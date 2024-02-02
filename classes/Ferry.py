class Ferry:
    # Cette classe doit permetre de:
    # Nommer un Ferry
    # Definir un nombre de place de voiture maximum
    # Stocker des vehicules
    # Donner le nombre de place restante (du Ferry)

    name: str
    places: int
    placeAvailable: int

    def setName(self, entryName):
        if entryName != "" and entryName != " ":
            self.name = entryName
        else:
            raise ValueError('the name is not Valid')

    def setPlaces(self, entryPlace):
        if entryPlace != 0 and entryPlace > 1:
            self.places = entryPlace
            self.placeAvailable = entryPlace
        else:
            raise ValueError('The number of places must be superior to one')

    def stockCars(self, entryVehicules):
        if entryVehicules > self.places:
            raise ValueError('their is not enought place in the ferry for the cars you want to bring in!!')
        elif entryVehicules > self.placeAvailable:
            raise ValueError('their is not enought place available in the ferry for the cars you want to bring in !!')
        elif entryVehicules < 1:
            raise ValueError('The number of cars you want to bring in is not valid!!')
        else:
            self.placeAvailable = self.placeAvailable - entryVehicules

    def getPlacesAvailable(self):
        return self.placeAvailable


