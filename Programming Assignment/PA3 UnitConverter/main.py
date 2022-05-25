"""File to launch the clock application."""

from converter import UnitConverter
from converter_ui import ConverterUI
from unittype import UnitType

if __name__ == '__main__':

    # Create a unit converter and give it to the ConverterUI
    # via the constructor. This is called Dependency Injection.
    converter = UnitConverter()
    ui = ConverterUI(converter)
    # load an initial unit to length type
    ui.load_units(UnitType.LENGTH)
    ui.run()
