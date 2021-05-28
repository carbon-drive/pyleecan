# -*- coding: utf-8 -*-
from ....Classes.Hole import Hole


def comp_radius_mid_yoke(self):
    """Compute the Lamination middle of the yoke radius

    Parameters
    ----------
    self : LamHole
        A LamHole object

    Returns
    -------
    Ry: float
        middle of the yoke radius [m]

    """

    Rmax = max(self.Rext, self.Rint)
    Rmin = min(self.Rext, self.Rint)
    for hole in self.hole:
        if type(hole) is not Hole:
            (Rmin_hole, Rmax_hole) = hole.comp_radius()
            Rmin = min(Rmin, Rmin_hole, Rmax_hole)
            Rmax = max(Rmax, Rmin_hole, Rmax_hole)

    return (Rmin + Rmax) / 2

