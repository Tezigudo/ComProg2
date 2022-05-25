"""An enumeration of known types of units."""
import enum


class UnitType(enum.Enum):
    """Define the unittypes here.  The value is the printable type name."""
    LENGTH = "Length"
    AREA = "Area"    # you can change Area to some other unittype
    VOLUME = "Volume"
    TEMPERATURE = "Temperature"

    def __str__(self) -> str:
        """Return the unittype name suitable for printing."""
        return self.value
