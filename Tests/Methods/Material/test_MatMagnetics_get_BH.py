import numpy as np

from pyleecan.Classes.MatMagnetics import MatMagnetics


def test_get_BH_default_importmatrix():
    mat = MatMagnetics()
    BH = mat.get_BH()
    assert BH is None or isinstance(BH, np.ndarray)
