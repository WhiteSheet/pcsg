Getting Started
===============

Installation
````````````

Installation process has only be tested on Ubuntu 20.04 yet, however *pcsg* should run on any operating system.
You need to install OpenScad, PovRay, Mencoder and MP4Box from gpac and make those tools available via the **PATH** variable.



Installation on Ubuntu 20.04
````````````````````````````

.. code-block:: bash

    # Install python 3 packages
    sudo apt-get install python3 python3-pip python3-venv

    # OpenScad is required to run pcsg
    sudo apt-get install openscad

    # For raytracing support, install povray
    sudo apt-get install povray

    # Optional requirements for video encoding
    sudo apt-get install mencoder gpac

    # Install pcsg
    pip3 install pcsg



First steps
```````````

After installing *pcsg*, you should be able to run one of the :ref:`Examples<Examples>`:

.. code-block:: bash

    # Download *gear.py* example file.
    wget https://raw.githubusercontent.com/WhiteSheet/pcsg/main/doc/source/examples/tools/gear.py

    # Render a single frame of the gear example
    python3 gear.py render --fmt png gears

    # Creating an mp4 video:
    python3 gear.py animation -j 8 gears
