import math
from pathlib import Path

from wand.color import Color
from wand.image import Image


def __resize(img: Image, max_dim: int):
    width, height = img.size

    if width > height:
        height = round(height / width * max_dim)
        img.resize(max_dim, height)
    else:
        width = round(width / height * max_dim)
        img.resize(width, max_dim)


def __get_sprite_size(images: int) -> tuple[int, int]:
    sqrt = math.sqrt(images)
    columns = round(sqrt)
    rows = math.ceil(images / columns)

    return (rows, columns)


def main():

    input_dir = Path("C:/Users/Kasper Fromm/Desktop/traffic-signs/svg")
    output_dir = input_dir.parent.joinpath("png")
    output_dir.mkdir(parents=True, exist_ok=True)

    svg_files = list(
        Path("C:/Users/Kasper Fromm/Desktop/traffic-signs/svg").glob("*.svg")
    )

    columns = __get_sprite_size(len(svg_files))

    sprite = Image(width=400, height=20, background=Color("transparent"))

    left = 0

    for svg_file in svg_files:
        with Image(
            filename=svg_file.as_posix(),
            background=Color("transparent"),
        ) as img:
            __resize(img, 20)
            with img.convert("png") as png_img:
                sprite.composite(png_img, left, 0)
                left += 25
                # png_img.save(
                #     filename=output_dir.joinpath(
                #         svg_file.with_suffix(".png").name
                #     ).as_posix()
                # )
    sprite.save(filename=output_dir.joinpath("sprite.png").as_posix())


if __name__ == "__main__":
    main()
