import math
import pcsg
from exampleimg import runtime
from exampleimg import conf




def _setAttributes2D (attributes):
    return attributes.override ({
        'camera.view': (0, 0, 0, 0, 0, 0, 8)
    })




def _setAttributes (attributes):
    return attributes.override ({
        'camera.view': (0, 0, 0, 70, 0, 30, 12),
        'camera.projection': 'perspective'
    })




def _posttransform (item):
    return pcsg.transform.Translate (pcsg.solid.LinearExtrude (height = 1, children = (item)), z = 2)




# Examples for transform.Translate
class Translate:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Transform solid on x-axis


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Translate (body, y = 2)
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Translate (body, y = 2, attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Transform solid on x- and y-axis


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Translate (body, x = 1, y = 2)
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Translate (body, x = 1, y = 2, attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_c (attributes, isThumbnail):
        """
        Transform solid by vector


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Translate (body, (1, 2, -2))
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Translate (body, (1, 2, -2), attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_d (attributes, isThumbnail):
        """
        Transform shape by vector


        import pcsg

        body = pcsg.shape.Circle (radius = 0.5)

        item = pcsg.transform.Translate (body, (0.5, 1))
        """
        body = pcsg.shape.Circle (radius = 0.5, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Translate (body, (0.5, 1), attributes = {'material': conf.getMaterial (1)})
        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))




# Examples for transform.Scale
class Scale:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Scale solid on x-axis


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Scale (body, sy = 2)
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Scale (body, sy = 2, attributes = {'material': conf.getMaterial (2)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Scale solid on x- and y-axis


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Scale (body, sx = 0.6, sy = 1.3)
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Scale (body, sx = 0.6, sy = 1.3, attributes = {'material': conf.getMaterial (2)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_c (attributes, isThumbnail):
        """
        Scale solid by vector


        import pcsg

        body = pcsg.solid.Sphere (radius = 1)

        item = pcsg.transform.Scale (body, (1.7, 0.9, 1.2))
        """
        body = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Scale (body, (1.7, 0.9, 1.2), attributes = {'material': conf.getMaterial (2)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_d (attributes, isThumbnail):
        """
        Scale shape by vector


        import pcsg

        body = pcsg.shape.Circle (radius = 0.5)

        item = pcsg.transform.Scale (body, (0.5, 1))
        """
        body = pcsg.shape.Circle (radius = 0.5, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Scale (body, (0.5, 1), attributes = {'material': conf.getMaterial (2)})
        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))




# Examples for transform.Rotate
class Rotate:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Rotate solid around x-axis


        import pcsg

        body = pcsg.solid.Cube (size = 1)

        item = pcsg.transform.Rotate (body, rx = 25)
        """
        body = pcsg.solid.Cube (size = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Rotate (body, rx = 25, attributes = {'material': conf.getMaterial (3)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Rotate solid around x- and y-axis


        import pcsg

        body = pcsg.solid.Cube (size = 1)

        item = pcsg.transform.Rotate (body, rx = 25, ry = 15)
        """
        body = pcsg.solid.Cube (size = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Rotate (body, rx = 25, ry = 15, attributes = {'material': conf.getMaterial (3)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_c (attributes, isThumbnail):
        """
        Rotate solid around vector


        import pcsg

        body = pcsg.solid.Cube (size = 1)

        item = pcsg.transform.Rotate (body, (10, 20, 35))
        """
        body = pcsg.solid.Cube (size = 1, attributes = {'material': conf.getMaterial (0)})
        item = pcsg.transform.Rotate (body, (10, 20, 35), attributes = {'material': conf.getMaterial (3)})
        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_d (attributes, isThumbnail):
        """
        Rotate shape around z-axis


        import pcsg

        body = pcsg.transform.Translate (
            pcsg.shape.Square (size = 0.5),
            x = 1
        )

        item = pcsg.transform.Rotate (body, rz = 30)
        """
        body = pcsg.transform.Translate (
            pcsg.shape.Square (size = 0.5),
            x = 1,
            attributes = {'material': conf.getMaterial (0)}
        )
        item = pcsg.transform.Rotate (body, rz = 30, attributes = {'material': conf.getMaterial (3)})
        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))
