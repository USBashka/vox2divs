from voxypy.models import Entity, Voxel


SIDES = (
    (0, 0, 1),  # 0 FRONT
    (0, 0, -1), # 1 BACK
    (0, 1, 0),  # 2 UP
    (0, -1, 0), # 3 DOWN
    (1, 0, 0),  # 4 RIGHT
    (-1, 0, 0)  # 5 LEFT
)


def make_div(pos: tuple[3], side: int, color: tuple[4]) -> str:
    """Makes <div>-tag with given pos"""
    pass


def generate(vox_file: str) -> str:
    """Generate html-code from vox-file"""

    entity = Entity().from_file(vox_file)

    palette = entity.get_palette()

    for voxel in entity.nonzero():
