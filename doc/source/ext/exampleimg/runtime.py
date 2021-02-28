import os
import inspect
from pcsg import tool
from pcsg.util import cache
from pcsg.attributes import Attributes
from pcsg.util.external import openscad




# default style definitions
ThumbnailWidth = 320
ThumbnailHeight = 240
ImageWidth = 800
ImageHeight = 600




def initialize (cachePath):
    """
    Initialize the example image builder.
    """
    cache.setup (cachePath)




def getDefaultAttributes ():
    """
    Get default attributes for running the exampleimg renderer.
    """
    attrs = Attributes.defaults ()
    attrs = attrs.override ({
        'render.quality':           1,
        'render.antialias':         1,
        'rasterize.minAngle':       2,
        'rasterize.minSize':        0.03,
        'camera.projection':        'orthogonal',
        'render.colorScheme':       'PcsgTheme'
    })
    return attrs




def getThumbnailImageAttributes ():
    """
    Return attributes for building a thumbnail image.
    """
    attrs = getDefaultAttributes ()
    attrs = attrs.override ({
        'render.width':             ThumbnailWidth,
        'render.height':            ThumbnailHeight,
        'render.view.axis':         True,
        'render.view.scales':       False
    })
    return attrs




def getImageAttributes ():
    """
    Return attributes for building an image.
    """
    attrs = getDefaultAttributes ()
    attrs = attrs.override ({
        'render.width':             ImageWidth,
        'render.height':            ImageHeight,
        'render.view.axis':         True,
        'render.view.scales':       True
    })
    return attrs




def renderImageThumbnail (createSceneFunc, cachePath):
    """
    Renders an example image thumbnail.
    """
    if inspect.isclass (createSceneFunc):
        if issubclass (createSceneFunc, tool.Tool):
            # calculate example output name
            outputNamePrefix = cachePath + os.path.sep + str (createSceneFunc.__qualname__) + ".thumb"

            # create and run tool instance
            instance = createSceneFunc ()
            commandLineOptions = [
                'render',
                outputNamePrefix,
                '--fmt', 'png',
                '--cache', cachePath,
                '-w', str (ThumbnailWidth),
                '-h', str (ThumbnailHeight),
                '-z'
            ]
            instance.run (commandLineOptions)

            # return output path
            return [outputNamePrefix + '.png']
        else:
            assert False, "unexpected class"

    else:
        # render csg tree
        attributes = getThumbnailImageAttributes ()
        result = createSceneFunc (attributes, True)
        images = []
        for pair in result:
            images.append (openscad.getRendering ('png', pair[1], pair[0]))
        return images




def renderImage (createSceneFunc, cachePath):
    """
    Renders an example image.
    """
    if inspect.isclass (createSceneFunc):
        if issubclass (createSceneFunc, tool.Tool):
            # calculate example output name
            outputNamePrefix = cachePath + os.path.sep + str (createSceneFunc.__qualname__) + ".img"

            # create and run tool instance
            instance = createSceneFunc ()
            commandLineOptions = [
                'render',
                outputNamePrefix,
                '--fmt', 'png',
                '--cache', cachePath,
                '-w', str (ImageWidth),
                '-h', str (ImageHeight),
                '-z'
            ]
            instance.run (commandLineOptions)

            # return output path
            return [outputNamePrefix + '.png']
        else:
            assert False, "unexpected class"

    else:
        # render csg tree
        attributes = getImageAttributes ()
        result = createSceneFunc (attributes, False)
        images = []
        for pair in result:
            images.append (openscad.getRendering ('png', pair[1], pair[0]))
        return images
