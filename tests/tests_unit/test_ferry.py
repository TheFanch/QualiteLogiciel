import unittest

from classes.Company import Company
from classes.Ferry import Ferry

class testFerry(unittest.TestCase):

    def getFerryObject(self):
        ferry = Ferry()

        ferry.setName("Atlantis")
        ferry.setPlaces(75)

        return ferry

    def getCompanyObject(self):
        company = Company()

        #company.setName("NASA")

        return company

    def test_Creation_Whith_Valid_Name_And_Place(self):
        ferry = self.getFerryObject()

        self.assertEqual("Atlantis",ferry.name)
        self.assertEqual(75,ferry.places)
        self.assertEqual(75,ferry.placeAvailable)

    def test_Creation_Invalid_Places(self):
        ferry = self.getFerryObject()

        with self.assertRaises(ValueError):
            ferry.setPlaces(0)

    def test_Creation_Invalid_Name(self):
        ferry = self.getFerryObject()

        with self.assertRaises(ValueError):
            ferry.setName('')

    def test_Put_Valid_Car_Number(self):
        ferry = self.getFerryObject()

        ferry.stockCars(25)

        self.assertEqual(ferry.placeAvailable, (self.getFerryObject().places-25))

    def test_Put_Invalid_Car_Number(self):
        ferry = self.getFerryObject()

        with self.assertRaises(ValueError):
            ferry.stockCars(200)

    def test_Put_Valid_Car_Number_Many_Time(self):
        ferry = self.getFerryObject()

        ferry.stockCars(25)
        ferry.stockCars(25)

        self.assertEqual(ferry.placeAvailable, (self.getFerryObject().places - 50))

    def test_Put_Invalid_Car_Number_Many_Time(self):
        ferry = self.getFerryObject()

        ferry.stockCars(25)
        with self.assertRaises(ValueError):
            ferry.stockCars(70)

    def test_Affect_Ferry_In_Company_OK(self):
        company = self.getCompanyObject()
        ferry = self.getFerryObject()

        company.affect(ferry)

    def test_Adding_Trunck_OK(self):
        ferry = self.getFerryObject()

        ferry.addTrunck(5)

        self.assertEqual(ferry.placeAvailable, (self.getFerryObject().places - 15))

    def test_Adding_Trunck_Manny_Time_OK(self):
        ferry = self.getFerryObject()

        ferry.addTrunck(5)
        ferry.addTrunck(5)

        self.assertEqual(ferry.placeAvailable, (self.getFerryObject().places - 30))

    def test_Put_Invalid_Trunck_Number_Many_Time(self):
        ferry = self.getFerryObject()

        ferry.addTrunck(5)
        with self.assertRaises(ValueError):
            ferry.addTrunck(70)

    def test_Affect_Route_OK(self):
        ferry = self.getFerryObject()

        ferry.affectRoute("Alpha","Epsilon")

        self.assertEqual("Alpha",ferry.route.startPLace)
        self.assertEqual("Epsilon",ferry.route.endPLace)


