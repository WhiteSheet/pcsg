import math
import pcsg
from exampleimg import runtime
from exampleimg import conf




def _setAttributes (attributes):
    return attributes.override ({
        'camera.view': (0, 0, 0, 0, 0, 0, 8)
    })




def _posttransform (item):
    return pcsg.transform.Translate (pcsg.solid.LinearExtrude (height = 1, children = (item)), z = 2)




class Circle:
    """
    """

    @staticmethod
    def exampleWithRadius (attributes, isThumbnail):
        """
        Circle created with *radius* = 1


        from pcsg import shape

        item = shape.Circle (radius = 1)
        """
        item = pcsg.shape.Circle (radius = 1, attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWithDiameter (attributes, isThumbnail):
        """
        Circle created with *diameter* = 1


        from pcsg import shape

        item = shape.Circle (diameter = 1)
        """
        item = pcsg.shape.Circle (diameter = 1, attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)




class Square:
    """
    """

    @staticmethod
    def exampleWithSize_a (attributes, isThumbnail):
        """
        Square created with *size* = (1, 2)


        from pcsg import shape

        item = shape.Square (size = (1, 2))
        """
        item = pcsg.shape.Square (size = (1, 2), attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWithSize_b (attributes, isThumbnail):
        """
        Square created with *size* = (2, 1)


        from pcsg import shape

        item = shape.Square (size = (2, 1))
        """
        item = pcsg.shape.Square (size = (2, 1), attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWithSize_c (attributes, isThumbnail):
        """
        Square created with *size* = 2


        from pcsg import shape

        item = shape.Square (size = 2)
        """
        item = pcsg.shape.Square (size = 2, attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)




class Polygon:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Simple Polygon


        from pcsg import shape

        item = shape.Polygon (
            points = (
                        (-1, 0),
                        (-1, 1),
                        (1, 1)
                     )
        )
        """
        points = (
                    (-1, 0),
                    (-1, 1),
                    (1, 1)
        )
        item = pcsg.shape.Polygon (points = points, attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Polygon with a hole


        from pcsg import shape

        item = shape.Polygon (
            points =  (
                        # points for outer shape:
                        (-1, 0),
                        (-1, 1),
                        (1, 1),
                        # points for cutout:
                        (-0.8, 0.2),
                        (-0.8, 0.8),
                        (-0.3, 0.8)
                      ),
            outer =   (0, 1, 2),
            cutouts = ((3, 4, 5),)
        )
        """
        item = pcsg.shape.Polygon (
            points = (
                        (-1, 0),
                        (-1, 1),
                        (1, 1),
                        (-0.8, 0.2),
                        (-0.8, 0.8),
                        (-0.3, 0.8)
                     ),
            outer = (0, 1, 2),
            cutouts = ((3, 4, 5),),
            attributes = {'material': conf.DefaultMaterial}
        )
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def example_c (attributes, isThumbnail):
        """
        Polygon with a multiple holes


        from pcsg import shape

        item = shape.Polygon (
            points =  (
                        # points for outer shape:
                        (-1, 0),
                        (-1, 1),
                        (1, 1),
                        # points for first cutout:
                        (-0.8, 0.2),
                        (-0.8, 0.8),
                        (-0.3, 0.8),
                        # points for second cutout:
                        (0, 0.8),
                        (0.5, 0.8),
                        (0, 0.6)
                      ),
            outer =   (0, 1, 2),
            cutouts = ((3, 4, 5), (6, 7, 8))
        )
        """
        item = pcsg.shape.Polygon (
            points = (
                        (-1, 0),
                        (-1, 1),
                        (1, 1),
                        (-0.8, 0.2),
                        (-0.8, 0.8),
                        (-0.3, 0.8),
                        (0, 0.8),
                        (0.5, 0.8),
                        (0, 0.6)
                     ),
            outer = (0, 1, 2),
            cutouts = ((3, 4, 5), (6, 7, 8)),
            attributes = {'material': conf.DefaultMaterial}
        )
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def example_d (attributes, isThumbnail):
        """
        Polygons can be created by rasterizing any Shape class


        import pcsg

        # create outline
        outline = pcsg.transform.Rotate (
            pcsg.shape.Square (size = 1),
            rz = 5
        )
        
        # rasterize outline to Polygon
        item = pcsg.shape.Polygon.fromShape (
            outline,
            attributes
        )
        """
        outline = pcsg.transform.Rotate (
            pcsg.shape.Square (size = 1),
            rz = 5
        )
        
        item = pcsg.shape.Polygon.fromShape (
            outline,
            attributes
        )

        # projection
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def example_e (attributes, isThumbnail):
        """
        Rasterizing a shape retruns a group of Polygons when the geometry renders to disjunct areas


        import pcsg

        # create a composed solid
        volume = pcsg.tree.Group (
            children = (
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (1.1),
                    x = -0.7,
                    z = -0.8
                ),
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (0.9),
                    x = 0.7,
                    z = -0.8
                )
            )
        )

        # project solid to x/y plane
        projection = pcsg.shape.Projection (
            volume,
            cut = True
        )
        
        # get polygons from projection
        polygons = pcsg.shape.Polygon.fromShape (
            projection,
            attributes
        )

        # result will be a group node.
        assert isinstance (polygons, pcsg.tree.Group)

        # colorize polygons inside group
        polygons = pcsg.algorithms.distributeColors (polygons)
        """
        solid = pcsg.tree.Group (
            children = (
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (1.1),
                    x = -0.7,
                    z = -0.8,
                    attributes = {
                        'material': conf.getMaterial (0)
                    }
                ),
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (0.9),
                    x = 0.7,
                    z = -0.8,
                    attributes = {
                        'material': conf.getMaterial (1)
                    }
                )
            )
        )

        # polygons
        projection = pcsg.shape.Projection (
            solid,
            cut = True
        )
        
        polygons = pcsg.shape.Polygon.fromShape (
            projection,
            attributes
        )

        polygons = pcsg.algorithms.distributeColors (polygons, colorGenerator = conf.colorGenerator)

        # scene
        cuttingPlane = pcsg.solid.Cube ((4, 2.5, 0.01), attributes = {'material': conf.CuttingPlaneMaterial})
        sourceScene = pcsg.tree.Group ((solid, cuttingPlane))

        # projection
        a = _setAttributes (attributes)
        sceneA = _setAttributes (attributes).override({
            'camera.view': (0, 0, 0, 70, 0, 30, 12)
        })
        return ((sceneA, sourceScene), (a, polygons))


    @staticmethod
    def example_f (attributes, isThumbnail):
        """
        Rasterizing a shape retruns Empty if it containes no areas


        import pcsg

        # create empty projection
        solid = pcsg.shape.Projection (
            pcsg.transform.Translate (
                pcsg.solid.Sphere (1.1),
                z = -2
            ),
            cut = True
        )

        # get empty polygon
        item = pcsg.shape.Polygon.fromShape (
            solid,
            attributes
        )

        # result will be an empty node.
        assert isinstance (item, pcsg.tree.Empty)
        """
        solid = pcsg.transform.Translate (
            pcsg.solid.Sphere (1.1),
            z = -2,
            attributes = {
                'material': conf.getMaterial (0)
            }
        )

        # scene
        cuttingPlane = pcsg.solid.Cube ((4, 2.5, 0.01), attributes = {'material': conf.CuttingPlaneMaterial})
        sourceScene = pcsg.tree.Group ((solid, cuttingPlane))

        sceneA = _setAttributes (attributes).override({
            'camera.view': (0, 0, 0, 70, 0, 30, 12)
        })
        return ((sceneA, sourceScene),)




class Bezier:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Shape from bezier curves


        from pcsg import shape

        item = shape.Bezier (
            curves = (
                        ((-2, -1.3), (-2, 0), (-2, 0), (0, 1.3)  ),
                        ((0, 1.3),   (1, 2),  (2, 1),  (2, -1.3) ),
                        ((2, -1.3),  (0, -1), (0, -1), (-2, -1.3))
                     )
        )
        """
        item = pcsg.shape.Bezier (
            curves = (
                        ((-2, -1.3), (-2, 0), (-2, 0), (0, 1.3)),
                        ((0, 1.3), (1, 2), (2, 1), (2, -1.3)),
                        ((2, -1.3), (0, -1), (0, -1), (-2, -1.3))
                     ),
            attributes = {'material': conf.DefaultMaterial}
        )
        a = _setAttributes (attributes)
        return ((a, item),)




def _exampleCurveFunction (phi):
    c1 = (1 + 0.9 * math.cos (8 * phi))
    c2 = (1 + 0.1 * math.cos (24 * phi))
    c3 = (0.9 + 0.1 * math.cos (200 * phi))
    c4 = (1 + math.sin (phi))
    return (1 + 5 * c1 * c2 * c3 * c4) * 0.1




class Polar:
    """
    """


    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Shape defined by polar curve function


        import math
        from pcsg import shape

        def curveFunction (phi):
            c1 = (1 + 0.9 * math.cos (8 * phi))
            c2 = (1 + 0.1 * math.cos (24 * phi))
            c3 = (0.9 + 0.1 * math.cos (200 * phi))
            c4 = (1 + math.sin (phi))
            return (1 + 5 * c1 * c2 * c3 * c4) * 0.1

        item = shape.Polar (
            curveFunction
        )
        """
        item = pcsg.shape.Polar (_exampleCurveFunction)
        a = _setAttributes (attributes)
        return ((a, item),)




class Projection:
    """
    """

    @staticmethod
    def example_a (attributes, isThumbnail):
        """
        Orthogonal projection of solid


        import pcsg

        # create solid
        volume = pcsg.transform.Rotate (
            pcsg.solid.Cylinder (height = 3, radius1 = 2, radius2 = 0),
            rx = -45,
            ry = 10
        )

        # orthogonal projection to x/y plane
        item = pcsg.shape.Projection (
            volume,
            cut = False
        )
        """
        body = pcsg.transform.Rotate (
            pcsg.solid.Cylinder (height = 2, radius1 = 1, radius2 = 0),
            rx = -45,
            ry = 10,
            attributes = {'material': conf.getMaterial (2)}
        )

        item = pcsg.shape.Projection (
            body,
            cut = False,
            attributes = {'material': conf.DefaultMaterial}
        )
        a = _setAttributes (attributes)
        return ((a, body), (a, item))


    @staticmethod
    def example_b (attributes, isThumbnail):
        """
        Intersection of solid with x/y plane


        import pcsg

        # create solid
        solid = pcsg.boolean.Union (
            children = (
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (1.1),
                    x = -0.7,
                    z = -0.8
                ),
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (0.9),
                    x = 0.7,
                    z = -0.8
                )
            )
        )

        # projection by cutting with x/y plane
        item = pcsg.shape.Projection (
            solid,
            cut = True
        )
        """
        solid = pcsg.tree.Group (
            children = (
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (1.1),
                    x = -0.7,
                    z = -0.8,
                    attributes = {
                        'material': conf.getMaterial (0)
                    }
                ),
                pcsg.transform.Translate (
                    pcsg.solid.Sphere (0.9),
                    x = 0.7,
                    z = -0.8,
                    attributes = {
                        'material': conf.getMaterial (1)
                    }
                )
            )
        )

        # scene
        cuttingPlane = pcsg.solid.Cube ((4, 2.5, 0.01), attributes = {'material': conf.CuttingPlaneMaterial})
        sourceScene = pcsg.tree.Group ((solid, cuttingPlane))

        # projection
        projection = pcsg.shape.Projection (solid, cut = True, attributes = {'material': conf.DefaultMaterial})
        a = _setAttributes (attributes)
        sceneA = _setAttributes (attributes).override({
            'camera.view': (0, 0, 0, 70, 0, 30, 12)
        })
        return ((sceneA, sourceScene), (a, projection))
