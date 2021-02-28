.. _Attributes:

Attributes
==========

.. currentmodule:: pcsg.tree

.. _Attribute:

.. autoclass:: Attributes
    :show-inheritance:
    :members:



Rasterizing Attributes
``````````````````````

.. _RasterizingAttributes:

Rasterizing attributes are used by the materializers and renderers when a geometry gets converted into a :ref:`Polygon<Polygon>` or :ref:`Polyhedron<Polyhedron>`.
Rasterizing attributes are evaluted for each :ref:`Item<Item>`.

.. code-block:: Python

    {
        # Minimum angular accuracy for rasterizing in degree.
        # Data type: positive float.
        'rasterize.minAngle':       1,

        # Maximum size error in units.
        # Data type: positive float.
        'rasterize.minSize':        0.01,

        # Rasterize with fixed number of segments.
        # Data type: positive integer.
        'rasterize.fixedCount':     None,

        # Number of slices for rasterizing LinearExtrude's.
        # Data type: positive integer.
        'rasterize.fixedSlices':    None       
    }
    


Render Attributes
`````````````````

.. _RenderAttributes:

Render attributes are used when rendering images.
The renderer will get the rendering attributes from the root csg tree :ref:`Node<Node>`.

.. code-block:: Python

    {
        # Size of rendered image.
        # Data type: positive integer.
        'render.width':             800,
        'render.height':            600,

        # Rendering quality. Higher values mean better quality.
        # Data type: integer in range 1 to 12.
        'render.quality':           1,
        'render.antialias':         1,

        # OpenScad rendering decoration attributes.
        # Data type: boolean.
        'render.view.axis':         False,
        'render.view.scales':       False,
        'render.view.crosshairs':   False,

        # Color scheme for OpenScad.
        # Data type: string.
        'render.colorScheme':       "PcsgTheme"
    }



Camera Attributes
`````````````````

.. _CameraAttributes:

Camera attributes are used when rendering images.
The renderer will get the camera attributes from the root csg tree :ref:`Node<Node>`.

.. code-block:: Python

    {
        # Camera view vector.
        # Data type:
        #
        # tuple (
        #     eyeX,
        #     eyeY,
        #     eyeZ,
        #     centerX,
        #     centerY,
        #     centerZ
        # )
        #
        # or:
        #
        # tuple (
        #     translateX,
        #     translateY,
        #     translateZ,
        #     rotateX,
        #     rotateY,
        #     rotateZ,
        #     distance
        # )
        'camera.view':              None,

        # Camera projection type:
        # Data type: string-option:
        #     "orthogonal",
        #     "perspective"
        'camera.projection':        "perspective"
    }
