import math
from exampleimg import conf
from pcsg.construction import gear




def _setAttributes2D (attributes):
    return attributes.override ({
        'camera.view': (0, 0, 0, 0, 0, 0, 40)
    })




def _setAttributes (attributes):
    return attributes.override ({
        'camera.view': (0, 0, 0, 40, 0, 30, 48),
        'camera.projection': 'perspective'
    })




class Wheel:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Basic gear wheel.


        from pcsg.construction import gear

        item = gear.Wheel (n = 12, m = 1)
        """
        item = gear.Wheel (n = 12, m = 1, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)




class HerringboneWheel:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Herringbone gear wheel.


        from pcsg.construction import gear

        item = gear.Herringbone (n = 12, m = 1, b = 90)
        """
        item = gear.HerringboneWheel (n = 12, m = 1, b = 90, height = 4, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)




class InnerWheel:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Basic inner gear wheel.


        from pcsg.construction import gear

        item = gear.InnerWheel (n = 16, m = 1)
        """
        item = gear.InnerWheel (n = 16, m = 1, attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes (attributes)
        return ((a, item),)




class InnerHerringboneWheel:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Basic inner Herringbone gear wheel.


        from pcsg.construction import gear

        item = gear.InnerHerringboneWheel (n = 16, m = 1, b = 90)
        """
        item = gear.InnerHerringboneWheel (n = 16, m = 1, b = 90, height = 4, attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes (attributes)
        a = a.override ({'camera.view': (0, 0, 0, 50, 0, 30, 48)})
        return ((a, item),)
