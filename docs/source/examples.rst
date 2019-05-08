Examples
========

.. contents:: :local:
   :depth: 3

.. note::
   In order for the :mod:`cthread` package to be fully functional, the developer
   must follow two coding practices:
   
   1. Any code within the
      :py:attr:`cthread.ControllableThread._active_callback()` callback function
      and any registered alternative state callback function must be:
      
      - Non-blocking (at the very least it must only block for a short
        period of time), and
      - Contain no indefinite ``while`` or ``for`` loops.
      
      In short, the :py:attr:`cthread.ControllableThread._active_callback()`
      callback function and any registered alternative state callback functions
      must be written to minimize its execution time.  This allows the thread
      to be controllable.  This is because it is only at the end of each
      callback function that a check is conducted to determine whether the
      state of the thread must be updated.
   2. The code within the
      :py:attr:`cthread.ControllableThread._started_callback()`
      :py:attr:`cthread.ControllableThread._paused_callback()`,
      :py:attr:`cthread.ControllableThread._resumed_callback()`, and
      :py:attr:`cthread.ControllableThread._killed_callback()` callback
      functions will only execute once.  There is a wrapper function for each
      callback function within the :class:`cthread.ControllableThread` class.
      This wrapper function automatically updates the thread state to
      :py:attr:`cthread.ThreadState.ACTIVE` at the completion of the
      :py:attr:`cthread.ControllableThread._started_callback()` and
      :py:attr:`cthread.ControllableThread._resumed_callback()` callback
      functions, and :py:attr:`cthread.ThreadState.IDLE` at the completion of
      the :py:attr:`cthread.ControllableThread._paused_callback()` callback
      function.  These callbacks should be written in such a way that they
      pause or resume/start thread functionality.

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
   :lines: 38,39

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