from dataclasses import dataclass
from enum import Enum

MAIN_CURRENCY = "$"  # USD


class MaterialUnit(Enum):
    """Supported measurement units for materials."""

    KILOGRAM = "kg"
    METER = "m"
    SQUARE_METER = "m^2"
    CUBIC_METER = "m^3"
    PIECE = "pc"
    LITER = "l"


@dataclass
class Material:
    """Represents a material with a price per measurement unit."""

    name: str
    price_per_unit: float
    unit: MaterialUnit

    def __str__(self) -> str:
        return f"{self.name} is {MAIN_CURRENCY}{self.price_per_unit}/{self.unit.value}"


@dataclass
class MaterialUsage:
    """Represents a quantity of material used in a product or scenario."""

    material: Material
    quantity: float

    @property
    def cost(self) -> float:
        return self.quantity * self.material.price_per_unit
