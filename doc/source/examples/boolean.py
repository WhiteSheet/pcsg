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




# Examples for boolean.Union
class Union:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Create union of two solid elements


        import pcsg

        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Union ((body1, body2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        unionMaterial = conf.getMaterial (3)
        item = pcsg.boolean.Union (
            (
                (
                    body1.copy (attributes = {'material': unionMaterial}), 
                    body2.copy (attributes = {'material': unionMaterial})
                )
            ),
            attributes = {'material': unionMaterial}
        )

        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Create union of two shape elements


        import pcsg

        outline1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5
        )

        outline2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Union ((outline1, outline2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        unionMaterial = conf.getMaterial (3)
        item = pcsg.boolean.Union (
            (
                (
                    body1.copy (attributes = {'material': unionMaterial}), 
                    body2.copy (attributes = {'material': unionMaterial})
                )
            ),
            attributes = {'material': unionMaterial}
        )

        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))




# Examples for boolean.Difference
class Difference:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Create difference of two solid elements


        import pcsg

        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Difference ((body1, body2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        item = pcsg.boolean.Difference (
            (
                (
                    body1, 
                    body2
                )
            ),
            attributes = {'material': conf.getMaterial (0)}
        )

        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Create difference of two shape elements


        import pcsg

        outline1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5
        )

        outline2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Difference ((outline1, outline2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        item = pcsg.boolean.Difference (
            (
                (
                    body1,
                    body2
                )
            ),
            attributes = {'material': conf.getMaterial (0)}
        )

        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))




# Examples for boolean.Intersection
class Intersection:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Create intersection of two solid elements


        import pcsg

        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Intersection ((body1, body2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.solid.Sphere (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        unionMaterial = conf.getMaterial (3)
        item = pcsg.boolean.Intersection (
            (
                (
                    body1.copy (attributes = {'material': unionMaterial}), 
                    body2.copy (attributes = {'material': unionMaterial})
                )
            ),
            attributes = {'material': unionMaterial}
        )

        a = _setAttributes (attributes)
        return ((a, body),(a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Create intersection of two shape elements


        import pcsg

        outline1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5
        )

        outline2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5
        )

        item = pcsg.transform.Intersection ((outline1, outline2))
        """
        body1 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = -0.5,
            attributes = {'material': conf.getMaterial (0)}
        )

        body2 = pcsg.transform.Translate (
            pcsg.shape.Circle (radius = 1),
            x = 0.5,
            attributes = {'material': conf.getMaterial (1)}
        )

        body = pcsg.tree.Group ((body1, body2))

        unionMaterial = conf.getMaterial (3)
        item = pcsg.boolean.Intersection (
            (
                (
                    body1.copy (attributes = {'material': unionMaterial}), 
                    body2.copy (attributes = {'material': unionMaterial})
                )
            ),
            attributes = {'material': unionMaterial}
        )

        a = _setAttributes2D (attributes)
        return ((a, body),(a, item))
