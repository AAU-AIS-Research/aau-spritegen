from dataclasses import dataclass

from pyvips import Image


@dataclass
class SpriteIcon:
    width: int
    height: int
    x: int
    y: int
    pixel_ratio: float


@dataclass
class Sprite:
    image: Image
    icons: dict[str, SpriteIcon]
