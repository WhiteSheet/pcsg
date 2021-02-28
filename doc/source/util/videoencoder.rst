Video Encoder
=============

Video encoders are used to create a video from a frame sequence.


.. currentmodule:: pcsg.util.encoder

.. autoclass:: pcsg.util.encoder.Encoder
    :members:



Encoder registry
````````````````

.. autofunction:: pcsg.util.encoder.getEncoders

.. autofunction:: pcsg.util.encoder.getEncoder

.. autofunction:: pcsg.util.encoder.registerEncoder

.. autofunction:: pcsg.util.encoder.parseSettings

.. autofunction:: pcsg.util.encoder.extension



Singletons
``````````

.. automodule:: pcsg.util.encoder
    :members: MP4H264, AviH264



Example: Encoding a list of frames to a video file
--------------------------------------------------

.. code-block:: Python

    import pcsg

    # list of frames to process
    frames = # [ ... list of frame file names ... ]

    # frames per second
    fps = 60

    # encoding format
    format = "mp4.insane"

    # parse format string
    instance, preset = pcsg.pcsg.util.encoder.parseSettings (format)

    # run video encoder
    cacheFile = instance.encode (frames, fps, preset = preset)
