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




# Examples for shape.Sphere
class Sphere:
    """
    """

    @staticmethod
    def exampleWithRadius (attributes, isThumbnail):
        """
        Sphere created with *radius* = 1


        from pcsg import solid

        item = solid.Sphere (radius = 1)
        """
        item = pcsg.solid.Sphere (radius = 1, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWithDiameter (attributes, isThumbnail):
        """
        Sphere created with *diameter* = 1


        from pcsg import solid

        item = solid.Sphere (diameter = 1)
        """
        item = pcsg.solid.Sphere (diameter = 1, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)




# Examples for shape.Cube
class Cube:
    """
    """

    @staticmethod
    def exampleWith_a (attributes, isThumbnail):
        """
        Cube created with *size* = (1, 2, 3)


        from pcsg import solid

        item = solid.Cube (size = (1, 2, 3))
        """
        item = pcsg.solid.Cube (size = (1, 2, 3), attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWith_b (attributes, isThumbnail):
        """
        Cube created with *size* = 2


        from pcsg import solid

        item = solid.Cube (size = 2)
        """
        item = pcsg.solid.Cube (size = 2, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)




# Examples for shape.Cylinder
class Cylinder:
    """
    """
    
    @staticmethod
    def exampleWith_a (attributes, isThumbnail):
        """
        Cylinder created with *height* = 2 and *radius1* = 1


        from pcsg import solid

        item = solid.Cylinder (
            height = 3,
            radius1 = 1
        )
        """
        item = pcsg.solid.Cylinder (height = 3, radius1 = 1, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)
    
    @staticmethod
    def exampleWith_b (attributes, isThumbnail):
        """
        Cylinder created with *height* = 2, *radius1* = 1 and *radius2* = 0.5


        from pcsg import solid

        item = solid.Cylinder (
            height = 3,
            radius1 = 1,
            radius2 = 0.5
        )
        """
        item = pcsg.solid.Cylinder (height = 3, radius1 = 1, radius2 = 0.5, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)




# Examples for shape.Polyhedron
class Polyhedron:
    """
    """
    
    @staticmethod
    def exampleWith_a (attributes, isThumbnail):
        """
        Creating a polyhedron from points and faces


        import pcsg

        points = (
            (-1, -1, -1),
            (0, 3, -1),
            (1, -1, -1),
            (1, 1, 1)
        )

        faces = (
            (0, 1, 2),
            (0, 1, 3),
            (1, 2, 3),
            (2, 0, 3)
        )

        item = pcsg.solid.Polyhedron.fromUnoptimizedMesh (
            points,
            faces
        )
        """
        points = (
            (-1, -1, -1),
            (0, 3, -1),
            (1, -1, -1),
            (1, 1, 1)
        )

        faces = (
            (0, 1, 2),
            (0, 1, 3),
            (1, 2, 3),
            (2, 0, 3)
        )

        item = pcsg.solid.Polyhedron.fromUnoptimizedMesh (
            points,
            faces,
            attributes = {'material': conf.getMaterial (0)}
        )
        a = _setAttributes (attributes)
        return ((a, item),)
    
    
    @staticmethod
    def exampleWith_b (attributes, isThumbnail):
        """
        Importing a ployhedron from an .stl file


        from pcsg import solid

        item = solid.Polyhedron.fromFileSTL ('foo.stl')
        """
        body = pcsg.solid.Sphere (1)
        item = pcsg.solid.Polyhedron.fromSolid (body, attributes, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)

   
    @staticmethod
    def exampleWith_c (attributes, isThumbnail):
        """
        Importing a polyhedron from an .off file


        from pcsg import solid

        item = solid.Polyhedron.fromFileOFF ('bar.off')
        """
        body = pcsg.transform.Rotate (
            pcsg.solid.Cube (size = 1),
            [30, 30, 30]
        )
        item = pcsg.solid.Polyhedron.fromSolid (body, attributes, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)


    @staticmethod
    def exampleWith_d (attributes, isThumbnail):
        """
        Creating a polyhedron by rasterizing a solid


        import pcsg

        body = pcsg.solid.LinearExtrude (
            pcsg.transform.Translate (
                pcsg.transform.Scale (
                    pcsg.shape.Circle (diameter = 0.5),
                    sy = 2
                ),
                x = 1
            ),
            height = 3,
            twist = 720
        )

        item = pcsg.solid.Polyhedron.fromSolid (body, attributes)
        """
        body = pcsg.solid.LinearExtrude (
            pcsg.transform.Translate (
                pcsg.transform.Scale (
                    pcsg.shape.Circle (diameter = 0.5),
                    sy = 2
                ),
                x = 1
            ),
            height = 3,
            twist = 720
        )
        item = pcsg.solid.Polyhedron.fromSolid (body, attributes, attributes = {'material': conf.getMaterial (0)})
        a = _setAttributes (attributes)
        return ((a, item),)
    
    
    @staticmethod
    def exampleWith_e (attributes, isThumbnail):
        """
        When a converted solid or imported file has disjunct volumes,
        a group of polyhedrons will be returned


        import pcsg

        body = pcsg.boolean.Difference (
            (
                pcsg.solid.Cube (size = 2),
                pcsg.solid.Sphere (diameter = 2.9)
            )
        )

        # rasterize body
        polyhedrons = pcsg.solid.Polyhedron.fromSolid (body, attributes)

        # a group of polyhedrons is expected
        assert isinstance (polyhedrons, pcsg.tree.Group)

        # colorize polyhedrons inside group
        polyhedrons = pcsg.algorithms.distributeColors (polyhedrons)
        """
        body = pcsg.boolean.Difference (
            (
                pcsg.solid.Cube (size = 2),
                pcsg.solid.Sphere (diameter = 2.9)
            )
        )

        polyhedrons = pcsg.solid.Polyhedron.fromSolid (body, attributes)
        assert isinstance (polyhedrons, pcsg.tree.Group)

        polyhedrons = pcsg.algorithms.distributeColors (polyhedrons, colorGenerator = conf.colorGenerator)

        a = _setAttributes (attributes)
        return ((a, polyhedrons),)




# Examples for shape.LinearExtrude
class LinearExtrude:
    """
    """
    
    @staticmethod
    def exampleWith_a (attributes, isThumbnail):
        """
        Linear extrusion of a shape.


        import pcsg

        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3
        )
        """
        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3,
            attributes = {'material': conf.getMaterial (0)} 
        )
        a = _setAttributes (attributes)
        a2 = _setAttributes2D (attributes)
        return ((a2, outline), (a, item))
    

    @staticmethod
    def exampleWith_b (attributes, isThumbnail):
        """
        Linear extrusion of a shape with *twist*.


        import pcsg

        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3,
            twist = 450
        )
        """
        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3,
            twist = 450,
            attributes = {'material': conf.getMaterial (0)}
        )
        a = _setAttributes (attributes)
        a2 = _setAttributes2D (attributes)
        return ((a2, outline), (a, item))


    @staticmethod
    def exampleWith_c (attributes, isThumbnail):
        """
        Linear extrusion of a shape width *scale*.


        import pcsg

        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3,
            scale = 0.5
        )
        """
        outline = pcsg.transform.Translate (
            pcsg.transform.Scale (
                pcsg.shape.Circle (diameter = 1),
                sx = 0.5
            ),
            y = 0.7
        )
        item = pcsg.solid.LinearExtrude (
            outline,
            height = 3,
            scale = 0.5,
            attributes = {'material': conf.getMaterial (0)} 
        )
        a = _setAttributes (attributes)
        a2 = _setAttributes2D (attributes)
        return ((a2, outline), (a, item))




# Examples for shape.RotateExtrude
class RotateExtrude:
    """
    """
    
    @staticmethod
    def exampleWith_a (attributes, isThumbnail):
        """
        Rotated extrusion of a shape.


        import pcsg

        outline = pcsg.transform.Translate (
            pcsg.transform.Rotate (
                pcsg.shape.Square (size = 0.7),
                rz = 45
            ),
            x = 1
        )
        
        item = pcsg.solid.RotateExtrude (
            outline,
            angle = 90
        )
        """
        outline = pcsg.transform.Translate (
            pcsg.transform.Rotate (
                pcsg.shape.Square (size = 0.7),
                rz = 45
            ),
            x = 1
        )
        item = pcsg.solid.RotateExtrude (
            outline,
            angle = 180,
            attributes = {'material': conf.getMaterial (0)} 
        )
        a = _setAttributes (attributes)
        a2 = _setAttributes2D (attributes)
        return ((a2, outline), (a, item))
