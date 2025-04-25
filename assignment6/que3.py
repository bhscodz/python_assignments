class Converter:
    def __init__(self,value,unit):
        conversion_factors_to_feet = {
        "inch": 1/12,         # 1 inch to feet
        "yard": 3,           # 1 yard to feet
        "mile": 5280,        # 1 mile to feet
        "millimeter": 0.00328084,  # 1 mm to feet
        "centimeter": 0.0328084,   # 1 cm to feet
        "kilometer": 3280.84,    # 1 km to feet
        "meter": 3.28084      # 1 meter to feet
    }
        self._feet= value * conversion_factors_to_feet[unit]
    # feet is my base unit
    def inch(self):
        return self._feet*12
    def yard(self):
        return self._feet/3
    def miles(self):
        return self._feet/5280
    def milli(self):
        return self._feet*04.8
    def centi(self):
        return self._feet*30.48
    def meter(self):
        return self.centi(self._feet)/100
    def kilo(self):
        return self.meter(self._feet)/1000
    def feet(self):
        return self._feet
c=Converter(9,'inch')
print(c.feet())