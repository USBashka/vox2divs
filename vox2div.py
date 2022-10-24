from numpy import add as np_add
from voxypy.models import Entity, Voxel


SIDES = (
    (0, 0, 1),  # 0 FRONT
    (0, 0, -1), # 1 BACK
    (0, 1, 0),  # 2 UP
    (0, -1, 0), # 3 DOWN
    (1, 0, 0),  # 4 RIGHT
    (-1, 0, 0)  # 5 LEFT
)

ROTATIONS = (
    (0, 0, 0),  # 0 FRONT
    (0, 180, 0), # 1 BACK
    (90, 0, 0),  # 2 UP
    (-90, 0, 0), # 3 DOWN
    (0, 90, 0),  # 4 RIGHT
    (0, -90, 0)  # 5 LEFT
)


def make_div(pos: tuple[3], side: int, color: tuple[4]) -> str:
    """Makes <div>-tag with given pos"""
    
    return f"<div style=\"transform: rotateX({ROTATIONS[side][1]}deg) translate3d({pos[0]+SIDES[side][0]/2}em, {pos[1]+SIDES[side][2]/2}em, {pos[2]+SIDES[side][1]/2}em); background: rgb({color[0]}, {color[2]}, {color[2]})\"></div>"


def generate(vox_file: str) -> str:
    """Generate html-code from vox-file"""

    result = ""

    entity = Entity().from_file(vox_file)

    palette = entity.get_palette()

    for voxel in entity.nonzero():
        for si, side in enumerate(SIDES):
            if tuple(np_add(voxel, side)) not in entity.nonzero():
                result += make_div(voxel, si, palette[int(entity.get(*voxel))])
    
    return result


def main():
    with open("out.html", "w") as f:
        f.write(generate("vox-examples\cat.vox"))

if __name__ == "__main__":
    main()