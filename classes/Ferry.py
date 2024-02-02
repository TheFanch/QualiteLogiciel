from classes.Cabine import Cabine
from classes.Route import Route
from classes.capitaine import Capitaine


class Ferry:
    # Cette classe doit permetre de:
    # Nommer un Ferry
    # Definir un nombre de place de voiture maximum
    # Stocker des vehicules
    # Donner le nombre de place restante (du Ferry)

    name: str
    places: int
    placeAvailable: int
    route: Route
    capitaine: Capitaine
    cabineNumber: int
    cabines: []

    hightPlaceNumber: int
    lowPlaceNumber: int

    def setName(self, entryName):
        if entryName != "" and entryName != " ":
            self.name = entryName
        else:
            raise ValueError('the name is not Valid')

    def setPlaces(self, entryPlace, entryHightPlaces, entryLowPlace):
        if entryPlace != 0 and entryPlace > 1:
            if entryHightPlaces > 1 and entryLowPlace > 1 and entryPlace == (entryHightPlaces+entryLowPlace):
                self.places = entryPlace
                self.placeAvailable = entryPlace
            else:
                raise ValueError('The number of Hightplaces and LowPlace invalid')
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
            if self.lowPlaceNumber >= entryVehicules:
                self.lowPlaceNumber = self.lowPlaceNumber - entryVehicules
            else:
                rest = entryVehicules - self.lowPlaceNumber
                self.lowPlaceNumber = 0
                self.hightPlaceNumber = self.hightPlaceNumber - rest

            self.placeAvailable = self.hightPlaceNumber + self.lowPlaceNumber

    def getPlacesAvailable(self):
        return self.placeAvailable

    def addTrunck(self, trunckNumber):
        # a Trunck is equal to 3 places
        if trunckNumber > 0:
            placeTake = trunckNumber * 3

            if placeTake > self.hightPlaceNumber:
                raise ValueError('their is not enought place in the ferry for the Truncks you want to bring in!!')
            elif placeTake > self.hightPlaceNumber:
                raise ValueError(
                    'their is not enought place available in the ferry for the Truncks you want to bring in !!')
            elif placeTake < 1:
                raise ValueError('The number of Trunck you want to bring in is not valid!!')
            else:
                self.hightPlaceNumber = self.hightPlaceNumber - placeTake
                self.placeAvailable = self.hightPlaceNumber + self.lowPlaceNumber

        else:
            raise ValueError('The number of trunck you want to bring in is not valid!!')

    def affectRoute(self,start,end):
        if start != '' and start != ' ' and end != '' and end != ' ':
            self.route.endPLace = end
            self.route.startPLace = start
        else:
            raise ValueError('The Route you want to define is not valid!!')

    def affectCapitaine(self,entryName):
        if entryName != '' and entryName != ' ':
            self.capitaine.setName(entryName)
        else:
            raise ValueError('The capitaine name is not valid!!')

    def setCabine(self, entryCabine):
        if entryCabine > 1:
            self.cabineNumber = entryCabine
        else:
            raise ValueError('The cabines number is not valid!!')

    def affectPassenger(self,passenger, number):
        cabine: Cabine

        cabine.setnumber(number)
        cabine.setpassenger(passenger)

        self.cabines.append(cabine)




