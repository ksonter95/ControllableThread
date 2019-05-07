Examples
========

.. contents:: :local:
   :depth: 3

Quickstart
----------

This code example can be found in the file ``examples/quickstart.py``.  It is an
example of how to create a class that inherits from
:class:`ControllableThread <cthread.ControllableThread>`.  No functionality has
been added to any of the states.  The lines: 

.. literalinclude:: ../../examples/quickstart.py
   :language: python
   :linenos:
   :lines: 14,15

can be replaced in each of the state callback functions with functional state
code that is specific to the user's needs.

.. literalinclude:: ../../examples/quickstart.py
   :language: python
   :linenos:

This code gives the following output:

.. code-block:: bash

   >> Starting thread: QuickstartThread...
   >> (Re)initialising thread...
   >> Thread activated!
   >> Pausing thread...
   >> Thread paused!
   >> Resuming thread...
   >> Thread activated!
   >> (Re)initialising thread...
   >> Thread activated!
   >> Killing thread...
   >> Stopped thread: QuickstartThread!

Alternative Thread states
-------------------------

This code example can be found in the file ``examples/alternative_state.py``.
It is an example of how to create a class that inherits from
:class:`ControllableThread <cthread.ControllableThread>` with additional
allowable thread states.  No functionality has been added to any of the 
additional states.  The lines:

.. literalinclude:: ../../examples/alternative_state.py
   :language: python
   :linenos:
   :lines: 28,29

can be replaced in each of the additional state callback functions with
functional state code that is specific to the user's needs.

.. note::
   There are two steps that must be followed when creating a
   :class:`cthread.ControllableThread` instance with alternative states:

   1. Initialise the :class:`cthread.ControllableThread` parent class with
      additional kwargs of the form **name: callback**. Each state name and
      callback function must be unique.
   2. Supply a callback function for each alternative state with the same name
      as that which was passed to the parent class in step 1 above.
   
   These two steps are highlighted in the proceeding code.

   Then, in order to transition the thread into one of the alternative states,
   the public method :py:attr:`cthread.ControllableThread.run()` must be called
   with the ``name`` parameter identical to the name specified in the kwargs
   from step 1 above.

.. literalinclude:: ../../examples/alternative_state.py
   :language: python
   :emphasize-lines: 14-20,37-39,41-43
   :linenos:

This code gives the following output:

.. code-block:: bash

   >> Starting thread: Starting thread: AlternativeStateThread...
   >> (Re)initialising thread...
   >> Thread activated!
   >> Transitioning thread to ALT1 state...
   >> Transitioning thread to ALT2 state....
   >> Killing thread...
   >> Stopped thread: AlternativeStateThread!