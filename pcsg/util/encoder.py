import os
import subprocess
from shutil import copyfile
from shutil import rmtree
import pathlib
from .external import openscad
from . import hash
from . import cache




class Encoder:
    """
    Base class of video encoder taking single frame images.
    """

    def __init__ (self):
        pass


    def name (self):
        """
        Returns the name of the materializer.
        """
        assert False, "To be implemented by child"


    def assertUsable (self):
        """
        Returns None if the video encoder is usable, an error string if not.
        """
        assert False, "To be implemented by child"


    def presets (self):
        """
        Retuns a list of supported presets.
        """
        assert False, "To be implemented by child"


    def defaultPreset (self):
        """
        Returns the default preset of the video encoder.
        """
        assert False, "To be implemented by child"


    def extension (self):
        """
        Returns the extension of the files generated by the video encoder.
        """
        assert False, "To be implemented by child"


    def encode (self, frames, fps, destinationPath = None, preset = None):
        """
        Generate a video from a sequence of frames.
        """
        assert False, "To be implemented by child"




class _AviH264Encoder (Encoder):
    """
    Video encoder using "mencoder" to produce h264 encoded avi files.
    """
    def __init__ (self):
        super ().__init__ ()
        self.usableChecked = False
        self.usableError = None

    presetMap = {
            'ultrafast': 'ultrafast',
            'superfast': 'superfast',
            'veryfast': 'veryfast',
            'faster': 'faster',
            'fast': 'fast',
            'medium': 'medium',
            'slow': 'slow',
            'slower': 'slower',
            'veryslow': 'veryslow',
            'insane': 'placebo'
    }


    @staticmethod
    def _getMEncoderRunnable ():
        return "mencoder"


    def name (self):
        return "avi-h264"


    def assertUsable (self):
        if self.usableChecked:
            return self.usableError
        try:
            # check if mencoder is runnable
            result = subprocess.run ([_AviH264Encoder._getMEncoderRunnable ()], capture_output = True)
            if result.returncode != 0:
                if not 'MEncoder' in (str(result.stdout) + ' ' + str(result.stderr)):
                    self.usableError = "Can not execute mencoder. Is inside PATH variable?"
            else:
                self.usableError = None
            self.usableChecked = True
            return self.usableError
        except:
            self.usableError = "Can not execute " + _AviH264Encoder._getMEncoderRunnable () + ". Is inside PATH variable?"
        self.usableChecked = True
        return self.usableError
        

    def presets (self):
        return _AviH264Encoder.presetMap.keys ()


    def defaultPreset (self):
        return 'insane'


    def extension (self):
        return 'avi'


    def encode (self, frames, fps, destinationPath = None, preset = None):
        # generate a file name hash by source frames names fps and preset.
        hc = hash ("video", "h264", "avi", fps, preset)
        for frame in frames:
            hc = hash (hc, str (pathlib.Path (frame).resolve ()))

        # check if file is already in cache
        cachePath = pathlib.Path (cache.persistentPath (hc, self.extension ())).resolve ()
        if cachePath.exists ():
            # return cached file or create copy
            if destinationPath == None:
                return str (cachePath)
            else:
                try:
                    copyfile (cachePath, pathlib.Path (destinationPath))
                except:
                    return None
                return str (destinationPath)

        # video doesn't exist, create it...

        # create temp working directory
        tempDir = cache.temporary ()
        os.makedirs (tempDir)

        # get extension of source frames
        framesExtension = None
        for frame in frames:
            fExt = str (frame).split ('.')[-1]
            if framesExtension == None:
                framesExtension = fExt
            else:
                assert fExt == framesExtension, "expected all input frames to have the same extension"

        # symlink video source files into temp directory
        imgId = 0
        for frame in frames:
            # create image index
            imgIdStr = str (imgId)
            while len (imgIdStr) < 6:
                imgIdStr = "0" + imgIdStr
            os.symlink (frame, tempDir + os.path.sep + "img_" + imgIdStr + "." + framesExtension)
            imgId += 1

        # process video rendering in temp directory with sym linked images
        lastDir = os.path.abspath (os.curdir)
        os.chdir (tempDir)

        # temporary avi output
        cacheFileTempAvi = "temp.avi"

        # TODO:
        silent = True

        # prepare command
        command = [_AviH264Encoder._getMEncoderRunnable ()]
        command.append ("mf://img_*.png")
        command.append ("-mf")
        command.append ("fps=" + str (fps) + ":type=png")
        command.append ("-oac")
        command.append ("copy")
        command.append ("-ovc")
        command.append ("x264")
        command.append ("-x264encopts")
        command.append ("preset=" + _AviH264Encoder.presetMap[preset] + ":tune=animation:threads=auto")
        command.append ("-o")
        command.append (cacheFileTempAvi)

        # do compression
        result = subprocess.run (command, capture_output=silent)
        if result.returncode != 0:
            if silent:
                print (result.stderr)
                print (result.stdout)
            try:
                os.chdir (lastDir)
                rmtree (tempDir)
            except:
                pass
            return None

        # copy to cache
        cacheFile = cache.persistentPath (hc, self.extension (), True)
        os.rename (cacheFileTempAvi, cacheFile)

        # leave and remove temporary directory
        os.chdir (lastDir)
        try:
            rmtree (tempDir)
        except:
            pass

        # need to copy to output file?
        if destinationPath == None:
            return str (cacheFile)
        else:
            try:
                copyfile (cacheFile, pathlib.Path (destinationPath))
            except:
                return None
            return str (destinationPath)

"""
Static instance of AVI-H264 Encoder.
"""
AviH264 = _AviH264Encoder ()




class _MP4H264Encoder (Encoder):
    """
    MP4 encoder using AviH264 encoder.
    """

    def __init__ (self):
        super ().__init__ ()
        self.usableChecked = False
        self.usableError = None


    def name (self):
        return "mp4-h264"


    @staticmethod
    def _getMP4BoxRunnable ():
        return "MP4Box"


    def assertUsable (self):
        """
        Returns None if the video encoder is usable, an error string if not.
        """
        if self.usableChecked:
            return self.usableError
        try:
            # check if parent encoder is runnable
            aviErr = AviH264.assertUsable ()
            if aviErr != None:
                self.usableChecked = True
                self.usableError = aviErr
                return self.usableError

            # check if mencoder is runnable
            result = subprocess.run ([_MP4H264Encoder._getMP4BoxRunnable ()], capture_output = True)
            if result.returncode != 0:
                if not 'MP4Box' in (str(result.stdout) + ' ' + str(result.stderr)):
                    self.usableError = "Can not execute MP4Box. Is inside PATH variable?"
            else:
                self.usableError = None
            self.usableChecked = True
            return self.usableError
        except:
            self.usableError = "Can not execute " + _MP4H264Encoder._getMP4BoxRunnable () + ". Is inside PATH variable?"
        self.usableChecked = True
        return self.usableError


    def presets (self):
        """
        Retuns a list of supported presets.
        """
        return AviH264.presets ()


    def defaultPreset (self):
        """
        Returns the default preset of the video encoder.
        """
        return AviH264.defaultPreset ()


    def extension (self):
        """
        Returns the extension of the files generated by the video encoder.
        """
        return 'mp4'


    def encode (self, frames, fps, destinationPath = None, preset = None):
        """
        Generate a video from a sequence of frames.
        """
        # generate a file name hash by source frames names fps and preset.
        hc = hash ("video", "h264", "mp4", fps, preset)
        for frame in frames:
            hc = hash (hc, str (pathlib.Path (frame).resolve ()))

        # check if file is already in cache
        cachePath = pathlib.Path (cache.persistentPath (hc, self.extension ())).resolve ()
        if cachePath.exists ():
            # return cached file or create copy
            if destinationPath == None:
                return str (cachePath)
            else:
                try:
                    copyfile (cachePath, pathlib.Path (destinationPath))
                except:
                    return None
                return str (destinationPath)

        # video doesn't exist, create it...

        # Encode via parent encoder (get avi file path)
        preEncoded = AviH264.encode (frames, fps, None, preset)

        # create temp working directory
        tempDir = cache.temporary ()
        os.makedirs (tempDir)

        # symlink video into temporary directory
        os.symlink (preEncoded, tempDir + os.path.sep + 'input.avi')

        # process inside temporary directory
        lastDir = os.path.abspath (os.curdir)
        os.chdir (tempDir)

        # TODO:
        silent = True

        # unpack h264 stream
        unpackCommand = [_MP4H264Encoder._getMP4BoxRunnable (), "-aviraw", "video", 'input.avi']
        result = subprocess.run (unpackCommand, capture_output=silent)
        if result.returncode != 0:
            if silent:
                print (result.stderr)
                print (result.stdout)
            try:
                os.chdir (lastDir)
                rmtree (tempDir)
            except:
                pass
            return None

        # temporary output file
        cacheFileTemp = "output.mp4"

        # pack mp4 file
        packCommand = [_MP4H264Encoder._getMP4BoxRunnable (), "-add", "input_video.h264", cacheFileTemp]
        result = subprocess.run (packCommand, capture_output=silent)
        if result.returncode != 0:
            if silent:
                print (result.stderr)
                print (result.stdout)
            try:
                os.chdir (lastDir)
                rmtree (tempDir)
            except:
                pass
            return None

        # copy to cache
        cacheFile = cache.persistentPath (hc, self.extension (), True)
        os.rename (cacheFileTemp, cacheFile)

        # leave & remove temporary directory
        try:
            os.chdir (lastDir)
            rmtree (tempDir)
        except:
            pass

        # need to copy to output file?
        if destinationPath == None:
            return str (cacheFile)
        else:
            try:
                copyfile (cacheFile, pathlib.Path (destinationPath))
            except:
                return None
            return str (destinationPath)

"""
Static instance of MP4-H264 Encoder.
"""
MP4H264 = _MP4H264Encoder ()




"""
List of registered encoders.
"""
_registeredEncoders = [MP4H264, AviH264]




def getEncoders ():
    """
    Returns a list of all registered video encoder instances.
    """
    return _registeredEncoders




def getEncoder (name):
    """
    Returns an encoder by name or None if not found.
    """
    for m in _registeredEncoders:
        if m.name () == name:
            return m
    return None




def registerEncoder (encoder):
    """
    Registers an video encoder at the registry.
    """
    assert False, "TODO:"




def parseSettings (formatStr):
    """
    Parses a format and returns a tuple (encoderInstance, presetName). When parsing failed, encoderInstance will be None.
    """
    # split string
    fmt = formatStr.split ('.')
    if len (fmt) < 0:
        return (None, None)
    
    # find encoder
    encoderInstance = None
    for e in _registeredEncoders:
        if len (fmt) > 0:
            if e.name () == fmt[0]:
                encoderInstance = e
                break
        else:
            encoderInstance = _registeredEncoders[0] if len (_registeredEncoders) > 0 else None

    # return tuple with parsed settings
    presetName = '.'.join (fmt[1:])
    if presetName in (None, ""):
        if encoderInstance != None:
            presetName = encoderInstance.defaultPreset ()
    return (encoderInstance, presetName)




def extension (formatStr):
    """
    Get file extension for rendering format.
    """
    assert False, "TODO:"
