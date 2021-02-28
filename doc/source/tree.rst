The *pcsg* tree
===============

A scene is represented as a tree consisting of basic shapes, solids, transformations, and boolean operations.
Trees are immutable, once a tree is created, it can not be changed anymore. This pattern was chosen for efficient
parallel processing in future releases of *pcsg*.


.. toctree::
    tree/baseclasses
    tree/shape
    tree/solid
    tree/transform
    tree/boolean
    tree/attributes
    tree/construction
    tree/howtoextend
    