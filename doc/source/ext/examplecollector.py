import importlib
import sys
import inspect
import os
from docutils import nodes
import docutils
from docutils.parsers.rst import Directive
from sphinx.locale import _
from sphinx.util.docutils import SphinxDirective
from exampleimg import runtime
from docutils.statemachine import StringList
from docutils.parsers import rst
from docutils import frontend
from docutils.utils import Reporter
from pcsg import tool




class example(nodes.container, nodes.Element):
    pass




def _parseRstString (text, target):
    """
    Parse RST string and add content to target.
    """
    parser = rst.Parser ()
    settings = frontend.OptionParser ().get_default_values ()
    settings.tab_width = 4
    settings.pep_references = False
    settings.rfc_references = False
    document = docutils.utils.new_document ("src", settings)
    parser.parse (text, document)
    for child in document.children:
        target += child




def buildExampleNode (directive, exampleDoc, exampleFuncs):
    # build container with headline
    containerId = directive.env.new_serialno('exampleimg-container')
    containerIdStrRaw = str (containerId)
    containerIdStr = 'exampleimg_cid_' + containerIdStrRaw
    node = example (classes = ['exampleimg_container', 'exampleimg_container_' + containerIdStrRaw, containerIdStr], literal_block=True)
    _parseRstString (exampleDoc, node)

    # build child container containers
    childrenContainer = nodes.container (classes = ['exampleimg_children_thumbs', 'exampleimg_children_thumbs_' + containerIdStrRaw, containerIdStr])
    node += childrenContainer

    childCodeContainers = nodes.container (classes = ['exampleimg_details', 'exampleimg_details_' + containerIdStrRaw, containerIdStr])

    # build documentation for each item
    childId = 0
    for exampleName, exampleFunc, exampleDoc in exampleFuncs:
        # generate example thumbnail image
        thumbnailImagePath = runtime.renderImageThumbnail (exampleFunc, directive.config.exampleimg_cache_folder)
        thumbCountClass = 'exampleimg_thumbcount_' + str (len (thumbnailImagePath))

        # create an example container
        childIdStrRaw = str (containerId) + "_" + str (childId)
        childIdStr = "exampleimg_cid_" + childIdStrRaw
        child = nodes.container (classes = ['exampleimg_child_thumb', 'exampleimg_child_thumb_' + childIdStrRaw, childIdStr, thumbCountClass])
        childrenContainer += child

        # write thumbnail image
        childImageContainer = nodes.container (classes = ['exampleimg_thumb_images', 'exampleimg_thumb_images_' + childIdStrRaw, childIdStr])
        for image in thumbnailImagePath:
            childImage = nodes.container (classes = ['exampleimg_thumb_image', 'exampleimg_thumb_image_' + childIdStrRaw, childIdStr])
            # need to prepend a slash to search in absolute directory
            childImage += nodes.image (uri = '/' + image)
            childImageContainer += childImage
        child += childImageContainer

        # example doc rst content + example code
        exampleSplit = exampleDoc.split ('\n')

        # find split position
        splitPos = None
        for splitPosCandidate in range (0, len (exampleSplit) - 1):
            if (exampleSplit[splitPosCandidate].strip () == "") and (exampleSplit[splitPosCandidate + 1].strip () == ""):
                splitPos = splitPosCandidate
                break

        # do split of description and code
        if (splitPos == None):
            splitPos = len (exampleSplit)
        exampleRstDoc = '\n'.join (exampleSplit[0:splitPos])
        if splitPos < (len (exampleSplit) - 1):
            exampleCode = exampleSplit[splitPos + 2:]
        else:
            exampleCode = []

        # description for example
        childDesription = nodes.container (classes = ['exampleimg_childdescription', 'exampleimg_childdescription_' + childIdStrRaw, childIdStr])
        _parseRstString (exampleRstDoc, childDesription)
        child += childDesription

        # create detail block
        detailBlock = nodes.container (classes=['exampleimg_detail', 'exampleimg_detail_' + childIdStrRaw, childIdStr])
        detailCaption = nodes.container (classes=['exampleimg_detail_caption', 'exampleimg_detail_caption_' + childIdStrRaw, childIdStr])
        _parseRstString ("Example: " + exampleRstDoc, detailCaption)
        detailBlock += detailCaption

        # generate example image
        imagePath = runtime.renderImage (exampleFunc, directive.config.exampleimg_cache_folder)

        # detail image block
        detailImageContainer = nodes.container (classes = ['exampleimg_detail_images', 'exampleimg_detail_images_' + childIdStrRaw, childIdStr])
        for image in imagePath:
            detailImage = nodes.container (classes = ['exampleimg_detail_image', 'exampleimg_detail_image_' + childIdStrRaw, childIdStr])
            # need to prepend a slash to search in absolute directory
            detailImage += nodes.image (uri = '/' + image)
            detailImageContainer += detailImage
        detailBlock += detailImageContainer

        # detail code block
        if len (exampleCode) > 0:
            codeBlock = nodes.container (classes=['exampleimg_detail_code', 'exampleimg_detail_code_' + childIdStrRaw, childIdStr])
            exCode = '.. code-block:: python\n\n'
            for codeLine in exampleCode:
                exCode += '    ' + codeLine + '\n'
            _parseRstString (exCode, codeBlock)
            detailBlock += codeBlock
        childCodeContainers += detailBlock

        # increment child index
        childId += 1

    # add code containers
    node += childCodeContainers
    return node
    



def visit_exampleimg_node(self, node):
    self.visit_container(node)




def depart_exampleimg_node(self, node):
    self.depart_container(node)




class ExampleimgDirective(SphinxDirective):
    """
    Parsing directive for exampleimg.
    """
    has_content = True

    def run(self):
        # initialize rendering runtime
        runtime.initialize (str (self.config.exampleimg_cache_folder))

        # parse more than once class attribute
        classesT = self.content[0].strip ().split (' ')
        classes = []
        for c in classesT:
            if c.strip () != "":
                classes.append (c)


        # loop for each element
        exampleFuncs = []
        for classElement in classes:
            # create source path
            exampleClassPath = classElement.split ('.')
            sourcePath = str (self.config.exampleimg_source_folder).split (os.path.sep)
            modulePath = os.path.sep.join (sourcePath + exampleClassPath[0 : len (exampleClassPath) - 2])
            moduleName = exampleClassPath[-2]
            className = exampleClassPath[-1]

            spec = importlib.util.spec_from_file_location (moduleName, modulePath + os.path.sep + moduleName + ".py")
            examplePackage = importlib.util.module_from_spec(spec)
            examplePackage.__package__ = 'examples'
            sys.modules[moduleName] = examplePackage

            spec.loader.exec_module(examplePackage)

            # find class of module
            exampleClass = None
            lstr = ""
            for name, instance in inspect.getmembers(examplePackage, inspect.isclass):
                lstr += " " + name
                if name == className:
                    exampleClass = instance
                    break
            assert exampleClass != None, "unable to load class " + self.content[0] + " in module " + str (examplePackage) + " - " + className + " - " + lstr

            # process example tools
            if issubclass (exampleClass, tool.Tool):
                # append tool class to example funcs
                exampleDoc = "\n"
                exampleFuncs.append ((exampleClass.__name__, exampleClass, inspect.getdoc (exampleClass)))
            else:
                # class is instanciated, collect comments and example methods
#               TODO: currently not displaying example doc string
#               exampleDoc = inspect.getdoc (exampleClass)
                exampleDoc = "\n"
                if exampleDoc == "":
                    exampleDoc = None
                for name, instance in inspect.getmembers (exampleClass, predicate = inspect.isfunction):
                    if name.startswith ('example'):
                        exampleFuncs.append ((name, instance, inspect.getdoc (instance)))


        # create example node
        example_node = buildExampleNode (self, exampleDoc, exampleFuncs)

        # create target node
        targetid = 'exampleimg-%d' % self.env.new_serialno('exampleimg')
        targetnode = nodes.target('', '', ids=[targetid])

        # add to registry
        if not hasattr(self.env, 'exampleimg_examples'):
            self.env.exampleimg_examples = []
        self.env.exampleimg_examples.append({
            'docname': self.env.docname,
            'lineno': self.lineno,
            'example': example_node.deepcopy(),
            'target': targetnode,
        })

        return [targetnode, example_node]




def purge_exampleimg(app, env, docname):
    """
    Purge old example records.
    """
    if not hasattr(env, 'exampleimg_examples'):
        return
    env.exampleimg_examples = [example for example in env.exampleimg_examples
                          if example['docname'] != docname]




def merge_exampleimg(app, env, docnames, other):
    """
    Merge after parallel processing.
    """
    if not hasattr(env, 'exampleimg_examples'):
        env.exampleimg_examples = []

    if hasattr(other, 'exampleimg_examples'):
        env.exampleimg_examples.extend(other.exampleimg_examples)




def process_exampleimg_nodes(app, doctree, fromdocname):
    """
    Process example nodes.
    """
    # Replace all todolist nodes with a list of the collected todos.
    # Augment each todo with a backlink to the original location.
    env = app.builder.env

    # create environment
    if not hasattr(env, 'exampleimg_examples'):
        env.exampleimg_examples = []




def setup(app):
    app.add_config_value ('exampleimg_source_folder', os.path.abspath ('.'), 'html')
    app.add_config_value ('exampleimg_cache_folder', os.path.abspath ('.exampleimg.cache'), 'html')

    app.add_node(example,
                 html = (visit_exampleimg_node, depart_exampleimg_node),
                 latex = (visit_exampleimg_node, depart_exampleimg_node),
                 text = (visit_exampleimg_node, depart_exampleimg_node))

    app.add_directive ('exampleimg', ExampleimgDirective)
    app.connect ('doctree-resolved', process_exampleimg_nodes)
    app.connect ('env-purge-doc', purge_exampleimg)
    app.connect ('env-merge-info', merge_exampleimg)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
