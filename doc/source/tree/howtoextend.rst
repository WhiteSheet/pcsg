Concepts behind *pcsg*
======================



Immutable Objects
*****************

A basic concept behind the *pcsg* tree are immutable objects.
Once an immubtable object is created it can not be modified anymore.

.. currentmodule:: pcsg.immutable

.. autoclass:: Object
    :members:



Data objects
````````````

.. autoclass:: DataObject
    :members:
    :special-members: __hash__



Implementing own data objects
`````````````````````````````

.. code-block:: python

    class MyBaseObject (immutable.DataObject):
        """
        Example for implementing a simple DataObject class.
        """
        def __init__ (self, value = 1):
            super ().__init__ ()
            self.value = value

        # List attributes for copy construction
        @staticmethod
        def _copyConstructorAttributes ():
            return (
                'value',        #< add field for copy construction
            )

        # List attributes for hash and comparision functions, 
        # when not defined _copyConstructorAttributes will be used
        @staticmethod
        def _compareAttributes ():
            return (
                'value',        #< add field for comparision
            )



    class MyObject (MyBaseObject):
        """
        Example for implementing a derived DataObject class.
        """
        def __init__ (self, value = 1, other = 2, noCompare = 3):
            super ().__init__ (value = value)
            self.other = other
            self.noCompare = noCompare

        @staticmethod
        def _copyConstructorAttributes ():
            return (
                MyBaseObject,   #< also copy values of base class
                'other',        #< add field for copy construction
                'noCompare'     #< add field for copy construction
            )

        @staticmethod
        def _compareAttributes ():
            return (
                MyBaseObject,   #< also compare values of base class
                'other'         #< add field for comparision
            )



Hash
****

The *hash* module generates hashcodes for *values* by deep inspection.

A hashcode is guaranteed to be the same for equal *values*, but equal hashcodes do not guarantee that the *values* are equal.
The hashcode algorithms are designed to minimize the probability of a hash collision, but nevertheless different *values* may have the same hashcode.

For primitive types like booleans, strings, floats the value will be converted to a hashcode.
Lists, Tuples and dictionaries are hashed by deep inspection. The hashcode of an object will be calculated via deep inspection by default. 
When an object implements its own *__hash__()* method, the result of *__hash__()* will used to calculate the returned hashcode and no deep inspection will not be performed.

.. currentmodule:: pcsg.util

.. automethod:: pcsg.util.hash



Cache
*****

The cache stores already computed items by a hash value. It is also used to provide a temporary directory for generating temporary files.

.. currentmodule:: pcsg.util.cache

.. automethod:: pcsg.util.cache.setup
.. automethod:: pcsg.util.cache.temporary
.. automethod:: pcsg.util.cache.load
.. automethod:: pcsg.util.cache.store
.. automethod:: pcsg.util.cache.persistentPath
