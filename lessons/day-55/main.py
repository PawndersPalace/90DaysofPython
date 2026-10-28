from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


start = Point(2, 5)
print(start)
print(f"Coordinates: ({start.x}, {start.y})")
