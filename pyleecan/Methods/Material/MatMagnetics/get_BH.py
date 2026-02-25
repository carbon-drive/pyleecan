def get_BH(self):
    """Return the B(H) curve of the material according to the Import object.
    If there is no B(H) curve linear data are computed from mur_lin.

    Parameters
    ----------
    self : MatMagnetics
        a MatMagnetics object

    Returns
    -------
    BH: numpy.ndarray
        B(H) values (two colums matrix: H and B(H))

    """

    BH = None
    if self.BH_curve is not None:
        try:
            BH = self.BH_curve.get_data()
        except AttributeError:
            BH = None

        if BH is None or getattr(BH, "size", 0) == 0:
            BH = None
        elif len(BH.shape) != 2:
            raise BHShapeError(
                "BH must be a two colums matrix: H and B(H). Return shape: "
                + str(BH.shape)
            )
        if BH is not None and BH.shape[1] != 2:
            raise BHShapeError(
                "BH must be a two colums matrix: H and B(H). Return shape: "
                + str(BH.shape)
            )

        if BH is not None and self.is_BH_extrapolate:
            BH = self.ModelBH.fit_model(BH=BH)

    if BH is None:
        BH = self.ModelBH.get_BH()

    if self.mur_lin is None and BH is None:
        raise BHShapeError("There are no BH data availible. Check input data.")

    return BH


class BHShapeError(Exception):
    """Raised when the BH curve has not the expected shape"""

    pass


class BHDataMissing(Exception):
    """Raised when there are no BH curve data"""

    pass
