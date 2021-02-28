from pcsg import tool
from pcsg import animation
from pcsg import solid




# Create a new example tool
class SimpleExample (tool.Tool):
    """
    Simple example tool.
    """
    def __init__ (self):
        super ().__init__ (
            name =          "Simple example",
            description =   "Most simple example tool."
        )


    def attributes (self):
        """
        Set camera.
        """
        return super ().attributes ().override ({
            'camera.view': (0, 0, 0, 20, -20, 0, 30)
        })



    def scene (self, attributes):
        """
        Build example scene.
        """
        return solid.Cylinder (
            height = 5, 
            radius1 = 3, 
            radius2 = 2,
            attributes = ({
                'material': (0.9, 0.6, 0.6)
            })
        )




# Run as command line tool
if __name__ == "__main__":
    SimpleExample ().run ()