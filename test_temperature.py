from unittest import TestCase, main
from temperature import Temperature

class TestTemperature(TestCase):

    def test_celsiustoKelvin1(self):
        output1 = Temperature(celsius = 20).kelvin
        output2 = 20 + 273.15
        self.assertEqual(output1, output2)

    def test_celsiustoKelvin2(self):
        output1 = Temperature(celsius = 32).kelvin
        output2 = 32 + 273.15
        self.assertEqual(output1, output2)

    def test_fahrenheittoKelvin1(self):
        output1 = Temperature(fahrenheit = 32).kelvin
        output2 = 273.15
        self.assertEqual(output1, output2)
    
    def test_fahrenheittoKelvin2(self):
        output1 = Temperature(fahrenheit = 35.33).kelvin
        output2 = 275
        self.assertEqual(output1, output2)

if __name__=="__main__":
    main()