from dataclasses import dataclass


@dataclass
class Operation:
    """Represents an operation with a rate per hour."""

    name: str
    rate_per_hour: float

    def __post_init__(self) -> None:
        if self.rate_per_hour <= 0:
            raise ValueError("Rate per hour must be greater than 0")


@dataclass
class OperationUsage:
    """Represents hours spent on an operation for a product or scenario."""

    operation: Operation
    hours: float

    @property
    def cost(self) -> float:
        return self.hours * self.operation.rate_per_hour

    def __post_init__(self) -> None:
        if self.hours <= 0:
            raise ValueError("Hours must be greater than 0")


print(
    OperationUsage(
        operation=Operation(name="extraction", rate_per_hour=100), hours=-10
    ).hours
)
