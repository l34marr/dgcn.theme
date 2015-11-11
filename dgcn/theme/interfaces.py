from zope.interface import Interface


class ICustomTheme(Interface):
    """Marker interface that defines a Zope 3 browser layer.
    """

    def getBuilding():
        """Returns Specific Items.
        """

    def getClothes():
        """Returns Specific Items.
        """

    def getShip():
        """Returns Specific Items.
        """

    def getRiver():
        """Returns Specific Items.
        """

    def getLighthouse():
        """Returns Specific Items.
        """

