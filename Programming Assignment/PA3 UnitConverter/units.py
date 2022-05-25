from dataclasses import dataclass
from unittype import UnitType


@dataclass(frozen=True)
class Unit:
    """The attributes of a Unit object."""
    name: str
    unittype: UnitType
    value: float
    # offset parameter with a default value,
    # for units that require an offset from some base value.
    offset: float = 0.0

    """dataclass provides a constructor, 
       getter properties for attributes,
       __eq__ method, and others.
    """

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        """Less than comparison, used for sorting units."""
        return self.name < other.name

    def __repr__(self) -> str:
        classname = type(self).__name__
        # the unit value and optional offset
        if self.offset == 0:
            values = f"{self.value}"
        else:
            values = f"{self.value}, {self.offset}"
        return f"{classname}('{self.name}', UnitType.{self.unittype.name}, {values})"


# For lack of a better place, define a list of known units.
units = [
    # Length units
    Unit("Meter", UnitType.LENGTH, 1.0),
    Unit("Kilometer", UnitType.LENGTH,  1000.0),
    Unit("Centimeter", UnitType.LENGTH,  1.0E-2),
    Unit("Nanometer", UnitType.LENGTH, 1.0E-9,),
    Unit("Mile", UnitType.LENGTH,  1609.344),
    Unit("Foot", UnitType.LENGTH, 0.3048),
    Unit("Inch", UnitType.LENGTH, 0.0254),
    Unit("Yard", UnitType.LENGTH,  0.9144),
    Unit("Wa", UnitType.LENGTH, 2.0),
    Unit("Light-year", UnitType.LENGTH, 9460730472580800.0),

    # Area Units
    Unit("Sq.Meter", UnitType.AREA, 1.0),
    Unit("Sq.Foot", UnitType.AREA, 0.3048*0.3048),
    Unit("Sq.Wa", UnitType.AREA, 4.0),
    Unit("Rai", UnitType.AREA, 1600.0),
    Unit("Sq.inch", UnitType.AREA, 0.00064516),
    Unit("Sq.yard", UnitType.AREA, 0.836127),
    Unit("sq.mile", UnitType.AREA, 2589988.110336),
    Unit("sq.kilometer", UnitType.AREA, 1000000.0),
    Unit("Acre", UnitType.AREA, 4046.8564224),
    Unit("Hectare", UnitType.AREA, 10000.0),
    Unit("Sq.millimeter", UnitType.AREA, 1.0E-6),
    Unit("Sq.centimeter", UnitType.AREA, 1.0E-4),
    Unit("Sq.nanometer", UnitType.AREA, 1.0E-9),

    # Volume Units
    Unit("Liter", UnitType.VOLUME, 1.0),
    Unit("Gallon", UnitType.VOLUME, 3.78541178),
    Unit("Quart", UnitType.VOLUME, 0.946352946),
    Unit("Pint", UnitType.VOLUME, 0.473176473),
    Unit("Cup", UnitType.VOLUME, 0.236588237),
    Unit("Tablespoon", UnitType.VOLUME, 0.0147867648),
    Unit("Teaspoon", UnitType.VOLUME, 0.00492892159),
    Unit("Cubic Meter", UnitType.VOLUME, 1000.0),
    Unit("Cubic Foot", UnitType.VOLUME, 0.0283168466),
    Unit("Cubic Inch", UnitType.VOLUME, 0.000016387064),
    Unit("Cubic Yard", UnitType.VOLUME, 0.764554858),
    Unit("Cubic Mile", UnitType.VOLUME, 4168181825.44058),
    Unit("Cubic Kilometer", UnitType.VOLUME, 1000000000.0),
    Unit("Cubic Centimeter", UnitType.VOLUME, 1.0E-9),
    Unit("Cubic Millimeter", UnitType.VOLUME, 1.0E-12),

    # Example of a unit with an offset value (4th parameter, default is 0)
    Unit("Celsius", UnitType.TEMPERATURE, 1/5, 0),
    Unit("Fahrenheit", UnitType.TEMPERATURE, 1/9, -32),
    Unit("Kelvin", UnitType.TEMPERATURE, 1/5, -273),
    Unit("Reaumur", UnitType.TEMPERATURE, 1/4, 0)
]

if __name__ == '__main__':
    """Demo: print some units."""
    unit_type = UnitType.LENGTH
    print(unit_type, "units")
    for unit in filter(lambda u: u.unittype == unit_type, units):
        print(repr(unit))
