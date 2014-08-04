"""
This module is going to implement a Rubik's Cube

It implements like this
________________
|    |    |    |
| 00 | 01 | 02 |
|____|____|____|
|    |    |    |
| 07 |Cntr| 03 |
|____|____|____|
|    |    |    |
| 06 | 05 | 04 |
|____|____|____|

"""

class Square(Object):
    """
    Square(colour, face, index), implements a square (sticker) on a cube.
    """
    def __init__():
        pass
    def __str__():
        pass
    def __repr__():
        pass
    def set_position():
        """Reset the position (index) of the square in a cube."""
        pass
    def set_colour():
        """Reset the colour of the square."""
        pass

class Face(Object):
    """
    Face(face, (?:[01, 02, ..., 08])), implements a face on a cube.
    """
    def __init__():
        pass
    def __str__():
        pass
    def __repr__():
        pass
    def rotate():
        """Rotate this face clockwise or counter-clockwise."""
        pass
    def get_horz_row():
        """Get the horizontal row(s) of the face."""
        pass
    def get_vert_row():
        """Get the vertical row(s) of the face."""
        pass
    def get_by_index():
        """Get the square by the index."""
        pass
    def get_by_2d():
        """Get the square by 2d position."""
        pass
    def get_colour():
        """Get the centre square of the face."""
        pass

class Cube(Object):
    """
    Cube([face * 6]), implements a whole cube.
    """
    def __init__():
        pass
    def __str__():
        pass
    def __repr__():
        pass
    def _outer_layer_rotate():
        """Perform the actions like U R' D2 L' """
        pass
    def _cube_rotation():
        """Perform the actions like x y' z2 """
        pass
    def _double_layers_rotate():
        """Perform the actions like u r' d2 l' """
        pass
    def _middle_layer_rotate():
        """Perform the actions like M S' E2"""
        pass
    def perform_action():
        """Perform an action."""
        pass

