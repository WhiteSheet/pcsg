Materializer
============

Materializers form the interface to external rendering applications.


.. currentmodule:: pcsg.util.materializer

.. autoclass:: pcsg.util.materializer.Materializer
    :members:



Materializer registry
`````````````````````

.. automethod:: pcsg.util.materializer.getMaterializers

.. automethod:: pcsg.util.materializer.getMaterializer

.. automethod:: pcsg.util.materializer.registerMaterializer



Singletons
``````````

.. automodule:: pcsg.util.materializer
    :members: OpenScad



Example: Render a .png image
----------------------------

.. code-block:: Python

    import pcsg

    # setup cache
    pcsg.util.cache.setup ('.pcsg.cache')

    # create sphere to render
    body = pcsg.solid.Sphere (radius = 1)

    # setup attributes
    attributes = pcsg.attributes.Attributes ({
        # camera settings
        'camera.view':          (0, 0, 0, 70, 0, 30, 12),
        'camera.projection':    "perspective",

        # render settings
        'render.width':         800,
        'render.height':        600,
        'render.quality':       6,
        'render.antialias':     6
    })

    # render test.png image
    absPath = pcsg.util.materializer.OpenScad.render (
        body, 
        attributes, 
        'test',
        'png'
    )



Example: Materialize a .stl file
--------------------------------

.. code-block:: Python

    import pcsg

    # setup cache
    pcsg.util.cache.setup ('.pcsg.cache')

    # create sphere to render
    body = pcsg.solid.Sphere (radius = 1)

    # setup attributes
    attributes = pcsg.attributes.Attributes ({
        # rasterizing settings
        'rasterize.minSize':    0.01
    })

    # materialize to test.stl file
    pcsg.util.materializer.OpenScad.materialize (
        body, 
        attributes, 
        'test',
        'stl'
    )

